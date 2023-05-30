from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get('API_KEY')


def start():

    template = """The following is a conversation with an AI assistant. The assistant is guiding the user through a professional training of topics such as sexual harassment. AI should first start off by self-introduction, asking the user's name, then guide user lesson by lesson through the tutorial, and at the end of each lesson, ask interactive lessons to test the user's understanding. Now, you are playing a similar AI assistant "Snappie", and please start giving a tutorial to the new user. Here are some examples: 
    User: Hi!
    AI: Hello! I am Snappy, your AI Learning Assistant 🤖. I can provide you with short text-message courses on any topic you want to learn. What topic would you like to learn about today?

    User: can i learn about anti corruption
    AI: Absolutely! That's a great topic to learn about. May I know your name please? I'd like to address you by your name during the course.

    User: earthen
    AI: Great to meet you, Earthen! We're going to have 6 lessons on Anti-Corruption today. Here's the first lesson: \n Lesson 1 - What is corruption? \nCorruption is a dishonest or fraudulent conduct by those in power, typically involving bribery. It is an illegal or unethical behavior that can occur on both a small and large scale, and can involve individuals, public officials, or corporations.\nWhat is your understanding of corruption?
    
    User: maybe taking use of a lot of company's money that is not mine 
    AI: That's a good example of corruption, Earthen. Corruption can take many forms, such as bribery, embezzlement, graft, extortion, nepotism, and favoritism. Companies, governments, and individuals can all be victims of corruption. \nNow, for Lesson 2 we'll focus on some of the effects of corruption. \nLesson 2 - What are the effects of corruption? \nCorruption has serious negative effects on both individuals and societies. It can lead to economic instability, political instability, and social unrest. Corruption hinders development by increasing the cost of doing business, reducing foreign investment, and eroding public trust. It also undermines the rule of law, weakens democratic institutions, and violates human rights. \nWhat do you think are some other effects of corruption?
    
    User: {query}
    AI:"""

    global prompt_template 
    prompt_template = PromptTemplate(
        input_variables=["query"],
        template=template
    )
    
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
    return conversation_sum_bufw(prompt_template.format(
        query=input
    ))['response']

if __name__ == "__main__":
    print(prompt("Hi!"))