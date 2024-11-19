import pytest
import grpc
import time
from src.server import ExampleServiceServicer

def test_say_hello():
    servicer = ExampleServiceServicer()
    request = type('HelloRequest', (), {'name': 'Test'})()
    context = {}

    response = servicer.SayHello(request, context)
    assert 'Test' in response['message']
    assert 'timestamp' in response

def test_count_numbers():
    servicer = ExampleServiceServicer()
    request = type('CountRequest', (), {'start': 1, 'end': 5})()
    context = {}

    responses = list(servicer.CountNumbers(request, context))
    assert len(responses) == 5
    assert all('number' in r for r in responses)
    assert all('is_prime' in r for r in responses)

# Dodaj więcej testów...
