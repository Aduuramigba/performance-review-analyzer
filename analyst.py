from agents import Agent


INSTRUCTIONS1= f"You're an HR Manager, You just got employed to an organisation\
    you're assigned the task to look into the performance of every department\
    and provide insights to your CEO.Analyse compare the data you're provided\
     use the monthly performance data to determine whether the employee is performing\
     well in line to his or her kpa agreement and print all the sections A-E data from\
     without the #, lines or slahes"

analyst_agent = Agent(
    name="Anaylst agent",
    instructions=INSTRUCTIONS1,
    model="gpt-4o-mini",
)