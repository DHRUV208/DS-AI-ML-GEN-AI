# #  before pydantic

# class Student:
#     def __init__(self, name: str, age: int, gpa: float):
#         self.name=name
#         self.age=age
#         self.gpa=gpa
    


# # s = Student(name=99, age="Twenty", gpa=True)
# # print(s.name, s.age, s.gpa)

# # adter pydantic

from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    age: int
    gpa: float

# s1 = Student(name="Ram", age=21, gpa=2.98)
# print(s1)

# s2 = Student(name=99, age="Twenty", gpa="False")

# raw_data={
#     "name": "sham",
#     "age": 20,
#     "gpa": 3.58
# }

# s2 = Student(**raw_data)
# print(s2)

raw_data1 = {
    "name": "Sham",
    "age": "21",
    "gpa": "21.5"
}

s3 = Student(**raw_data1)
print(s3)
print(type(s3.name), type(s3.age), type(s3.gpa))

raw_data4 = {
    "name": 1234,
    "age": "Twenty"
}

# s4 = Student(**raw_data4)

try:
    s5 = Student(**raw_data4)
except ValidationError as e:
    print(f"Total validation errors: {e.error_count()}")
    for error in e.errors():
        print(f"Fields: {error['loc']}, Type: {error['type']}, Message: {error['msg']}")



from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    in_stock: bool

raw_data6 ={
    "product_id":"5",
    "name":"Laptop",
    "price":"19",
    "in_stock":"1"
}
p1 = Product(**raw_data6)

# print(p1)

print("Product ID:", p1.product_id, type(p1.product_id))
print("Name:", p1.name, type(p1.name))
print("Price:", p1.price, type(p1.price))
print("In Stock:", p1.in_stock, type(p1.in_stock))

incorrect_rawdata = {
    "product_id": "abc",
    "name": "Mobile",
    "price": "hello",
    "in_stock": "yes"
}

try:
    p2 = Product(**incorrect_rawdata)

    print(p2)

except ValidationError as e:
    print(e)
    print("Error count:", e.error_count())
    for error in e.errors():
        print(f"Field: {error['loc']}, Type: {error['type']}, Message: {error['msg']}")



from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str

# Required & non-nullable
# what happens when valuie is not provided in a dict
value = {
    "product_id": "50"
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"error count: {e.error_count()}")
    for error in e.errors():
        print(f"Field: {error['loc']}, Type: {error['type']}, message: {error['msg']} ")



#  Required & Non-nullable
# what happens if value is None


value = {
    "product_id": "50",
    "name": None 
}

try:
    p2 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for error in e.errors():
        print(f"Fields: {error['loc']}, Type: {error['type']}, message: {error['msg']}")


#  Required & Nullable
class Product(BaseModel):
    product_id: int
    name: str | None

value ={
    "product_id": "50"
}

try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for error in e.errors():
        print(f"Fields: {error['loc']}, Type: {error['type']}, message: {error['msg']}")


# required & nullable
# what happens if value is None

value = {
    "product_id": "50",
    "name": None
}

try:
    p3 = Product(**value)
except ValidationError as e:
    print(f"Total Number of error: {e.error_count()}")
    for error in e.errors():
        print(f"Fields: {error['loc']}, Type: {error['type']}, message: {error['msg']}")
    

