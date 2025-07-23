from os import path
from typing import final
import gradio as gr
from gradio.components import button
from pathlib import Path
from dotenv import load_dotenv

import task_runner

load_dotenv(override=True)


async def run(performance_path, kpa_path):
        performance_path = Path(performance_path)
        kpa_path = Path(kpa_path)
        final = await task_runner.start(performance_path,kpa_path) 
        return (final)  
  



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


ui.launch(debug=True)