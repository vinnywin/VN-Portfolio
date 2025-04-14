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
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please enter the number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for a Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("20250414_NguyenViet_Project0-5")

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
        save_allowed_vehicles(AllowedVehiclesList)
        print(f"You have added '{vehicle_name}' as an authorized vehicle.")

# Function to remove a vehicle from the authorized list
def remove_vehicle(vehicle_name):
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
            vehicle_name = input("Enter the name of the vehicle to SEARCH: ")
            search_vehicle(vehicle_name)
            print("\n")
        elif choice == "3":
            vehicle_name = input("Please Enter the full Vehicle name you would like to ADD: ")
            add_vehicle(vehicle_name)
            print("\n")
        elif choice == "4":
            vehicle_name = input("Please Enter the full Vehicle name you would like to REMOVE: ")
            remove_vehicle(vehicle_name)
            print("\n")
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, 4, or 5.")

# Run the program
main()
print("20250414_NguyenViet_Project0-5")