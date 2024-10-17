def process_weather_data(data):
    if data.get('cod') != 200:
        print(f"Error: {data.get('message')}")
        return None, None

    temp = data['main']['temp']
    condition = data['weather'][0]['description'].capitalize()  # Capitalize the condition
    city_name = data['name']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Display formatted data
    print(f"{city_name}: {temp}°C, {condition}, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")
    return temp, condition
