from agents import agent_output
from reader import clean_output 
import asyncio
from pymongo import MongoClient
from task_runner import start 
from ui_app import performance_path, kpa_path


client = MongoClient("localhost", 27017)

db = client.perf
collection = db.my_data 

collection.insert_one(asyncio.run(start(performance_path,kpa_path)))
