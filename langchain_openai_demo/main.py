import os
from openai import OpenAI
from langchain_experimental.openai_assistant import OpenAIAssistantRunnable
from dotenv import load_dotenv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_dotenv()
    interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
        name="langchain assistant",
        instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4"
    )

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
