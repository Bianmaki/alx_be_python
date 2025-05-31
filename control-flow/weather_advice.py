weather_input = (input("what's the weather like today? (sunny/rainy/cold): "))

if weather_input == 'sunny':
    print("wear a t-shirt and sunglasses.")
elif weather_input == 'rainy':
    print("don't forget your umbrella and a raincoat.")
elif weather_input == 'cold':
    print("make sure to wear a warm coat and a scarf.")
else:
    print("sorry, I don't have recommendations for this weather.")
