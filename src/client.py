import grpc
import time
from dotenv import load_dotenv
import os
import logging

# Importy wygenerowanych plików proto będą dodane po ich generacji
# import service_pb2
# import service_pb2_grpc

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run():
    port = os.getenv('GRPC_PORT', '50051')
    channel = grpc.insecure_channel(f'localhost:{port}')
    stub = None  # service_pb2_grpc.ExampleServiceStub(channel)

    # Test SayHello
    logger.info("Testing SayHello...")
    response = stub.SayHello(None)  # service_pb2.HelloRequest(name="User")
    logger.info(f"SayHello Response: {response.message}")

    # Test CountNumbers
    logger.info("Testing CountNumbers...")
    count_request = None  # service_pb2.CountRequest(start=1, end=10)
    for response in stub.CountNumbers(count_request):
        logger.info(f"Number: {response.number}, Is Prime: {response.is_prime}")

    # Test ProcessItems
    logger.info("Testing ProcessItems...")
    def item_generator():
        items = ["Item1", "Item2", "Item3"]
        for item in items:
            yield None  # service_pb2.ProcessRequest(item=item, operation="TEST")
            time.sleep(1)

    process_response = stub.ProcessItems(item_generator())
    logger.info(f"Processed {process_response.processed_count} items")
    for result in process_response.results:
        logger.info(f"Result: {result}")

    # Test Chat
    logger.info("Testing Chat...")
    def message_generator():
        messages = ["Hello", "How are you?", "Goodbye"]
        for msg in messages:
            yield None  # service_pb2.ChatMessage(
                # username="Client",
                # content=msg,
                # timestamp=int(time.time())
            # )
            time.sleep(1)

    for response in stub.Chat(message_generator()):
        logger.info(f"Server response: {response.content}")

if __name__ == '__main__':
    run()
