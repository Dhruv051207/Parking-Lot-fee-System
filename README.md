## 🅿️ Parking Management System

### 📖 Overview

This is a **console-based parking management system** built in Python.
It allows users to:

* Check in vehicles (car, bike, van)
* Check out vehicles and calculate parking fees
* Track total revenue
* Maintain simple data storage in memory

The script demonstrates use of:

* Python’s built-in `datetime` module
* Basic CRUD (Create, Read, Update, Delete) operations
* Data structures like lists, dictionaries, and sets

---

### 🗂️ Project Structure

```
.
├── script1.py          # Main Python script containing all logic
└── README.md           # Project documentation (this file)
```

---

### ⚙️ Main Components

| Section                    | Description                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Fixed Data**             | Contains parking rates (`hourly_rate`, `daily_rate`), allowed vehicle types, and admin password.              |
| **Data Storage**           | Stores active parking records (`parked_vehicles` list) and total revenue.                                     |
| **Helper Functions**       | Utility functions for validating vehicle type, finding parked vehicles, and calculating fees.                 |
| **CRUD Operations**        | Core functions: `check_in()`, `check_out()`, `display_vehicles()`, and `remove_vehicle()` to manage vehicles. |
| **Main Loop (if present)** | Runs the menu-driven program that interacts with the user through the terminal.                               |

---

### 🚗 Features

* ✅ Add (check in) a vehicle with license plate and type
* ⏱️ Automatically records entry time using `datetime.now()`
* 💰 Calculates parking fee based on duration (hourly or daily)
* 🧾 Displays all parked vehicles and total revenue
* 🔐 Simple admin password protection for some actions

---

### 🧠 Example Usage

```bash
$ python3 script1.py
Enter vehicle type (car/bike/van): car
Enter license plate: DL01AB1234
Vehicle checked in successfully!

# Later...
Enter license plate to check out: DL01AB1234
Total fee: ₹40
```

---

### 🧩 Dependencies

* Python ≥ 3.6
  (No external libraries are required.)

---
