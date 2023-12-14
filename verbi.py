#Rilevare i verbi sulla porta 80
import http.client

#inserimento degli input IP e port che vogliamo controllare
host = input("Inserire l'IP del sistema target:\n")
port=input("Inserire la porta del sistema target (default port 80):\n")

#per impostare come default la porta 80 in caso di mancato inserimento della line 6
if(port == ""):
    port="80"
#creiamo la connessione per host e porta inseriti e alla pagina interessata
try:
    connection = http.client.HTTPConnection(host,port)
    connection.request('OPTION', 'http://192.168.50.101/phpMyAdmin/phpMyAdmin.html')
    response = connection.getresponse()
    methods=response.getheader('allow').split(',')#definire i verbi permessi
    print("i metodi abilitati sono:\n")#print a schermo dei verbi
    for method in methods:
        print(method)
    connection.close()

#stampa a schermo la mancata connessione al server
except ConnectionRefusedError:
    print("Connessione fallita")
