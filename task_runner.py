from agents import Agent, trace, Runner
import asyncio
from click import prompt

from db_impl import query_agent
from reader import filereader, reader_agent


async def start(performance_path,kpa_path):
  """run the agents using the file paths provided in the inputs"""
  with trace ("Reading Excel files"):
   result = await Runner.run(reader_agent, f"Read the excel files {performance_path} and {kpa_path}, and analyse the file ")
  agent_output = result.final_output
  return agent_output


async def run_db(prompt):
  with trace ("querying the database"):
   result_1 = await Runner.run(query_agent, f"Retrieve the data specified by user's {prompt} and provide overall analysis if users requests it ")
  return result_1.final_output
     
  


 
    


