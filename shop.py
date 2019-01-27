import smtplib

from email.message import EmailMessage

from getpass import getpass

from collections import defaultdict


def get_user_input(message, type=str):
    while True:
        try:
            return type(input(message))
        except ValueError:
            print (f"Please input a {type}.")


def add_item(shopping_list):
    product = get_user_input("Input the product name: ")
    quantity = get_user_input("Input the product quantity: ", int)
    shopping_list[product] += quantity


def print_list(shopping_list):
    for product, quantity in shopping_list.items():
        print(product, "x", quantity)


def email_to(shopping_list, from_email, password, *recipients):
    email = EmailMessage()
    email['Subject'] = "Shopping List"
    email['From'] = from_email
    email['To'] = recipients
    message = "\n".join(f"{product} x {quantity}" for product, quantity in shopping_list.items())
    email.set_content(message)

    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        s.login(from_email, password)
        s.send_message(email)
        s.quit()
        print ("\nThe email has been sent.")
    except Exception as e:  
        print ("\nAn error occurred:", e)
   

if __name__ == "__main__":
    name = input("Name: ")
    n = get_user_input(f"Hi, {name}!\nHow many products do you want to add to the shopping list? ", int)
    shopping_list = defaultdict(int)
    for _ in range(n):
        add_item(shopping_list)
    print("\nThese products have been added to the shopping list:")
    print_list(shopping_list)

    from_email = input("\nEmail: ")
    password = getpass("Password: ")
    recipient = input("Recipient's email: ")
    email_to(shopping_list, from_email, password, recipient)

    print ("\nHave a nice day!")

exit()