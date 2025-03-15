def checkInput(input, input_type):
    if input_type == "employeeName" and not input.isalpha() and input.isspace():
        return f'{input} is not a name. Please try again.'
    
def checkInput(input, input_type):
    if input_type == "shiftsWorked" and not input.isnumeric():
        return f'{input} is not a number. Please try again.'

    if input_type == "transactionsMade" and not input.isnumeric():
        return f'{input} is not a number. Please try again.'

    if input_type == "dollarValue" and not input.isnumeric():
        return f'{input} is not a number. Please try again.'
1
def calculate_bonus(dollarValue, transactionsMade, shiftsWorked):
    # Calculate the productivity score
    productivity_score = (dollarValue / transactionsMade) / shiftsWorked
    
    # Determine bonus based on the productivity score
    if productivity_score <= 30:
        return 50.00
    elif 31 <= productivity_score <= 69:
        return 75.00
    elif 70 <= productivity_score <= 199:
        return 100.00
    else:  # productivity_score >= 200
        return 200.00

def main():
    # Calculate the bonus
    bonus = calculate_bonus(dollarValue, transactionsMade, shiftsWorked)
    
    # Display the result
    print(f'Employee Name: {employeeName}')
    print(f"Employee Bonus: ${bonus:.2f}")


while True:
    employeeName = input("What is the name of the employee? ")
    message = checkInput(employeeName, "employeeName")
    if message:
        print(message)
        continue
    break

while True:
    shiftsWorked = input("How many shifts did the employee work? ")
    message = checkInput(shiftsWorked, "shiftsWorked")
    if message:
        print(message)
        continue   

    shiftsWorked = int(shiftsWorked)
    break

while True:
    transactionsMade = input("How many transactions did the employee make? ")
    message = checkInput(transactionsMade, "transactionsMade")
    if message:
        print(message)
        continue

    transactionsMade = int(transactionsMade)
    break

while True:
    dollarValue = input("What was the dollar value of the transactions? ")
    message = checkInput(dollarValue, "dollarValue")
    if message:
        print(message)
        continue

    dollarValue = int(dollarValue)
    break


# Run the program
if __name__ == "__main__":
    main()
print ("20250315_NguyenViet_4-2")