import datetime

# --- Fixed Data ---
PARKING_RATES = ('hourly_rate', 10), ('daily_rate', 80)
ALLOWED_VEHICLE_TYPES = set(['car', 'bike', 'van'])
PASSWORD = "admin123"

# --- Data Storage ---
parked_vehicles = []
total_revenue = 0

# --- Helper Functions ---
def input_vehicle_type():
    vt = input("Enter vehicle type (car/bike/van): ").lower()
    if vt not in ALLOWED_VEHICLE_TYPES:
        print(f"Invalid vehicle type. Allowed: {ALLOWED_VEHICLE_TYPES}")
        return None
    return vt

def find_vehicle(license_plate):
    for v in parked_vehicles:
        if v["license"] == license_plate:
            return v
    return None

def calculate_fee(time_in, time_out):
    hours = (time_out - time_in).total_seconds() // 3600 + 1
    # daily rate if parked for more than 8 hours
    if hours > 8:
        fee = dict(PARKING_RATES)['daily_rate']
    else:
        fee = int(hours) * dict(PARKING_RATES)['hourly_rate']
    return fee

# --- CRUD Operations ---
def check_in():
    license_plate = input("Enter license plate: ").upper()
    if find_vehicle(license_plate):
        print("Vehicle is already parked.")
        return
    v_type = input_vehicle_type()
    if not v_type:
        return
    time_in = datetime.datetime.now()
    parked_vehicles.append({'license': license_plate, 'type': v_type, 'time_in': time_in, 'fee_paid': None})
    print(f"Vehicle {license_plate} checked in at {time_in.strftime('%Y-%m-%d %H:%M:%S')}")

def check_out():
    global total_revenue
    license_plate = input("Enter license plate to check out: ").upper()
    vehicle = find_vehicle(license_plate)
    if not vehicle:
        print("Vehicle not found.")
        return
    time_out = datetime.datetime.now()
    fee = calculate_fee(vehicle['time_in'], time_out)
    vehicle['fee_paid'] = fee
    parked_vehicles.remove(vehicle)
    total_revenue += fee
    print(f"Vehicle {license_plate} checked out at {time_out.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total parking fee to be paid: {fee}")

def modify_vehicle():
    license_plate = input("Enter license plate to modify: ").upper()
    vehicle = find_vehicle(license_plate)
    if not vehicle:
        print("Vehicle not found.")
        return
    print(f"Current details: {vehicle}")
    field = input("What do you want to modify? (type): ").lower()
    if field == "type":
        new_type = input_vehicle_type()
        if new_type:
            vehicle['type'] = new_type
            print("Vehicle type updated.")

def search_vehicle():
    query = input("Search by license plate or vehicle type: ").lower()
    results = []
    for v in parked_vehicles:
        if query in v['license'].lower() or query == v['type'].lower():
            results.append(v)
    if results:
        for v in results:
            print(v)
    else:
        print("No matching vehicles found.")

def view_reports():
    print("Occupancy Report:")
    type_counts = {t: 0 for t in ALLOWED_VEHICLE_TYPES}
    for v in parked_vehicles:
        type_counts[v['type']] += 1
    for v_type, count in type_counts.items():
        print(f"{v_type.capitalize()}: {count}")
    print(f"Total revenue so far: {total_revenue}")

# --- Main Logic ---
def main():
    attempts = 3
    while attempts > 0:
        pwd = input("Enter password: ")
        if pwd == PASSWORD:
            break
        else:
            attempts -= 1
            print(f"Wrong password! {attempts} attempts left.")
    else:
        print("Login failed. Exiting.")
        return

    while True:
        print("\nMenu:\n1. Check-in Vehicle\n2. Check-out Vehicle\n3. Modify Vehicle Details\n4. Search for a Vehicle\n5. View Reports\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_in()
        elif choice == "2":
            check_out()
        elif choice == "3":
            modify_vehicle()
        elif choice == "4":
            search_vehicle()
        elif choice == "5":
            view_reports()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
