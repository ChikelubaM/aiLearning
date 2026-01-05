# 1. Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# i. Write a program that asks user to enter a city name, and it should tell which country the city belongs to
city=input("enter a city name:")
if city in india:
    print(f"{city} is India")
elif city in pakistan:
    print(f"{city} is in Pakistan")
elif city in bangladesh:
    print(f"{city} is in Bangladesh")
else:
    print(f"I wont be able to tell you which country {city} is in. Sorry!")

# ii. Write a program that asks user to enter two cities, and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India"but if I enter mumbai and dhaka it should print "They don't belong to same country"
city_one=input("enter a city name:")
city_two=input("enter a second city name:")
if city_one in india and city_two in india:
    print(f"Both {city_one} and {city_two} are in India")
elif city_one in pakistan and city_two in pakistan:
    print(f"Both {city_one} and {city_two} are in Pakistan")
elif city_one in bangladesh and city_two in bangladesh:
    print(f"Both {city_one} and {city_two} are in Bangladesh")
else:
    print(f"{city_one} and {city_two} don't belong to same country")

# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# i. Ask user to enter his fasting sugar level
# ii. If it is below 80 to 100 range then print that sugar is low
# iii. If it is above 100 then print that it is high otherwise print that it is normal
sugar_level=input("enter your fasting sugar level:")
sugar_level=float(sugar_level)
if sugar_level < 80:
    print("Your sugar level is low")
elif sugar_level > 100:
    print("Your sugar level is high")
else:
    print("Your sugar level is normal")