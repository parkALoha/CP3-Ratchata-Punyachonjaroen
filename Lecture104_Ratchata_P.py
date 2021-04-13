class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8

customer2 = Customer()
customer2.name = "Moo"
customer2.lastName = "Dang"
customer2.age = 19

customer3 = Customer()
customer3.name = "Kao"
customer3.lastName = "Suay"
customer3.age = 33

customer4 = Customer()
customer4.name = "Ton"
customer4.lastName = "Maii"
customer4.age = 45

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()