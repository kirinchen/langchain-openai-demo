import os
from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.agents import load_tools


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_dotenv()
    llm = OpenAI()
    tools = load_tools(["serpapi", "llm-math"], llm=llm)

    # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
        name="langchain assistant",
        instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4"
    )
    output = interpreter_assistant.invoke({"content": "What's 10 - 4 raised to the 2.7"})
    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
