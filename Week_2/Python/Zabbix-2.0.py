#!/usr/bin/env python3
import json

MOCK_TOKEN = "pobrany-z-ukrytego-pliku-env-123"

try:
    with open("data.json", "r", encoding="utf-8") as file:
        dane = json.load(file)
        print(f" Sukces! Autoryzacja tokenem {MOCK_TOKEN} powiodła się.")
        print(f"Pomyślnie odczytano {len(dane)} błędy z pliku data.json.")

except FileNotFoundError:
    print(" CRITICAL ERROR: Plik data.json nie istnieje! Skrypt nie może kontynuować.")
    print("Log: Awaria obsługi plików lokalnych.")