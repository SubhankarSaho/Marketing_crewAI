import pandas as pd
import json
import openpyxl 

# Given JSON data
customers_json = '''
[
    {"birth_year": 1975, "sex": "F", "marital_status": "married", "yearly_household_income_percentile": 65, "number_of_toddlers": 1, "number_of_teens": 0, "highest_education": "masters", "monthly_spend_on_wine": 30, "monthly_spend_on_vegetables": 65, "monthly_spend_on_toys": 20, "last_month_coupon_use": "high"},
    {"birth_year": 1992, "sex": "M", "marital_status": "single", "yearly_household_income_percentile": 30, "number_of_toddlers": 0, "number_of_teens": 0, "highest_education": "bachelors", "monthly_spend_on_wine": 15, "monthly_spend_on_vegetables": 40, "monthly_spend_on_toys": 0, "last_month_coupon_use": "none"},
    {"birth_year": 1980, "sex": "F", "marital_status": "married", "yearly_household_income_percentile": 80, "number_of_toddlers": 0, "number_of_teens": 2, "highest_education": "bachelors", "monthly_spend_on_wine": 50, "monthly_spend_on_vegetables": 80, "monthly_spend_on_toys": 85, "last_month_coupon_use": "low"},
    {"birth_year": 1968, "sex": "M", "marital_status": "divorced", "yearly_household_income_percentile": 45, "number_of_toddlers": 0, "number_of_teens": 0, "highest_education": "high_school", "monthly_spend_on_wine": 45, "monthly_spend_on_vegetables": 50, "monthly_spend_on_toys": 0, "last_month_coupon_use": "high"},
    {"birth_year": 1990, "sex": "F", "marital_status": "single", "yearly_household_income_percentile": 25, "number_of_toddlers": 0, "number_of_teens": 0, "highest_education": "associates", "monthly_spend_on_wine": 10, "monthly_spend_on_vegetables": 35, "monthly_spend_on_toys": 0, "last_month_coupon_use": "low"},
    {"birth_year": 1985, "sex": "M", "marital_status": "married", "yearly_household_income_percentile": 90, "number_of_toddlers": 2, "number_of_teens": 1, "highest_education": "phd", "monthly_spend_on_wine": 80, "monthly_spend_on_vegetables": 100, "monthly_spend_on_toys": 120, "last_month_coupon_use": "high"},
    {"birth_year": 2003, "sex": "F", "marital_status": "single", "yearly_household_income_percentile": 40, "number_of_toddlers": 0, "number_of_teens": 0, "highest_education": "bachelors", "monthly_spend_on_wine": 25, "monthly_spend_on_vegetables": 55, "monthly_spend_on_toys": 0, "last_month_coupon_use": "none"},
    {"birth_year": 1972, "sex": "M", "marital_status": "married", "yearly_household_income_percentile": 70, "number_of_toddlers": 0, "number_of_teens": 1, "highest_education": "masters", "monthly_spend_on_wine": 60, "monthly_spend_on_vegetables": 70, "monthly_spend_on_toys": 40, "last_month_coupon_use": "low"},
    {"birth_year": 1988, "sex": "F", "marital_status": "married", "yearly_household_income_percentile": 55, "number_of_toddlers": 1, "number_of_teens": 0, "highest_education": "associates", "monthly_spend_on_wine": 20, "monthly_spend_on_vegetables": 40, "monthly_spend_on_toys": 30, "last_month_coupon_use": "high"},
    {"birth_year": 1970, "sex": "M", "marital_status": "single", "yearly_household_income_percentile": 60, "number_of_toddlers": 0, "number_of_teens": 0, "highest_education": "high_school", "monthly_spend_on_wine": 35, "monthly_spend_on_vegetables": 60, "monthly_spend_on_toys": 0, "last_month_coupon_use": "none"}
]
'''

# Load JSON data
customers = json.loads(customers_json)

# Create a DataFrame
df = pd.DataFrame(customers)

# Save to Excel file
excel_file_path = 'customers_data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Data successfully saved to {excel_file_path}")
