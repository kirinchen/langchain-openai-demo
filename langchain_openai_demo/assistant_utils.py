import os

from langchain.agents import initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.language_models import BaseLanguageModel
from openai import OpenAI
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser  # Updated import
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from dotenv import load_dotenv


def create_new_assistant():
    interpreter_assistant = OpenAIAssistantRunnable.create_assistant(
        name="langchain assistant",
        instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4"
    )
    return interpreter_assistant


def get_assistant():
    agent = OpenAIAssistantRunnable(assistant_id=os.getenv('OPENAI_ASSISTANT_ID'), as_agent=True)
    return agent


def get_agent_with_tools(assistant: OpenAIAssistantRunnable):
    llm: BaseLanguageModel = assistant
    # Load tools with the LLM instance
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    # Initialize agent with tools and LLM
    agent = initialize_agent(tools=tools, llm=llm, verbose=True)
    return agent
