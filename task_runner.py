from agents import Agent, trace, Runner
import asyncio

from click import prompt


from analyst import analyst_agent
from reader import filereader, reader_agent

async def start(performance_path,kpa_path):
  """run the agents using the file paths provided in the inputs"""
  with trace ("Reading Excel files"):
   result = await Runner.run(reader_agent, f"Read the excel files {performance_path} and {kpa_path} ")
   result.final_output

  with trace ("Analysing Excel files"):
    final_results = await Runner.run(analyst_agent,f"analyse the data from the files/output provided by the {result.final_output} and print result in full details" )
    return final_results.final_output
    


