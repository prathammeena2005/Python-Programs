temp=int(input("Enter temperature in Celsius: "))
def convert_temp(c):
    a=(c * 9/5) + 32
    return a
print("Temperature in Fahrenheit", convert_temp(temp),"°F")