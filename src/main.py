# main.py

import os
import json
import pandas as pd
from tqdm import tqdm
from crewai import Agent, Task, Crew, Process
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import logging
from tasks import *
from agents import *
from io import StringIO
import openpyxl  # Make sure to have openpyxl installed for Excel output

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
llm = ChatOpenAI(model=OPENAI_MODEL_NAME)



# Input JSON strings
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

# Load customers and products from JSON
customers = json.loads(customers_json)
products = json.loads(products_json)

df_customers = pd.DataFrame(customers)

df_output_list = []  # to store results

for index, row in df_customers.iterrows():
    print('############################################## ' + str(index))
    customer_description = f'''The customer was born in {row['birth_year']}.
    Its sex is {row['sex']}.
    Its marital status is {row['marital_status']}.
    Its yearly household income percentile is {row['yearly_household_income_percentile']}.
    The customer has {row['number_of_toddlers']} toddlers.
    The customer has {row['number_of_teens']} teenage kids.
    The customer highest education is {row['highest_education']}.
    The customer spends on average {row['monthly_spend_on_wine']} $ on wine.
    The customer spends on average {row['monthly_spend_on_vegetables']} $ on vegetables.
    The customer spends on average {row['monthly_spend_on_toys']} $ on toys.
    The customer's coupon use is {row['last_month_coupon_use']}.
    '''
    task1 = get_ad_campaign_task(Chief_Promotional_Director, customer_description, products)

    targetting_crew = Crew(
        agents=[profiler, product_specialist, Chief_Promotional_Director],
        tasks=[task1],
        verbose=2,  # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
        process=Process.sequential  # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
    )
    targetting_result = targetting_crew.kickoff()
    
    content_results = {}
    for variation in ["creative", "basic advertising", "aggressive"]:
        task2 = get_ad_campaign_written_task(Chief_Promotional_Director, targetting_result, variation)
        copywriting_crew = Crew(
            agents=[creative_content_creator_agent, Chief_Promotional_Director],
            tasks=[task2],
            verbose=2,  # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
            process=Process.sequential  # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
        )
        copywriting_result = copywriting_crew.kickoff()
        content_results[variation] = copywriting_result

    # Append results to output list
    df_output_list.append({
        'Customer Description': customer_description,
        'Top 3 Products': targetting_result,
        'Creative Content': content_results['creative'],
        'Basic Advertising Content': content_results['basic advertising'],
        'Aggressive Content': content_results['aggressive']
    })

# Convert output list to DataFrame
df_output = pd.DataFrame(df_output_list)

# Save DataFrame to Excel
df_output.to_excel('marketing_campaign_results.xlsx', index=False)
print("Output saved to marketing_campaign_results.xlsx")
