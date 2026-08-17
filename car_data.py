# Expanded local database - no API calls or keys required
CAR_DATABASE = [
    {"make": "Toyota", "model": "Fortuner", "fuel_type": "diesel", "transmission": "automatic", "drive": "4wd", "cylinders": 4, "min_price": 3200000, "max_price": 5000000},
    {"make": "Toyota", "model": "Camry", "fuel_type": "electricity", "transmission": "automatic", "drive": "fwd", "cylinders": 4, "min_price": 4500000, "max_price": 4600000},
    {"make": "Toyota", "model": "Glanza", "fuel_type": "gas", "transmission": "manual", "drive": "fwd", "cylinders": 4, "min_price": 680000, "max_price": 1000000},
    {"make": "Toyota", "model": "Urban Cruiser Hyryder", "fuel_type": "electricity", "transmission": "automatic", "drive": "fwd", "cylinders": 3, "min_price": 1100000, "max_price": 2000000},
    {"make": "Honda", "model": "City", "fuel_type": "gas", "transmission": "manual", "drive": "fwd", "cylinders": 4, "min_price": 1150000, "max_price": 1600000},
    {"make": "Honda", "model": "City e:HEV", "fuel_type": "electricity", "transmission": "automatic", "drive": "fwd", "cylinders": 4, "min_price": 1800000, "max_price": 2050000},
    {"make": "Honda", "model": "Elevate", "fuel_type": "gas", "transmission": "automatic", "drive": "fwd", "cylinders": 4, "min_price": 1160000, "max_price": 1650000},
    {"make": "Hyundai", "model": "Creta", "fuel_type": "diesel", "transmission": "automatic", "drive": "fwd", "cylinders": 4, "min_price": 1100000, "max_price": 2000000},
    {"make": "Hyundai", "model": "Ioniq 5", "fuel_type": "electricity", "transmission": "automatic", "drive": "rwd", "cylinders": 0, "min_price": 4500000, "max_price": 4800000},
    {"make": "Hyundai", "model": "Verna", "fuel_type": "gas", "transmission": "manual", "drive": "fwd", "cylinders": 4, "min_price": 1100000, "max_price": 1740000},
    {"make": "BMW", "model": "3 Series Gran Limousine", "fuel_type": "gas", "transmission": "automatic", "drive": "rwd", "cylinders": 4, "min_price": 6000000, "max_price": 6200000},
    {"make": "BMW", "model": "i4", "fuel_type": "electricity", "transmission": "automatic", "drive": "rwd", "cylinders": 0, "min_price": 7200000, "max_price": 7800000},
    {"make": "Tata", "model": "Nexon EV", "fuel_type": "electricity", "transmission": "automatic", "drive": "fwd", "cylinders": 0, "min_price": 1450000, "max_price": 1950000},
    {"make": "Tata", "model": "Harrier", "fuel_type": "diesel", "transmission": "manual", "drive": "fwd", "cylinders": 4, "min_price": 1540000, "max_price": 2640000}
]

def fetch_car_makes():
    """Extract unique manufacturers dynamically from dataset."""
    makes = sorted(list(set(car["make"] for car in CAR_DATABASE)))
    return makes

def fetch_car_data(make=None, fuel_type=None):
    """Filter dataset by selected brand and fuel type without needing external APIs."""
    results = CAR_DATABASE
    
    if make:
        results = [c for c in results if c["make"].lower() == make.lower()]
    if fuel_type:
        results = [c for c in results if c["fuel_type"].lower() == fuel_type.lower()]
        
    return results
