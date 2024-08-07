from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")


def generate_script(prompt, video_length, creativity):

    # Template for generating 'Title'
    title_template = PromptTemplate(
        input_variables=["subject"],
        template="Please come up with a title for a YouTube video on the  {subject}.",
    )

    # Template for generating 'Video Script' using search engine
    script_template = PromptTemplate(
        input_variables=["title", "DuckDuckGo_Search", "duration"],
        template="Create a script for a YouTube video based on this title for me. TITLE: {title} of duration: {duration} minutes using this search data {DuckDuckGo_Search} ",
    )

    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=creativity,
        token=HUGGINGFACEHUB_API_TOKEN,
        max_new_tokens=512,
    )

    # Creating chain for 'Title' & 'Video Script'
    title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
    script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)

    search = DuckDuckGoSearchRun()

    # Executing the chains we created for 'Title'
    title = title_chain.invoke(prompt)

    # Executing the chains we created for 'Video Script' by taking help of search engine 'DuckDuckGo'
    search_result = search.run(prompt)
    script = script_chain.run(
        title=title, DuckDuckGo_Search=search_result, duration=video_length
    )

    # Returning the output
    return search_result, title, script
