def checkInput(input):
    #Decision Stricture
    if (not response.isnumeric()):
        return f'{input} is not a number. Please try again.'
    
    if (int(response) > 10 or int(response) < 1):
        return f'{response} is out of bounds. Please try again.'
    
    return f'The number is {response}'

#INPUT to response variable
response = input("Please enter a number between 1 and 10: ")

while (response != "" or response != exit):
    print(checkInput(response))
    response = input("Please enter a number between 1 and 10: ")

#EXECUTE checkInput function and OUTPUT response
print(checkInput(response))

#jump statements - break; continue; goto