#!/bin/bash
set -e

# Tworzenie środowiska wirtualnego
python3 -m venv venv
source venv/bin/activate

# Instalacja zależności
pip install -r requirements.txt

# Generowanie plików proto
./scripts/generate_proto.sh

echo "Instalacja zakończona!"
