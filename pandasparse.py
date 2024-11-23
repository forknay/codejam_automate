import pandas as pd
import itertools
import random
# Load the data
all_data = pd.read_csv('vehicles.csv')

# Define the list of characteristics
characteristics = [
    'Type', 'Year', 'Make', 'Model', 'Body', 'ModelNumber', 'Doors', 'ExteriorColor', 
    'InteriorColor', 'EngineCylinders', 'EngineDisplacement', 'Transmission', 'Miles', 'SellingPrice', 
    'BookValue', 'Certified', 'Options', 'Style_Description', 'Ext_Color_Generic', 'Int_Color_Generic', 'Int_Upholstery', 'Engine_Block_Type', 
    'Engine_Aspiration_Type', 'Engine_Description', 'Transmission_Speed', 'Transmission_Description', 
    'Drivetrain', 'Fuel_Type', 'CityMPG', 'HighwayMPG', 'EPAClassification', 
    'Internet_Price', 'MarketClass', 'PassengerCapacity'
]

# Collect all rows in a list
rows = []
print('loading....')
# Iterate over each row in the data
size = 100000
while len(rows) < size:
    for index, row in all_data.iterrows():
        p1, p2, p3 = random.sample(characteristics, 3)
        #print(p1,p2,p3)
        stock = row['Stock']
        name = row['Model']
        if pd.notna(row.loc[p1]) and pd.notna(row.loc[p2]) and pd.notna(row.loc[p3]):
            temp_dict = {"messages":[{"role":"System","content":"You are a large language model trained by Cohere."},
                                 {"role":"User","content":f"Hi!, I am looking for a car with {p1} {row.loc[p1]}, {p2} {row.loc[p2]} and {p3} {row.loc[p3]}"},
                                 {"role":"Chatbot","content":f"I would recommend the {name} ({stock})"},
                                 {"role":"User","content":"Thank you!"}]}
                
            rows.append(temp_dict)

# Create the DataFrame once at the end
prompts = pd.DataFrame(rows)

# Print the resulting DataFrame
print(len(prompts))
print(prompts.tail()[['messages']])
print(prompts.dtypes)

prompts.to_json('prompts.json', orient='records', lines=True)