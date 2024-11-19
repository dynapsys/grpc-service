import grpc
from concurrent import futures
import time
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

# Importy wygenerowanych plików proto będą dodane po ich generacji
# import service_pb2
# import service_pb2_grpc

load_dotenv()

logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ExampleServiceServicer(object):  # service_pb2_grpc.ExampleServiceServicer
    def SayHello(self, request, context):
        logger.info(f"Otrzymano żądanie Hello od: {request.name}")
        response = {
            'message': f"Witaj {request.name}!",
            'timestamp': int(time.time())
        }
        return response  # service_pb2.HelloResponse(**response)

    def CountNumbers(self, request, context):
        logger.info(f"Rozpoczęto liczenie od {request.start} do {request.end}")
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        for number in range(request.start, request.end + 1):
            response = {
                'number': number,
                'is_prime': is_prime(number)
            }
            yield response  # service_pb2.CountResponse(**response)

    def ProcessItems(self, request_iterator, context):
        processed_items = []
        count = 0

        for request in request_iterator:
            count += 1
            logger.info(f"Przetwarzanie elementu: {request.item}")
            result = f"Przetworzono: {request.item} ({request.operation})"
            processed_items.append(result)

        return {  # service_pb2.ProcessSummary
            'processed_count': count,
            'results': processed_items
        }

    def Chat(self, request_iterator, context):
        for message in request_iterator:
            logger.info(f"Chat message from {message.username}: {message.content}")
            response = {
                'username': 'Server',
                'content': f"Otrzymano wiadomość od {message.username}",
                'timestamp': int(time.time())
            }
            yield response  # service_pb2.ChatMessage(**response)

def serve():
    port = int(os.getenv('GRPC_PORT', 50051))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # service_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logger.info(f"Serwer uruchomiony na porcie {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
