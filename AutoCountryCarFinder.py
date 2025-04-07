# List of authorized vehicles
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

# Function to display the menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please enter the number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")
    print("20250407_NguyenViet_Project0-1")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in AllowedVehiclesList:
                print(vehicle)
            print("\n")
        elif choice == "2":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

# Run the program
main()
print("20250407_NguyenViet_Project0-1")