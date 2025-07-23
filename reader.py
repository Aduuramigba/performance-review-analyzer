from dis import Instruction 
import pandas as pd
from agents import Agent, function_tool









@function_tool
def filereader(performance_path: str, kpa_path: str) -> dict:
    df_perf = pd.read_excel(performance_path)
    df_kpa = pd.read_excel(kpa_path)
    return {
        "performance": df_perf.to_dict(orient="records"),
        "kpa": df_kpa.to_dict(orient="records")
    }

INSTRUCTIONS =  f"You're an expert at reading excel files with a knack for paying attention to tiny details,\
     you use the {filereader} to read the excel files provided, " 

reader_agent = Agent(
    name="Reader agent",
    instructions=INSTRUCTIONS,
    tools=[filereader],
    model="gpt-4o-mini",
   
)

