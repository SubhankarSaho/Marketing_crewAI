#task.py
from textwrap import dedent
from crewai import Task

products = '''
Fresh Lettuce
Diapers
Irish whiskey
laundry detergent
Chips
Spaghetti cans (ready to eat)
Minecraft Video Game
Mascara
Toilet Paper (best value)
Wagyu beef steak
Organic avocados
Cigarettes
'''

def get_profiling_task(agent, customer_description):
    return Task(
        description=dedent(f"""\
        You're creating a targeted marketing campaign tailored to what we know about our customers.

        For each customer, we have to choose exactly three products to promote in the next campaign.
        Make sure the selection is the best possible and aligned with the customer,
        review, approve, ask clarifying question or delegate follow up work if
        necessary to make decisions. When delegating work send the full draft
        as part of the information.
        This is the list of all the products participating in the campaign: {products}.
        This is all we know so far from the customer: {customer_description}.

        To start this campaign we will need to build first an understanding of our customer.
        Once we have a profile about the customers interests, lifestyle and means and needs,
        we have to select exactly three products that have the highest chance to be bought by them.

        Your final answer MUST be exactly 3 products from the list, each with a short description
        why it matches with this customer. It must be formatted like this example:
        <Product 1> : <Product 1 description>
        <Product 2> : <Product 2 description>
        <Product 3> : <Product 3 description>
        """),
        agent=agent,
        expected_output=dedent(f"""\
        <Product 1> : <Product 1 description>
        <Product 2> : <Product 2 description>
        <Product 3> : <Product 3 description>
        """)
    )

def get_ad_campaign_task(agent, customer_description, products):
    return Task(
        description=dedent(f"""\
        You're creating a targeted marketing campaign tailored to what we know about our customers.

        For each customer, we have to choose exactly three products to promote in the next campaign.
        Make sure the selection is the best possible and aligned with the customer,
        review, approve, ask clarifying question or delegate follow up work if
        necessary to make decisions. When delegating work send the full draft
        as part of the information.
        This is the list of all the products participating in the campaign: {products}.
        This is all we know so far from the customer: {customer_description}.

        To start this campaign we will need to build first an understanding of our customer.
        Once we have a profile about the customers interests, lifestyle and means and needs,
        we have to select exactly three products that have the highest chance to be bought by them.

        Your final answer MUST be exactly 3 products from the list, each with a short description
        why it matches with this customer. It must be formatted like this example:
        <Product 1> : <Product 1 description>
        <Product 2> : <Product 2 description>
        <Product 3> : <Product 3 description>
        """),
        agent=agent,
        expected_output=dedent(f"""\
        <Product 1> : <Product 1 description>
        <Product 2> : <Product 2 description>
        <Product 3> : <Product 3 description>
        """)
    )

# tasks.py
def get_ad_campaign_written_task(agent, targetting_result, content_type):
    return Task(
        description=dedent(f"""\
        You're creating a targeted marketing campaign tailored to what we know about our customers.

        For each customer, we have chosen three products to promote in the next campaign.
        This selection is tailored specifically to the customer: {targetting_result}.

        Create a {content_type} ad campaign message.

        To end this campaign successfully we will need a promotional message advertising these products to the customer with the ultimate intent that they buy from us.
        This message should be around 3 paragraphs, so that it can be easily integrated into the full letter. For example:
        Tired of making dinner, get our best ready made canned tuna.
        Your lifestyle deserves a taste of this fresh lobster.
        In the weekends, go on a day trip with the kids with these new lunch box containers.

        You need to review, approve, and delegate follow up work if necessary to have the complete promotional message. When delegating work send the full draft
        as part of the information.

        Your final answer MUST include the 3 products from the list, each with a short promotional message.
        """),
        agent=agent,
        expected_output=dedent(f"""\
        <Product 1> : <Product 1 promotional message>
        <Product 2> : <Product 2 promotional message>
        <Product 3> : <Product 3 promotional message>
        """)
    )