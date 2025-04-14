# File to store the list of authorized vehicles
ALLOWED_VEHICLES_FILE = "allowed_vehicles.txt"

# Function to load the authorized vehicles from the file
def load_allowed_vehicles():
    try:
        with open(ALLOWED_VEHICLES_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Function to save the authorized vehicles to the file
def save_allowed_vehicles(vehicles):
    with open(ALLOWED_VEHICLES_FILE, "w") as file:
        for vehicle in vehicles:
            file.write(vehicle + "\n")

# Load the authorized vehicles into memory
AllowedVehiclesList = load_allowed_vehicles()

# Function to display the menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v1.0")
    print("********************************")
    print("Please enter the number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for a Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("20250414_NguyenViet_Project1.0")

# Function to handle printing all authorized vehicles
def handle_print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    print("\n")

# Function to handle searching for a vehicle
def handle_search_vehicle():
    vehicle_name = input("Enter the name of the vehicle to SEARCH: ")
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is an authorized vehicle.")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try")
    print("\n")

# Function to handle adding a vehicle
def handle_add_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to ADD: ")
    if vehicle_name in AllowedVehiclesList:
        print(f"{vehicle_name} is already in the authorized list.")
    else:
        AllowedVehiclesList.append(vehicle_name)
        save_allowed_vehicles(AllowedVehiclesList)
        print(f"You have added '{vehicle_name}' as an authorized vehicle.")
    print("\n")

# Function to handle removing a vehicle
def handle_remove_vehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if vehicle_name in AllowedVehiclesList:
        confirmation = input(f"Are you sure you want to remove '{vehicle_name}' from the authorized list? (yes/no): ").strip().lower()
        if confirmation == "yes":
            AllowedVehiclesList.remove(vehicle_name)
            save_allowed_vehicles(AllowedVehiclesList)
            print(f"You have removed '{vehicle_name}' as an authorized vehicle.")
        else:
            print(f"'{vehicle_name}' was not removed from the authorized list.")
    else:
        print(f"{vehicle_name} is not in the authorized list, so it cannot be removed.")
    print("\n")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            handle_print_vehicles()
        elif choice == "2":
            handle_search_vehicle()
        elif choice == "3":
            handle_add_vehicle()
        elif choice == "4":
            handle_remove_vehicle()
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, 4, or 5.")

# Run the program
main()
print("20250414_NguyenViet_Project1.0")