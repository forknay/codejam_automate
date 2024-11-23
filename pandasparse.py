import pandas as pd
import itertools

# Load the data
all_data = pd.read_csv('testdata.csv')

# Define the list of characteristics

characteristics = [
    'Type', 'Stock', 'Year', 'Make', 'Model', 'Body', 'ModelNumber', 'Doors', 'ExteriorColor', 
    'InteriorColor', 'EngineCylinders', 'EngineDisplacement', 'Transmission', 'Miles', 'SellingPrice', 
    'MSRP', 'BookValue', 'Invoice', 'Certified', 'Options', 'Style_Description', 'Ext_Color_Generic', 
    'Ext_Color_Code', 'Int_Color_Generic', 'Int_Color_Code', 'Int_Upholstery', 'Engine_Block_Type', 
    'Engine_Aspiration_Type', 'Engine_Description', 'Transmission_Speed', 'Transmission_Description', 
    'Drivetrain', 'Fuel_Type', 'CityMPG', 'HighwayMPG', 'EPAClassification', 'Wheelbase_Code', 
    'Internet_Price', 'MarketClass', 'PassengerCapacity', 'ExtColorHexCode', 'IntColorHexCode', 
    'EngineDisplacementCubicInches'
]

# Create an empty DataFrame for prompts
prompts = pd.DataFrame(columns=['P1', 'P2', 'Output']).astype({'Output': 'category'})

# Iterate over each row in the data
for index, row in all_data.iterrows():
    vin = row['VIN']
    # Generate all possible pairs of characteristics
    for p1, p2 in itertools.combinations(characteristics, 2):
        prompts = prompts._append({'P1': row[p1], 'P2': row[p2], 'Output': vin}, ignore_index=True)

# Print the resulting DataFrame
print(prompts.tail())

prompts.to_csv('prompts.csv', index=False)