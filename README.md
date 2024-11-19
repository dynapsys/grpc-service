# Example gRPC Service

Przykładowa usługa gRPC implementująca różne typy komunikacji:
- Unary RPC (SayHello)
- Server Streaming (CountNumbers)
- Client Streaming (ProcessItems)
- Bidirectional Streaming (Chat)

## Instalacja

1. Klonowanie repozytorium:
```bash
git clone <repository_url>
cd example-grpc-service
```

2. Uruchomienie skryptu instalacyjnego:
```bash
./scripts/setup.sh
```

## Uruchomienie

1. Aktywacja środowiska wirtualnego:
```bash
source venv/bin/activate
```

2. Uruchomienie serwera:
```bash
python src/server.py
```

3. W innym terminalu, uruchomienie klienta:
```bash
python src/client.py
```

## Rozwój

1. Modyfikacja definicji proto:
   Edytuj plik `proto/service.proto`

2. Generowanie kodu:
```bash
./scripts/generate_proto.sh
```

3. Uruchomienie testów:
```bash
pytest tests/
```

## Struktura projektu

- `proto/` - Definicje protokołu
- `src/` - Kod źródłowy
  - `server.py` - Implementacja serwera
  - `client.py` - Przykładowy klient
  - `generated/` - Wygenerowany kod
- `tests/` - Testy
- `scripts/` - Skrypty pomocnicze

## Licencja

[LICENSE](LICENSE)