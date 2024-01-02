# This code converts units of measurement

def fahrenheit_to_celsius(n):
    return (n-32)/1.8

def celsius_to_fahrenheit(n):
    return (n*1.8)+32

def miles_to_km(n):
    return n*1.609

def km_to_miles(n):
    return n/1.609

def get_input():
    number = float(input("Insert the number you want convert. "))
    conversion = int(input("Introduce a number:\n1 for °F to °C\n2 for °C to °F\n3 for mi to km\n4 for km to mi.\n"))
    return number, conversion

def main():
    number, conversion = get_input()
    if conversion == 1:
        print(fahrenheit_to_celsius(number), "°C")
    if conversion == 2:
        print(celsius_to_fahrenheit(number), "°F")
    if conversion == 3:
        print(miles_to_km(number), "km")
    if conversion == 4:
        print(km_to_miles(number), "miles") 

if __name__ == "__main__":
    main()