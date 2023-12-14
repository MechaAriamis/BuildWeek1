#Rilevazione delle porte attive
import socket

#inserire le IP della porta e definire in quale range andare a cercare la porta
target=input("Inserisci l'IP a cui fare lo scanner:\n")
portrange=input("Inserisci il range di porta su cui fare lo scan (es 1-100): ")

#lavorare sulla stringa inserita dall'utente in linea 5 (porte inserite)
lowport=int(portrange.split('-')[0])
highport=int(portrange.split('-')[1])

#print a chermo delle informazioni inserite
print("Scanning Host ", target, "from port ", lowport, "to port", highport)

#creazione ciclo for per andare a identificare le porte attive e il servizio di ogni porta
for port in range(lowport, highport):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status=s.connect_ex((target,port))
    if(status==0):
        service=socket.getservbyport(port)
        print("*** Port ',port, ' -OPEN***"," --SERVICE: ", service)
    s.close()
