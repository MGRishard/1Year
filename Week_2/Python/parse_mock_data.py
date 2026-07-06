try:
    with open("mock_data.txt", "r", encoding="utf-8") as file:
        data = file.read()
        print(f" Sukces! Odczytano dane z pliku mock_data.txt.")
        print(f"Pomyślnie odczytano {len(data)} znaków z pliku mock_data.txt.")
except FileNotFoundError:
    print(" CRITICAL ERROR: Plik mock_data.txt nie istnieje! Skrypt nie może kontynuować.")