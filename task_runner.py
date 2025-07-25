from agents import Agent, trace, Runner
import asyncio

from click import prompt

from reader import filereader, reader_agent

async def start(performance_path,kpa_path):
  """run the agents using the file paths provided in the inputs"""
  with trace ("Reading Excel files"):
   result = await Runner.run(reader_agent, f"Read the excel files {performance_path} and {kpa_path}, and analyse the file ")
  agent_output = result.final_output
  return agent_output
  
  
 

 
    


