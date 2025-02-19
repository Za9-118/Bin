import sys

print("ARE YOU SURE?")
conf=input("[Y]-Yes,[N]-No:")
if conf.lower().startswith("n"):
    sys.exit(0)

print("THIS IS A SYSTEM DIRECTORY!\nARE YOU SURE?")
conf=input("[Y]-Yes,[N]-No:")
if conf.lower().startswith("n"):
    sys.exit(0)

print("ARE YOU THE ADMIN?")
conf=input("[Y]-Yes,[N]-No:")
if conf.lower().startswith("n"):
    sys.exit(0)

while (1):
    print("BIN INSIDE BIN...")