from crewai.flow import Flow, start, listen
from crw_3_multiple_agents_with_yaml.crews.dev_crew.dev_crew import DevCrew 


#Note: I use here generate_code Sir Qasim use here run_dev_crew This is for user input or solve problem or write code.
#Note: For output kickoff method import and connected from @CrewBase() class DevCrew: in dev_crew.py file.
class DevFlow(Flow):
    @start()
    def generate_code(self):  
     output = DevCrew().crew().kickoff( 
        inputs={
             "problem":"write python code for addition two numbers"
        } 
     )
     return output.raw #raw is for future object or data
    

def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result) #print result for output 