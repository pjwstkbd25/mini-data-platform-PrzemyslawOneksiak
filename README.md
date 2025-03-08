**Projekt zaliczeniowy na zajęcia BigData**  
**Autor: Przemysław Oneksiak s34225**

Projekt zakłada stworzenie pierwszej części systemu odpowiedzialnego za wczytywanie danych z pliku csv oraz zapisywanie   
go w formie tabelarycznej w bazie SQL - PostgreSQL. Aby poprawnie uruchomić program należy:  
1. Ustawić hasło do użytkownika postgres w lokalizacji /secrets/postgres_password.txt: echo "supersecretpassword" > ./secrets/postgres_password.txt
2. Uruchomienie kontenera docker w trybie deweloperskim: docker-compose up -d postgres
3. Uruchomić plik app.py z argumentami: --csv_path, --db_path, --table_name