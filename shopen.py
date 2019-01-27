import smtplib
from email.message import EmailMessage
from getpass import getpass

name = str(input("Name: "))
email = str(input("Email: "))
password = str(getpass("Password: "))
recipient = str(input("Recipient's email: "))

while True:
	try:
		productsnm = int(input(f"Hi, {name}!\nHow many products do you want to add to the shopping list? " ))
	except ValueError:
		print ("Please input a number.")
	else:
		break

products = []
quantities = []

for x in range(int(productsnm)):

    product = str(input('Input the product name: '))

    while True:
        try:
            quantity = int(input('Input the product quantity: '))
        except ValueError:
            print ("Please input a number.")
        else:
            break

    products.append(product)
    quantities.append(quantity)

print ("These products have been added to the shopping list:")

for x, y in zip (products, quantities):
    print (f'{x} x {y}')

gmail_user = email 
gmail_password = password

msg = EmailMessage()
msg['Subject'] = "Shopping List"
msg['From'] = gmail_user
msg['To'] = [recipient]
message = ""
for i in range(max(len(products), len(quantities))):
    message = message + str(products[i]) + " x " + str(quantities[i]) + "\n"
msg.set_content(message)

try:
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(gmail_user, gmail_password)
    s.send_message(msg)
    s.quit()

    print ('\nThe email has been sent.')

except:  
    print ('An error occurred.')
    
print ("\nHave a nice day!")

exit()
