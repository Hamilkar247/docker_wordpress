1) Skopiuj  `cp .env .env.example` i zmień wedle uznania
2) `docker-compose up` - uruchomy obraz
3) gdy chcesz zatrzymać kontener 
`docker-compose down
4) Usuń kontenery i ich dane
`docker-compose down --volumes`
By widzieć recordy bazy - domyślnie http://127.0.0.1:9090 tutaj się można zalogować na dane mysqla

#uwaga db dbhost to nazwa serwisu
#uwaga 2 - w adminerze serwer to również ta nazwa obowiązuje

Błąd Error establishing a database connection
wynikał z tego że hasło wordpressa do bazy a hasło do bazy mysql odbiegał od siebie odbiega od siebie


