import platform
import socket


print("FRIDAY")
print("1.calculator")
print("2.Even / odd checker")
print("3.unit converter")
print("4.simple system information")
print("5.exit")

choice = input("enter your task: ")

while True:
  if choice == "1":
    print("Welcome to calculator ")

    num1 = float(input("enter your 1st number: "))
    num2 = float(input("enter your 2nd number: ") )

    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.exit")

    options = input("enter the task 1.add 2.sub 3.mul 4.divide 5.exit: ")

    if  options == "1":
     add =  num1+num2
     print(add)
    elif options == "2":
     sub = num1-num2
     print(sub)
    elif options == "3":
     mul = num1*num2
     print(mul)
    elif options == "4":
     div = num1/num2
     print(div)
    elif options == "5":
     print("exit")
    break

  elif choice == "2":
   print("Welcome even/ odd checker :")
   num1 = float(input("enter your 1st number: "))
   
   if num1 == num1%2==0:
    print("even")
   else :
    print("odd")
    break

  elif choice == "3":
   print("Welcome to unit converter ")


   print("1. miles to kilometer : ")
   print("2. kilometer to miles : ")
   print("3. celsius to fahernheit : ") 
   print("4. fahernheit to celsius : ")
   print("5. exit the menu :  ")

   menu = (input(" enter your conversion : "))

   if menu == "1":
    mile = float(input("enter your mile : "))
    kilometer = mile * 1.60934
    print(kilometer)

   elif menu == "2":
    kilometer = float (input ("enter your kilometer : "))
    mile = kilometer * 0.621371
    print(mile)

   elif menu == "3":
    celsius = float(input("enter your celsius : "))
    fahernheit = (celsius * 9/5)+32
    print(mile)

   elif menu == "4":
    fahernheit = float(input("enter your  fahernheit : "))
    celsius = (fahernheit - 32)* 5/9
    print(mile)

   elif menu == "5":
    print("exit thanks for using conversion ")
    break
    
  elif choice == "4" :

    print("===========System information========")

    print("1.computer name : ")
    print("2.python version : ")
    print("3.processor : ")
    print("4.operating system : ")

    system_info = input("enter your type of info : ")
  
    if system_info == "1":
      computer_name = socket.gethostname()
      print(computer_name)
     
    elif system_info =="2" : 
      python_version = platform.python_version()
      print(python_version)
    elif system_info == "3" :
     processor = platform.processor()
     print(processor)
     
    elif system_info == "4" :  
     operating_system = platform.system()
     print(operating_system)
     
  elif choice == "5" :
     print("Good bye!")
     break  

  else:
   print("Invalid choice")


   



