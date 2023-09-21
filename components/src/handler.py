import sys
import os
from openai_key import openAI_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain , LLMChain, SequentialChain
from langchain.memory import ConversationBufferWindowMemory

os.environ['OPENAI_API_KEY'] = openAI_key


llm = OpenAI(temperature= 0.7)

def generate_story(genre, length, additional_info):
    PromptTemplate_name = PromptTemplate(
        input_variables= ['genre'],
        template="I want to write {genre} book, suggest a fancy name for it."
    )

    name_chain = LLMChain(llm=llm, prompt= PromptTemplate_name, output_key= "book_name")

    PromptTemplate_sentences = PromptTemplate(
        input_variables= ['length','book_name','additional_info'],
        template= '''You are a story generator, 
                  Write a {length} sentences of {book_name} book, and {additional_info}'''
    )

    sentence_chain = LLMChain(llm=llm, prompt= PromptTemplate_sentences, memory=ConversationBufferWindowMemory(k=4, input_key='history'),  output_key= "Sentences")


    chain = SequentialChain(
                    chains= [name_chain, sentence_chain],
                    input_variables= ['genre', 'length', 'additional_info'],
                    output_variables= ["book_name", "Sentences"]
                            )

    response = chain({'genre': genre, 'length': length, 'additional_info': additional_info})
    return(response)

#Handle the data formate 

def format_output(genre, length, additional_info):
    # Create the formatted output string based on user inputs
    output = ""
    response = generate_story(genre, length, additional_info)
    output += f"Genre: {response['genre']}\n"
    output += f"Book Name:{response['book_name']}\n"  
    output += f"Length: {response['length']}\n\n"
    output += f"Generated Story:\n{response['Sentences']}"
    return output




# #Example
# result = chain('Romance')
# print(result)