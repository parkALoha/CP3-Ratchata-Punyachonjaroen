MenuList =[]
Price =[]
def ShowBill():
    print("----My Food----")
    for i in range(len(MenuList)):
        print(MenuList[i],Price[i])

def TotalPrice():
    Total = 0
    for b in Price:
        Total += (b)
    print("Total Price :",Total, "THB")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName == "exit"):
        break
    else:
        MenuPrice = int(input("Price : "))
        MenuList.append(menuName)
        Price.append(MenuPrice)
print(MenuList)
print(Price)
ShowBill()
TotalPrice()