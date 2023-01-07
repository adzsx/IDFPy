from faker import Faker
from random import choice, randint, randrange
import sys
import json
import datetime


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
-o PATH         Open Json data in stored PATH
"""

def all():
  gender = choice(["m", "f"])
  age = randint(18, 70)
  setName = faker.name_male() if gender == "m" else faker.name_female()
  address = faker.address()
  email = setName.split(" ")[0] + "." + setName.split(" ")[1] + "@" + choice(["gmail", "gmx", "proton", "aol", "outlook", "protonmail"]) + choice([".com", ".de", ".fr", ".uk", ".ru", ".us"])

  return {"name": setName, "gender": gender, "age": str(age), "mail": email}

person = all()

if not "-o" in args:
  print(json.dumps(person, indent=4))
else:
  path = args[args.index("-o")+1]
  with open(path, "r") as f:
    data = json.load(f)
    print(json.dumps(data, indent=4))



if "-s" in args:
  path = args[args.index("-s")+1]
  with open(path, "w") as f:
    json.dump(person, f)