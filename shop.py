import smtplib
from email.message import EmailMessage
from getpass import getpass

nume = str(input("Nume: "))
email = str(input("Email: "))
parola = str(getpass("Parola: "))
destinatar = str(input("Email-ul destinatarului: "))

while True:
	try:
		nrproduse = int(input(f"Buna, {nume}!\nCate produse doresti sa adaugi in lista de cumparaturi? " ))
	except ValueError:
		print ("Te rog sa introduci un numar.")
	else:
		break

produse = []
cantitati = []

for x in range(int(nrproduse)):

    produs = str(input('Introdu numele produsului: '))

    while True:
        try:
            cantitate = int(input('Introdu cantitatea produsului: '))
        except ValueError:
            print ("Te rog sa introduci un numar.")
        else:
            break

    produse.append(produs)
    cantitati.append(cantitate)

print ("Am adaugat urmatoarele produse in lista de cumparaturi:")

for x, y in zip (produse, cantitati):
    print (f'{x} x {y}')

gmail_user = email 
gmail_password = parola

msg = EmailMessage()
msg['Subject'] = "Lista Cumparaturi"
msg['From'] = gmail_user
msg['To'] = [destinatar]
message = ""
for i in range(max(len(produse), len(cantitati))):
    message = message + str(produse[i]) + " x " + str(cantitati[i]) + "\n"
msg.set_content(message)

try:
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(gmail_user, gmail_password)
    s.send_message(msg)
    s.quit()

    print ('\nEmail-ul a fost trimis.')

except:  
    print ('A aparut o eroare.')
    
print ("\nO zi buna!")

exit()