from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get('API_KEY')


def start():
    #set up model
    llm = OpenAI(
        temperature=0,
        openai_api_key=API_KEY,
        model_name="text-davinci-003"
    )

    global conversation_sum_bufw
    conversation_sum_bufw = ConversationChain(
        llm=llm, 
        memory=ConversationSummaryBufferMemory(
            llm=llm,
            max_token_limit=650
        )
    )

def prompt(input):
    return conversation_sum_bufw(input)['response']

if __name__ == "__main__":
    print(prompt("Hi!"))