def well_wishes():
    print("nice to meet you")
    print("nice to meet you too")

well_wishes()

#function with arguments
def weather_condition(a):
   if a == "summer":
       print("wear cotten and thin clothes")
   elif a == "winter":
       print("wear warm clothes")
   elif a == "spring":
       print("wear wool clothes")
   elif a == "autumn":
       print("wear sweat shirts")
   else:
       print("invalid season")
weather = input("enter season here")
weather_condition(weather)