'''Sayyed Zainul Abedin ali has made the Class Article and Inventory dictionary and File_path function
   Natnael  '''





import csv

class Article:
    """
    Represents an article in the inventory or cart with a name, price, and quantity.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_Name(self):
        return self.name

    def get_Price(self):
        return self.price

    def get_Quantity(self):
        return self.quantity

    def set_Quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Article: {self.name}, Quantity: {self.quantity}, Price: {self.price:.2f}"

# Placeholder for the global INVENTORY dictionary
INVENTORY = {}

def read_data(file_path):
    """
    Reads the data from a CSV file and stores it in the global INVENTORY dictionary.
    """
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the headers
        for row in csvreader:
            name, quantity, price = row
            INVENTORY[name] = Article(name, float(quantity), int(price))

def display_menu():
    print("1. List all items, inventory and price \n2. List cart shopping items \n3. Add an item to the shopping cart \n4. Remove an item from the shopping cart \n5. Checkout \n6. Exit")
 

class Cart:
    """
    Represents a shopping cart, which is capable of adding and removing articles, 
    displaying its contents, and checking out.
    """
    def __init__(self):
        self.list_of_purchased = []

    def addProduct(self, article_name, quantity):
        if article_name in INVENTORY:
            article = INVENTORY[article_name]
            if quantity <= article.get_Quantity():
                # Check if article is already in the cart
                for purchased in self.list_of_purchased:
                    if purchased.get_Name() == article_name:
                        purchased.set_Quantity(purchased.get_Quantity() + quantity)
                        article.set_Quantity(article.get_Quantity() - quantity)
                        return
                # If not in the cart, add new entry
                self.list_of_purchased.append(Article(article_name, article.get_Price(), quantity))
                article.set_Quantity(article.get_Quantity() - quantity)
            else:
                print(f"Not enough inventory for {article_name}.")
        else:
            print(f"Article {article_name} not found in inventory.")

    def removeProduct(self, article_name, quantity):
        for purchased in self.list_of_purchased:
            if purchased.get_Name() == article_name:
                if quantity < purchased.get_Quantity():
                    purchased.set_Quantity(purchased.get_Quantity() - quantity)
                    INVENTORY[article_name].set_Quantity(INVENTORY[article_name].get_Quantity() + quantity)
                elif quantity >= purchased.get_Quantity():
                    self.list_of_purchased.remove(purchased)
                    INVENTORY[article_name].set_Quantity(INVENTORY[article_name].get_Quantity() + purchased.get_Quantity())
                return
        print(f"Article {article_name}  is not found in your cart.")

    def displayCart(self):
        if not self.list_of_purchased:
            print("Sorry but your shopping cart is empty")
        else:
            for article in self.list_of_purchased:
                print(article)

    def checkout(self):
        total = sum(item.get_Price() * item.get_Quantity() * (0.9 if item.get_Quantity() >= 3 else 1) for item in self.list_of_purchased)
        total *= 1.07  # Applying 7% VAT
        print(f"Your bill is ${total:.2f}")

def main():
    """
    The main function to run the shopping cart program.
    """
    filename = input("Enter the file path")
    read_data(filename)  # Replace with the correct path to the CSV file
    cart = Cart()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            for article in INVENTORY.values():
                print(article)
        elif choice == "2":
            cart.displayCart()
        elif choice == "3":
            article_name = input("write the name of an item from our catalogue to the shopping cart: ")
            quantity = int(input(f"Add the quantity of {article_name}: "))
            cart.addProduct(article_name, quantity)
        elif choice == "4":
            article_name = input("Give the name of the item you want to remove from the shopping cart: ")
            quantity = int(input(f"Removing the quantity of {article_name} from the shopping cart: "))
            cart.removeProduct(article_name, quantity)
        elif choice == "5":
            cart.checkout()
        elif choice == "6":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")
        continue_prompt = input("Do you want to continue? press y if you want to and any other key if not: ").lower()
        if continue_prompt != 'y':
            print("Thank you for using our service")
            break
            


main()
