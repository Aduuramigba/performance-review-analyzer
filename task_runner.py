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
  
  
   tool1 = reader_agent.as_tool(tool_name="sales_agent1", tool_description= "reads excel file" )

  with trace ("Analysing Excel files"):
    final_results = await Runner.run(analyst_agent,f"""analyse the data from the files/output provided by the {result.final_output} \
    and print result line by line in cases where objectives in section A, key metrics in section B 
    or agreed action steps in section E are more than one from the {performance_path} make sure to captue
    all the items, it is very important to make sure you're picking the data from {performance_path} and give a detailed and insightful summary on your analysis""" )
    return final_results.final_output
    


