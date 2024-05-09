from dotenv import load_dotenv

import assistant_utils

if __name__ == '__main__':
    load_dotenv()
    assistant = assistant_utils.get_assistant()
    output = assistant.invoke({"content": "What's 10 - 4 raised to the 2.7"})
    print(output)

