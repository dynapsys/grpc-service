#!/bin/bash
set -e

# Przejście do katalogu głównego projektu
cd "$(dirname "$0")/.."

# Utworzenie katalogu na wygenerowane pliki
mkdir -p src/generated

# Generowanie plików Python
python3 -m grpc_tools.protoc \
    -I proto \
    --python_out=src/generated \
    --grpc_python_out=src/generated \
    proto/*.proto

# Poprawienie importów w wygenerowanych plikach
sed -i 's/import service_pb2/from . import service_pb2/' src/generated/service_pb2_grpc.py

# Dodanie __init__.py
touch src/generated/__init__.py

echo "Generowanie proto zakończone!"
