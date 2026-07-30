#=========LOAD MODULES================



from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import langchain
from langchain.agents import create_agent
import langchain_community
from tavily import TavilyClient
import pytesseract as pyt
import streamlit as st
import os
import time
from PIL import Image
import pandas as pd
import numpy as np


# To show web-app: complete page layout
st.set_page_config(layout="wide")


# To Give Title 
st.title("AI RESUME GENERATOR")

st.write("""This app helps user to build customized Professional
Resume with Latest Jobapply links""")

st.image("bg.png")



#==========API KEY====================
#step 3: Api keys
GOOGLE_API_KEY = "AQ.Ab8RN6KLKN6ZVnfMf6o2Yg8Hx8L0n02ksp63RSQZ3P0Y7Kjkew"
GROQ_API_KEY = "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"
TAVILY_API_KEY = "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"


model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash-lite',
    google_api_key = GOOGLE_API_KEY
)

# response = model.invoke("Hello Buddy!")
# response.content[-1]['text']




def search_latest_news_jobs(query):
  """This function helps to fetch latest
  news or job related article using tavily"""

  client = TavilyClient(
      api_key = TAVILY_API_KEY)
  response = client.search(query)
  return response



# Agent Creation
agent = create_agent(
    model = model,
    tools = [
        search_latest_news_jobs
    ]
)
# agent







def main_agent(agent,query):
  """This is prompt agent, or leader agent
orchestrate sub agents"""

  # Giving promp to create deatiled propmt
  # for code generation
  prompt = """You are AI assistant and below given is a prompt, your task is to give detailed
  prompt for this.
  You are a professional Resume generator where user will give their personal info, you have to create
  detailed Resume for students or professional one, it must be with dynamic UI and UX and, with
  advanced CSS Professional Designing, Make sure to give output in HTML format only no markdowns allowed
  """

  response = agent.invoke({'messages':[{'role':'user','content':prompt}]})
  detailed_prompt = response['messages'][-1].content[-1]['text']

  # SAVE PROMPT using File Hnadling

  with open('prompt.txt','w') as f:
    f.write(detailed_prompt)

  user_details = f"""Bleow Given is a user details generate Resume based on that,
  if not given keep: Default Resume: Python Developer
  user details: {query}"""





def main_agent(agent,query):
  """This is prompt agent, or leader agent
orchestrate sub agents"""

  # Giving promp to create deatiled propmt
  # for code generation
  prompt = """You are AI assistant and below given is a prompt, your task is to give detailed
  prompt for this.
  You are a professional Resume generator where user will give their personal info, you have to create
  detailed Resume for students or professional one, it must be with dynamic UI and UX and, with
  advanced CSS Professional Designing, Make sure to give output in HTML format only no markdowns allowed
  """

  response = agent.invoke({'messages':[{'role':'user','content':prompt}]})
  detailed_prompt = response['messages'][-1].content[-1]['text']

  # SAVE PROMPT using File Hnadling

  with open('prompt.txt','w') as f:
    f.write(detailed_prompt)

  user_details = f"""Bleow Given is a user details generate Resume based on that,
  if not given keep: Default Resume: Python Developer
  user details: {query}"""

  final_prompt = prompt + detailed_prompt + user_details

    #Code Generation
  response = agent.invoke({'messages':[{'role':'user','content':final_prompt}]})
  code = response['messages'][-1].content[-1]['text']

  return code





#   code = main_agent(agent,"GIGA NIGGA, IITM BCA STUDENT")
# from IPython import display as DISPLAY
# DISPLAY.HTML(code)







# Fetch Latest Domain related Jobs using Tavily
def get_jobs(agent,
             Location = "Noida,Delhi",
             Profile = "Data Analysts, AI Engineer"):
  Location = "Noida,Delhi"
  Profile = "Data Analyst, AI Engineer"

  prompt = f"""Based on user given Job profile, fetch Latest jobs or job apply article
  using Naukri, Linkedin, Indeed, or all popular
  Job apply platforms, Show Results with
  JOB PROFILE NAME, LOCATION, SALARY, COMPANY NAME,
  SHOW jobs only related to given
  {Location} and {Profile}. Output must be in Professional HTML Naukri theme cards with Dynamic Design,
  Show atleast Top 10-20 results with direct apply link"""

  response = agent.invoke({'messages':[{'role':'user','content':prompt}]})

  code = response['messages'][-1].content[-1]['text']

  return code




#   code = get_jobs(agent)
# DISPLAY.HTML(code)




