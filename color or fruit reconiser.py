def fruit_reconiser() :
  while True :
   fruits = ['banana','strawberrie','grape','apple','watermelon','orange','blueberrie','lemon']
   fruit_choice = input("enter a fruit name : ")
   if fruit_choice in fruits :
    print("* certfied fruit✅")
    break
   elif fruit_choice not in fruits :
    print("* uncertified fruit❌")
    break
def color_reconiser() :
 while True :
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'black', 'white']
  color_choice = input("enter a color name : ")
  if color_choice in colors :
    print("* certfied color✅")
    break
  elif color_choice not in colors :
    print("* uncertified color❌")
    break
while True :
    a=input("color or fruit ? : ")
    if a=="color" : 
      color_reconiser()
    elif a=="fruit" : 
      fruit_reconiser()
    else : 
      print("""Invalid choice
Please enter 'color' or 'fruit'.""")
      a=0
