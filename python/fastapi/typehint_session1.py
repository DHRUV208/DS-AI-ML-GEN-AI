# str1 = 'Ram'
# print(type(str))

a = 10
print(type(a))

a = '10'
print(type(a))
print("-"*20)

text: str = "Ram"

text1: str = "100"

print("typeof text: ", type(text))
print("typeof text1: ",type(text1))

text2: str = 1200

print("typeof text2: ", type(text2))

print("-"*20)

def fun(param):
    param.reverse()
    return param

print(fun(['1', '2']))

def fun1(param: list[str]) -> list[str]:
    param.reverse()
    return param

print(fun1(['1', '2']))

def full_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()

print(full_name('dhruv', 'mehta'))

def full_name1(first_name:str, last_name:str) -> str:
    return first_name.title() + " " + last_name.title()


print("-"*20)

"""
Types in type hint
1. int
2. str
3. bool
4. bytes
5. float

"""
def get_items(item_a: str, item_b: int, item_c: bool, item_d: bytes, item_e: float):
    return item_a, item_b, item_c, item_d, item_e


print(get_items('Ram', 100, True, b"a", 10.2))

print("-="*20)

from typing import Any
def random_fun(data: Any):
    return data

print(random_fun("Ram"))
print(random_fun(100))

print("-"*20)

"""
1. list[str]
2. tuple[int, int, int]
3. set[bytes]
4. dict[str, str]

"""

def process_list(items: list[str]) -> None:
    for item in items:
        print(item)


process_list(['1', '2', '3', '4'])


def process_tuple_set(item_t: tuple[int, int, str], item_s: set[bytes]):
    return item_t, item_s


print(process_tuple_set((1, 2, '3'), {b"1", b"2", b"3"}))

print("-="*20)

def process_dict(prices: dict[str, int]):
    for item_name, item_price in prices.items():
        print(item_name, " -> ", item_price)
    

process_dict({"chair": 100, "table": 250})

print("-"*20)

"""
Union
declare variables accepting multiple types using '|' separator
"""

def process_id(item: str | int):
    print("ID: ", item, "of type: ", type(item))



(process_id(100))
process_id("str") 

def hi(name: str | None = None):
    if name is not None:
        print("Hello", name)
    else:
        print("no name provided")
    

hi("Ram")
hi()

from collections.abc import Iterable

def reverse_array(items: Iterable[str]) -> list[str]:
    return list(items)[::-1]

print(reverse_array(["1", "2", "3"]))

# Literal in TypeHint

from typing import Literal
def set_access(name: str, role: Literal["admin", "editor", "viewer"]) -> str:
    return f"{name} has a {role} permission"


print(set_access("Ram", "admin"))
print(set_access("Sham", "viewer"))
print(set_access("Kiran", "xyz"))

#  enum in typehint

from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

def assign_role(user: str, role: Role) -> str:
    return f"{user} has a role name = {role.name}, role value = {role.value}"


print(assign_role("ram", Role.ADMIN ))
