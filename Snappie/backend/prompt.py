from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory

def prompt(input):
    llm = OpenAI(
        temperature=0,
        openai_api_key="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",
        model_name="text-davinci-003"
    )

    conversation_buf = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )

    return conversation_buf(input)['response']

if __name__ == "__main__":
    print(prompt("Hi!"))