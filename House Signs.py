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
    validation_message = checkInput(numChar, "numChar")
    if validation_message:
        print(validation_message)
        continue
    
    numChar = int(numChar)
    break

while True:
    woodType = input("What type of wood would you like? ")
    validation_message = checkInput(woodType, "woodType")
    if validation_message:
        print(validation_message)
        continue
    break

while True:
    color = input("What color would you like? ")
    validation_message = checkInput(color, "color")
    if validation_message:
        print(validation_message)
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