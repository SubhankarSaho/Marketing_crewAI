import pandas as pd
import json

# Given JSON data
products_json = '''
[
    "Fresh Lettuce",
    "Diapers",
    "Irish whiskey",
    "Laundry detergent",
    "Chips",
    "Spaghetti cans (ready to eat)",
    "Minecraft Video Game",
    "Mascara",
    "Toilet Paper (best value)",
    "Wagyu beef steak",
    "Organic avocados",
    "Cigarettes"
]
'''

# Load JSON data
products = json.loads(products_json)

# Create a DataFrame
df = pd.DataFrame(products, columns=['Product'])

# Save to Excel file
excel_file_path = 'products_data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Data successfully saved to {excel_file_path}")
