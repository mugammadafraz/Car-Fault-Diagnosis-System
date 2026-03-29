# Car Fault Diagnosis Expert System

print("Welcome to Car Fault Diagnosis Expert System")

car_not_starting = input("Is the car not starting? (yes/no): ")
battery_dead = input("Is the battery dead? (yes/no): ")
engine_overheating = input("Is the engine overheating? (yes/no): ")
coolant_low = input("Is the coolant level low? (yes/no): ")
fuel_low = input("Is the fuel level low? (yes/no): ")

# Rule 1
if car_not_starting == "yes" and battery_dead == "yes":
    print("Possible Fault: Battery Problem")

# Rule 2
elif car_not_starting == "yes" and fuel_low == "yes":
    print("Possible Fault: Fuel System Problem")

# Rule 3
elif engine_overheating == "yes" and coolant_low == "yes":
    print("Possible Fault: Cooling System Issue")

# Rule 4
elif engine_overheating == "yes":
    print("Possible Fault: Engine Temperature Problem")

# Rule 5
elif car_not_starting == "yes":
    print("Possible Fault: Starter Motor Issue")

else:
    print("No major fault detected. Please check the vehicle manually.")