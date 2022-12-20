from faker import Faker
from random import choice, randint
import sys

args = sys.argv
faker = Faker()

logo = """
 _______________________      
|_   _|  _  \  ___| ___ \     
  | | | | | | |_  | |_/ /   _ 
  | | | | | |  _| |  __/ | | |
 _| |_| |/ /| |   | |  | |_| |
 \___/|___/ \_|   \_|   \__, |
                         __/ |
                        |___/ 
"""

hmes = """
IDFPy - Identity Faker Python

Generated random information about a person such as name, address, phone number, email, and much more


Syntax:
IDFPy [options]

Options:
-s PATH         Person will be stored in JSON data in PAHT
"""


gender = choice(["m", "f"])
age = randint(18, 70)
name = faker.name_male() if gender == "m" else faker.name_female()
address = faker.address()
email = name.split(" ")[0] + "." + name.split(" ")[1] + "@" + choice(["gmail", "gmx", "proton", "aol", "outlook", "protonmail"]) + choice([".com", ".de", ".fr", ".uk", ".ru", ".us"])

print(f"Name: {name}\nGender: {gender}\nAge: {age}\nEmail: {email}\n ")