from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get('API_KEY')

def prompt(input):
    llm = OpenAI(
        temperature=0,
        openai_api_key=API_KEY,
        model_name="text-davinci-003"
    )

    conversation_buf = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )

    return conversation_buf(input)['response']

if __name__ == "__main__":
    print(prompt("Hi!"))