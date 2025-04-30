# This Python program is a simple medical record manager.
# It allows a user to input patient details (name, weight, height, and temperature) via the command line.
# The data is stored in an Excel file (`patient_details.xlsx`).
# If the patient already exists (case-insensitive name check), their data is updated.
# If not, the program adds the new patient data to the file.
# The program uses `pandas` for data manipulation, `openpyxl` as the Excel engine, 
# and `datetime` for time-stamping each record.

# Import pandas for data handling and Excel operations
import pandas as pd

# Import datetime to record the date and time of entry
from datetime import datetime

# Import os to check if the file already exists
import os

# Define a function that updates existing patient data or adds a new patient
def update_or_add_patient(file_name, name, weight, height, temperature):
    # Create a new entry as a dictionary with the provided details and a timestamp
    new_entry = {
        'Name': name,
        'Weight (kg)': weight,
        'Height (cm)': height,
        'Temperature (°C)': temperature,
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Check if the Excel file already exists
    if os.path.exists(file_name):
        # Load the Excel file using pandas and openpyxl engine
        df = pd.read_excel(file_name, engine='openpyxl')

        # Find index(es) of patient(s) matching the input name, case-insensitive
        existing_index = df[df['Name'].str.lower() == name.lower()].index

        # If a match is found, update that patient's information
        if not existing_index.empty:
            df.loc[existing_index[0], ['Weight (kg)', 'Height (cm)', 'Temperature (°C)', 'Date']] = \
                [weight, height, temperature, new_entry['Date']]
            print(f"Updated data for patient: {name}")
        else:
            # If the patient doesn't exist, append the new entry to the DataFrame
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            print(f"Added new patient: {name}")
    else:
        # If the file doesn't exist, create a new DataFrame with the patient entry
        df = pd.DataFrame([new_entry])
        print(f"Created new file and added patient: {name}")

    # Save the DataFrame to the Excel file
    df.to_excel(file_name, index=False)

    # Print the updated DataFrame for visual confirmation
    print("\nUpdated Patient Records:")
    print(df)

# === MAIN LOGIC ===

# Set the name of the Excel file to store patient data
file_name = 'patient_details.xlsx'

# Show current working directory for reference (optional)
print("Current working directory:", os.getcwd())

# Take patient details from the user at runtime
name = input("Enter patient's name: ")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))
temperature = float(input("Enter body temperature (°C): "))

# Call the function with user input to update or add the patient
update_or_add_patient(file_name, name, weight, height, temperature)
