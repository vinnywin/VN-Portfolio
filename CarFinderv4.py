# List of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to display the menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please enter the number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for a Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Delete Authorized Vehicle")
    print("5. Exit")
    print("20250414_NguyenViet_Project0-2")

# Function to search for a vehicle
def search_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is an authorized vehicle.")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try")

# Function to add a vehicle to the authorized list
def add_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is already in the authorized list.")
    else:
        AllowedVehiclesList.append(vehicle_name)
        print(f"You have added '{vehicle_name}' as an authorized vehicle.")

# Function to remove a vehicle from the authorized list
def remove_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        AllowedVehiclesList.remove(vehicle_name)
        print(f"You have removed '{vehicle_name}' from the authorized list.")
    else:
        print(f"{vehicle_name} is not in the authorized list, so it cannot be removed.")

# Function to check if user is sure they wish to remove vehicle from authorized list
def remove_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
        confirmation = input(f"Are you sure you want to remove '{vehicle_name}' from the authorized list?\n: ").strip().lower()
        if confirmation == "yes":
            AllowedVehiclesList.remove(vehicle_name)
            print(f"You have removed '{vehicle_name}' as an authorized vehicle.")
        else:
            print(f"'{vehicle_name}' was not removed from the authorized list.")
    else:
        print(f"{vehicle_name} is not in the authorized list, so it cannot be removed.")
        
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
            vehicle_name = input("Enter the name of the vehicle to search: ")
            search_vehicle(vehicle_name)
            print("\n")
        elif choice == "3":
            vehicle_name = input("Please Enter the full Vehicle name you would like to add: ")
            add_vehicle(vehicle_name)
            print("\n")
        elif choice == "4":
            vehicle_name = input("Please Enter the full Vehicle name you would like to remove: ")
            remove_vehicle(vehicle_name)
            print("\n")
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, 4, or 5.")

# Run the program
main()
print("20250414_NguyenViet_Project0-2")