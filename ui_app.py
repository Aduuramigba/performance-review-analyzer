from os import path
from typing import final
import gradio as gr
from gradio.components import button, chatbot
from pathlib import Path
from dotenv import load_dotenv
import os 
from db_impl import collection
from task_runner import run_db, start

load_dotenv(override=True)

#database set up



async def run(performance_path, kpa_path):
        performance_path = Path(performance_path)
        kpa_path = Path(kpa_path)
        final = await start(performance_path,kpa_path) 
        if hasattr(final, "dict"): #checks if the output is a pydantic model
         bson_form = final.model_dump() # converts the output to bson cause mongodb only accepts bson pbkects
        collection.insert_one(bson_form)
        return (final)  

async def ask_agent(prompt):
 answer = await run_db(prompt)
 return answer     


with gr.Blocks(theme=gr.themes.Default(primary_hue="blue")) as ui :
    performance_data = gr.File(label="upload performance file",type="filepath" )
    kpa_data = gr.File(label="upload KPA data",type="filepath")
    submit_button = gr.Button("submit", variant = "primary")
    outputs = gr.Textbox()

    submit_button.click(
        fn=run,
        inputs=[performance_data, kpa_data],
        outputs=outputs
    )

    chatbot = gr.Interface(  
        fn=ask_agent,
        inputs=gr.Textbox(lines=2, placeholder="Ask something..."),
        outputs=gr.Textbox()
    )
    

ui.launch(debug=True)