Usernameinput = input("Username : ")
Passwordinput = input("Password : ")
if Usernameinput == "park" and Passwordinput == "1234" :
    print("-----Welcome-----")
    print("---MENU---")
    print("1.Wine = 500THB")
    print("2.Milk = 150THB")
    print("3.Water = 5THB")
    print("4.Beer = 200 THB")
    OrderDetails = input("รายการสั่งซื้อ : ")
    Quantity = int(input("จำนวน = "))
    if OrderDetails == "1":
        print("Wine จำนวน",Quantity,"ขวด =",500*Quantity,"THB")
    if OrderDetails == "2":
        print("Milk จำนวน",Quantity,"ขวด =",150*Quantity,"THB")
    if OrderDetails == "3":
        print("Water จำนวน",Quantity,"ขวด =",5*Quantity,"THB")
    if OrderDetails == "4":
        print("Beer จำนวน",Quantity,"ขวด =",5200*Quantity,"THB")
    else:
        print("THE ORDER CAN'T BE FOUND")
print("----THANK YOU----")