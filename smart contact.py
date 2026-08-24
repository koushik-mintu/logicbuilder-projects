users = []

while True:
    
  print("=======WELCOME TO SMART MANGER==========")

  print("1.ADD USER :")
  print("2.SEARCH USER :")
  print("3.UPDATE USER :")
  print("4.DELETE USER :")
  print("5.FILTERS USERS :")
  print("6.DISPLAY USERS :")
  print("7.EXIT")

  choice = input("Enter your task: ")

  if choice == "1":
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    skills = input("Enter skills: ")

    user = {
    "name":name,
    "age":age,
    "skills":skills

    }
    users.append(user)
    print("User added successfully!")

  elif choice == "2":
   print("======= wlecome to search =======  ")  

   search_name = input("Enter name to search: ")

   for user in users: 
    if user["name"] == search_name:
     print( user) 
    else:
      print("not found detail !") 

  elif choice == "3":
    print("=====Update user=========")

    search_name = input("Enter name to update : ")   
    for user in users:
     if user["name"] == search_name:
      new_name = input("Enter new name: ")
      new_age = input("Enter new age:")
      new_skill = input("Enter new skills: ")

    user["name"] = new_name
    user["age"] = new_age
    user["skills"] = new_skill

    print(" user update Successfully !")

    for user in users:
      print("Name:",user["name"])
      print("Age:",user["age"])
      print("Skills:",user["skills"])

  elif choice == "4":

    print("=========Delete users======")
    delete_user = input("Enter your user to delete : ")
    
    for user in users:
      if user["name"] == delete_user :
        users.remove(user)
        print("User deleted successfully!")
        break
    
   
  elif choice == "6":

    print("======Display users =======")

    if not users :
      print("no users found")

    for user in users :
      print("Name:",user["name"])
      print("Age:",user["age"])
      print("Skill:",user["skills"])
      break






















  elif choice =="7":
  
    print("Goodbye!")
    break 

