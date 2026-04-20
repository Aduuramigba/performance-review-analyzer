
from pymongo import MongoClient
from agents import Agent, function_tool
from typing import List, Optional
from pydantic import BaseModel

from reader import INSTRUCTIONS



client = MongoClient("mongodb://localhost:27017/")
db = client.monthly_performance
collection = db.monthly_performance

class QueryInput(BaseModel):
    name: Optional[str] = None
    month: Optional[List[str]] = None

@function_tool
def query_database(input: QueryInput) -> list:

    query = {}

    # Add case-insensitive regex filter for 'name'
    if input.name:
        query["Employee_Name"] = {"$regex": input.name, "$options": "i"}  # exact match, case-insensitive

    # Match 'month' using $in operator (multiple allowed)
    if input.month:
        query["Month_of_Review"] = {"$in": input.month} #exact match, case insensitive


    # Debug print statements
    print("Constructed Query:", query)

    results = list(collection.find(query, {"_id": 0}))
    return results or ["no matching records found"]
     
     
INSTRUCTIONS1 = f"""you are a query agent, you extract keyword like name (a string) 
             month (a list of strings, even if user mentions one),
            from user inputs and retrieve the data specified using {query_database} only use the tool if at least one field is called,
            and provide an overall analysis on the data only when user specifies it""" 

query_agent = Agent(
        name= "Query agent",
        instructions=INSTRUCTIONS1,
        tools=[query_database],
         model="gpt-4o-mini",
   

       )



     


