from dotenv import load_dotenv

import assistant_utils

if __name__ == '__main__':
    load_dotenv()
    assistant = assistant_utils.get_assistant()
    agent = assistant_utils.get_agent_with_tools(assistant)
    agent_output = agent.run(
        "What was the high temperature in Taiwan yesterday in Kaohsiung? What is that number different with the high temperature in Taiwan yesterday in Taipei? To the end, display temperature in Celsius.")
    print(agent_output)
