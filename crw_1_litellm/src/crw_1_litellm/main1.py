from crewai.flow import Flow, listen, start
from litellm import completion

class LiteLLmFlow(Flow):

    @start()
    def start_function(self):
        input_text = input("Enter the text: ")  # Get the input text
        output = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                {'role': 'user',
                 'content': input_text
                 } 
            ]
        )
        return output['choices'][0]['message']['content']  # Return the output


#    @start()
#    def generate_text(self):
#        print("Generating text")
#        self.state.text = completion("Once upon a time, there was a", max_tokens=100)

    # @listen(start_function)  # Change this to listen(generate_text) if you want to use the commented out function
    # def save_text(self):
    #     print("Saving text")
    #     with open("text.txt", "w") as f:
    #         f.write(self.state.text)

def run_litellm_flow():
    object = LiteLLmFlow()
    result = object.kickoff()  # Start the flow and get the result
    print(result)  # Print the result