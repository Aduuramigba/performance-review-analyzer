from dis import Instruction 
import pandas as pd
from agents import Agent, function_tool
from openai import BaseModel
from typing import List, Optional


class objective(BaseModel):
    objectives: str
    start_date: str
    expected_end_date: str
    status: Optional[str]
    percent_completion: Optional[float] # so the agent understand that the cell contains options which could be none if anything isn't selected
    key_wins: str
    risk_issue: str

    class Config:
        extra = "forbid" 

class kpi_metric(BaseModel):
    kpi_metric: str
    target: str
    actual: str
    variance: str
    comments: str

    class Config:
        extra = "forbid" 

class Agreed_action(BaseModel):
    action_item: str
    owner:str
    deadline:str
    priority:str
    class Config:
        extra = "forbid" 

class clean_output(BaseModel):
    Employee_Name: str
    Role_Function: str
    Line_Manager_Reviewer: str
    Month_of_Review:str 
    Date_of_Check_In:str

    
    Section_A: List[objective]

    Section_B: List[kpi_metric]

    sections_C: str = "Employee self reflection"
    what_went_well_this_month: str
    challenges_blockers: str
    infrastructure_challenge: str

    Section_E: List[Agreed_action]

    Summary:str
    class Config:
        extra = "forbid" #disables additional properties of the agent i.e conforms the agent to follow a strict json schema

    def __str__(self):
        output = f"""
🔹 Employee Check-in Report
----------------------------------------
👤 Name: {self.Employee_Name}
🧑‍💼 Role/Function: {self.Role_Function}
🧑‍🏫 Line Manager: {self.Line_Manager_Reviewer}
🗓️ Review Month: {self.Month_of_Review}
📅 Date of Check-in: {self.Date_of_Check_In}

🔸 Section A: SMART Objectives
"""  
        for i, obj in enumerate(self.Section_A, 1):
            output += f"""
  {i}. Objective: {obj.objectives}
     - Start Date: {obj.start_date}
     - Expected End: {obj.expected_end_date}
     - Status: {obj.status or "N/A"}
     - Completion: {obj.percent_completion or "N/A"}%
     - Key Wins: {obj.key_wins}
     - Risk/Issue: {obj.risk_issue}
"""

        output += "\n🔸 Section B: KEY METRICS\n"
        for i, kpi in enumerate(self.Section_B, 1):
            output += f"""
  {i}. KPI: {kpi.kpi_metric}
     - Target: {kpi.target}
     - Actual: {kpi.actual}
     - Variance: {kpi.variance}
     - Comments: {kpi.comments}
"""

        output += f"""
🔸 Section C: Employee Self Reflection
   - What went well: {self.what_went_well_this_month}
   - Challenges/Blockers: {self.challenges_blockers}
   - Infra Challenges: {self.infrastructure_challenge}

🔸 Section E: Agreed Actions & Next Steps
"""
        for i, act in enumerate(self.Section_E, 1):
            output += f"""
  {i}. Action: {act.action_item}
     - Owner: {act.owner}
     - Deadline: {act.deadline}
     - Priority: {act.priority}
"""

        output += f"\n📌 Summary:\n{self.Summary}\n"
        return output









@function_tool
def filereader(performance_path: str, kpa_path: str) -> dict:
    df_perf = pd.read_excel(performance_path)
    df_kpa = pd.read_excel(kpa_path)
    return {
        "performance": df_perf.to_dict(orient="records"),
        "kpa": df_kpa.to_dict(orient="records")
    }

INSTRUCTIONS =  f"""You're an expert at reading excel files with a knack for paying attention to tiny details,\
     you use the {filereader} to read the excel files provided, use the monthly performance and the kpa dats to 
     determine if the level of the employee's performance.  """ 


reader_agent = Agent(
    name="Reader agent",
    instructions=INSTRUCTIONS,
    tools=[filereader],
    output_type=clean_output,
    model="gpt-4o-mini",
   
)
