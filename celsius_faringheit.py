class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    def get_celsius(self):
        return self.__celsius



temp = Temperature(25)
fahrenheit = temp.to_fahrenheit()
celsius = temp.get_celsius()

print(f"Temperature in Fahrenheit: {fahrenheit}")
print(f"Temperature in Celsius: {celsius}")
