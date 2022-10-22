bill=0
while(True):
    print(""" *** MENU ***
          1.coffee
          2.tea
          3.maggiee
          4.samosa""")
    op=int(input("enter your option: "))
    if op==1:
            print("selected coffee")
            q=int(input("enter the quantity: "))
            bill=bill+(q*100)
    elif op==2:
              print("selected tea")
              q=int(input("enter the quantity: "))
              bill=bill+(q*10)
    elif op==3:
            print("selected maggiee")
            q=int(input("enter the quantity: "))
            bill=bill+(q*50)
    elif op==4:
            print("selected samosa")
            q=int(input("enter the quantity: "))
            bill=bill+(q*20)
    else:
            print("total price: ",bill)
            break