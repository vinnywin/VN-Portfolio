def checkInput(input, input_type):
    if input_type == "numChar" and not input.isnumeric():
        return f'{input} is not a number. Please try again.'

    if input_type == "woodType" and not input.isalpha():
        return f'{input} is not a wood we offer. Please try again.'

    if input_type == "color" and not input.isalpha():
        return f'{input} is not a color we offer. Please try again.'
def checkInput(input, input_type):
    if input_type == "numChar" and not input.isnumeric():
        return f'{input} is not a number. Please try again.'

    if input_type == "woodType" and not input.isalpha():
        return f'{input} is not a wood we offer. Please try again.'

    if input_type == "color" and not input.isalpha():
        return f'{input} is not a color we offer. Please try again.'

# User Input
while True:
    numChar = input("How many characters would you like on your sign? ")
    message = checkInput(numChar, "numChar")
    if message:
        print(message)
        continue
    
    numChar = int(numChar)
    break

while True:
    woodType = input("What type of wood would you like? ")
    message = checkInput(woodType, "woodType")
    if message:
        print(message)
        continue
    break

while True:
    color = input("What color would you like? ")
    message = checkInput(color, "color")
    if message:
        print(message)
        continue
    break

# Initialize charge
charge = 0.0
charge += 35.00

# Character charges
if numChar > 5:
    charge += (numChar - 5) * 4.00

# Color charges
if color == "gold":
    charge += 15.00

# Wood Charge
if woodType == "oak":
    charge += 20.00

# Output
print("The charge for this sign is $" + str(charge))
print("20250313_NguyenViet_4-1")