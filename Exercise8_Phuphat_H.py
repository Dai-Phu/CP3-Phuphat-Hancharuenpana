usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "Phuphat" and passwordInput == "Hancha" :
    print("-------------------------")
    print("Accept !")
    print("You are within Shop Store")
    print("-------------------------")
    print("Order in Stop :")
    print("1. Film Camera : 2,000 THB")
    print("2. Digital Camera : 10,000 THB")
    print("3. Vdo Camera : 20,000 THB")
    print("4. Go Camera : 8,000 THB")
    print("5. Compact Camera : 9,000 THB")
    Selected  = int(input(" Number Order :"))
    if Selected == 1  :
        amount = int(input("amount : "))
        total = amount*2000
        print("total :",total,"THB")
    elif  Selected == 2 :
        amount = int(input("amount : "))
        total = amount*10000
        print("total :",total, "THB")
    elif Selected == 3 :
        amount = int(input("total :"))
        total = amount * 20000
        print("total :", total, "THB")
    elif Selected == 4 :
        amount = int(input("total :"))
        total = amount*8000
        print("total :", total, "THB")
    elif Selected == 5 :
        amount = int(input("total :"))
        total = amount*9000
        print("total :", total, "THB")
else :
    print("ERROR")

print("Thank you for your support ^^")

