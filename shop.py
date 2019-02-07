import smtplib

from email.message import EmailMessage

from getpass import getpass

from collections import defaultdict


def get_user_input(message, type=str):
    while True:
        try:
            return type(input(message))
        except ValueError:
            print(f"Please input a {type}.")


class ShoppingList:

    def __init__(self):
        self.items = defaultdict(int)

    def __str__(self):
        return ("\n".join(f"{product} x {quantity}"
                for product, quantity in self.items.items()))

    def add_item(self, product, quantity):
        self.items[product] += quantity

    def email_to(self, from_email, password, *recipients):
        email = EmailMessage()
        email['Subject'] = "Shopping List"
        email['From'] = from_email
        email['To'] = recipients
        message = str(self)
        email.set_content(message)

        try:
            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            s.ehlo()
            s.login(from_email, password)
            s.send_message(email)
            s.quit()
            print("\nThe email has been sent.")
        except Exception as e:
            print("\nAn error occurred:", e)


if __name__ == '__main__':
    name = input("Name: ")
    n = get_user_input(f"Hi, {name}!\nHow many products do you want to add to the shopping list? ", int)
    shopping_list = ShoppingList()
    for _ in range(n):
        product = get_user_input("Input the product name: ")
        quantity = get_user_input("Input the product quantity: ", int)
        shopping_list.add_item(product, quantity)
    print("\nThese products have been added to the shopping list:")
    print(shopping_list)

    email = input("\nEmail: ")
    password = getpass("Password: ")
    recipient = input("Recipient's email: ")
    shopping_list.email_to(email, password, recipient)

    print("\nHave a nice day!")

exit()
