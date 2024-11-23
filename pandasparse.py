import pandas as pd
import itertools

# Load the data
all_data = pd.read_csv('vehicles.csv')

# Define the list of characteristics
characteristics = [
    'Type', 'VIN', 'Year', 'Make', 'Model', 'Body', 'ModelNumber', 'Doors', 'ExteriorColor', 
    'InteriorColor', 'EngineCylinders', 'EngineDisplacement', 'Transmission', 'Miles', 'SellingPrice', 
    'MSRP', 'BookValue', 'Invoice', 'Certified', 'Options', 'Style_Description', 'Ext_Color_Generic', 
    'Ext_Color_Code', 'Int_Color_Generic', 'Int_Color_Code', 'Int_Upholstery', 'Engine_Block_Type', 
    'Engine_Aspiration_Type', 'Engine_Description', 'Transmission_Speed', 'Transmission_Description', 
    'Drivetrain', 'Fuel_Type', 'CityMPG', 'HighwayMPG', 'EPAClassification', 'Wheelbase_Code', 
    'Internet_Price', 'MarketClass', 'PassengerCapacity', 'ExtColorHexCode', 'IntColorHexCode', 
    'EngineDisplacementCubicInches'
]

# Collect all rows in a list
rows = []

# Iterate over each row in the data
for index, row in all_data.iterrows():
    stock = row['Stock']
    # Generate all possible pairs of characteristics
    for p1, p2 in itertools.combinations(characteristics, 2):
        if pd.notna(row[p1]) and pd.notna(row[p2]):
            rows.append({'P1': (p1,row[p1]), 'P2': (p2,row[p2]), 'Output': stock})

# Create the DataFrame once at the end
prompts = pd.DataFrame(rows)

# Print the resulting DataFrame
print(len(prompts))
print(prompts.tail())
print(prompts.dtypes)

prompts.to_csv('prompts.csv', index=False)