from ast import Dict
from os import name
from agents import Agent
from openai import BaseModel
from typing import List, Optional
from pprint import pprint



from openai.types.responses.response_reasoning_item import Summary

from reader import tool1  


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

        output += "\n🔸 Section B: KEY METRICS\\ KPI\n"
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



INSTRUCTIONS1= f""" You're an HR Manager, You just got employed to an organisation
    you're assigned the task to look into the performance of every department
    and provide insights to your CEO.Analyse compare the data you're provided
     use the monthly performance data to determine whether the employee is performing
     well in line to his or her kpa agreement use {clean_output} to generate your output make sure to capture 
     all objectives, key metrics, agreed actions if there is more than one"""



analyst_agent = Agent(
    name="Anaylst agent",
    instructions=INSTRUCTIONS1,
    output_type=clean_output,
    model= "gpt-4o",
    
    
)