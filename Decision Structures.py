def checkInput(input):
     #Decision Structures
    if (not response.isnumeric()):
        return f'{input} is not a number. Please try again.'

    if (int(response) > 10 or int(response) < 1):
        return f'{response} is out of bounds. Please try again.'

    return f'The number is {response}'



# User Input
response = input("Please enter a number between 1 and 10: ")
print(checkInput(response))
