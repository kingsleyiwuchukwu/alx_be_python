# Utilize conditional statements to guide program execution based on user input regarding weather conditions.

# Prompt the user for input the current weather
weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

# Conditional Statement to Clothing Recommendations base on user response.

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

