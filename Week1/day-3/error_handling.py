#basics error handling
def divide_numbers(a, b):
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only!"
    
# Test
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))

#multiple exception
def save_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Invali Input"
    except Exception as e:
        return f"Unexpected Error: {e}"
    else:
        return f"Result: {result}"
    finally:
        print("Division operation completed")
        
print(save_divide(10, 2))

#custom exception
class InvalidAgeError(Exception):
    pass
class InvalidEmailError(Exception):
    pass
class User:
    def __init__(self, name, age ,email):
        self.name = name
        self.age = self.validate_age(age)
        self.email = self.validate_email(email)
        
    def validate_age(self, age):
        if not isinstance(age, int):
            raise InvalidAgeError("Age must be an integer!")
        if age < 0 or age > 150:
            raise InvalidAgeError("Age must be between 0 and 150")
        return age
    
    def validate_email(self, email):
        if "@" not in email or "." not in email:
            raise InvalidEmailError("Invalid format email")
        return email
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
    
try:
    user1 = User("Budi", 25, "budi@email.com")
    print(user1)

    user2 = User("Ani", -5, "ani@emailcom") 
except InvalidAgeError as e:
    print(f"Error Age: {e}")
except InvalidEmailError as e:
    print(f"Error Email: {e}")

    
    