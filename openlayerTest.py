from openai import OpenAI

api_key = '--'

import os
import openai
from openlayer import llm_monitors

openlayer_api_key = "--"
project_name = "Test Project"

os.environ["OPENLAYER_API_KEY"] = openlayer_api_key
os.environ["OPENLAYER_PROJECT_NAME"] = project_name
os.environ["OPENAI_API_KEY"] = "--"


openai_client = openai.OpenAI()
# With publish=True, every row is published to Openlayer
monitor = llm_monitors.OpenAIMonitor(client=openai_client, publish=True)
monitor.start_monitoring()


def create_gpt_chat_agent():
    client = OpenAI(api_key=api_key)

    def chat_with_gpt(prompt):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are an expert research assistant."}, 
                          {"role": "user", "content": prompt}]
            )
            # Corrected response access
            return response.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {e}"

    return chat_with_gpt

def main():
    gpt_chat_agent = create_gpt_chat_agent()

    while True:
        user_input = input("You: ")
        
        # Check if the user wants to exit the chat
        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            print("Exiting chat...")
            break

        response = gpt_chat_agent(user_input)
        print("GPT:", response)

if __name__ == "__main__":
    main()

    monitor.stop_monitoring()