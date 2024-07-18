# agents.py
from crewai import Agent
# from langchain_openai import ChatOpenAI
# from tasks import MarketingTasks
# import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import logging
from textwrap import dedent

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
llm = ChatOpenAI(model=OPENAI_MODEL_NAME)


profiler = Agent(
  role='profiler',
  goal='''From limited data, you logically deduct conclusions about people.''',
  backstory='You are an expert psychologist with decades of experience.',
  llm=llm,
  verbose=True,
  allow_delegation=True
)
product_specialist = Agent(
  role='product specialist',
  goal='''Match the product to the customer''',
  backstory='You have exceptional knowledge of the products and can say how valuable they are to a customer.',
  llm=llm,
  verbose=True,
  allow_delegation=True
)

Chief_Promotional_Director = Agent(
				role="Chief Promotion Director",
				goal=dedent("""\
					Oversee the work done by your team to make sure it's the best
					possible and aligned with the product's goals, review, approve,
					ask clarifying question or delegate follow up work if necessary to make
					decisions"""),
				backstory=dedent("""\
					You're the Chief Promotion Officer of a large retailer. You're launching a personalized ad campaign,
          trying to make sure your team is crafting the best possible
					content for the customer."""),
				tools=[],
				llm=llm,
				verbose=True
)

creative_content_creator_agent = Agent(
			role="Creative Content Creator",
			goal=dedent("""\
				Develop compelling and innovative content
				for ad campaigns, with a focus customer specific ad copies."""),
			backstory=dedent("""\
				As a Creative Content Creator at a top-tier
				digital marketing agency, you excel in crafting advertisements
				that resonate with potential customers.
				Your expertise lies in turning marketing strategies
				into engaging stories that capture
				attention and inspire buying action."""),
			llm=llm,
			verbose=True
		)