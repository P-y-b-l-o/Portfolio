# This code converts units of measurement

# Convert from Fahrenheit to Celsius
def fahrenheit_to_celsius(n):
    return (n-32)/1.8

# Convert from Celsius to Fahrenheit
def celsius_to_fahrenheit(n):
    return (n*1.8)+32

# Convert from miles to kilometers
def miles_to_km(n):
    return n*1.609

# Convert from kilometers to miles
def km_to_miles(n):
    return n/1.609

# Get user input for number and conversion
def get_input():
    number = float(input("Insert the number you want convert: "))
    conversion = int(input("Introduce a number:\n1 for °F to °C\n2 for °C to °F\n3 for mi to km\n4 for km to mi\n"))
    return number, conversion

# Process the user inputs and print the answer
def main():
    while True:
        number, conversion = get_input()
        if conversion == 1:
            print(round(fahrenheit_to_celsius(number), 2), "°C")
        if conversion == 2:
            print(round(celsius_to_fahrenheit(number), 2), "°F")
        if conversion == 3:
            print(round(miles_to_km(number), 2), "km")
        if conversion == 4:
            print(round(km_to_miles(number), 2), "miles")
        print()
        print("Do you want to make another conversion? (yes/no)")
        answer = input().lower()
        if answer != 'yes':
            break

if __name__ == "__main__":
    main()