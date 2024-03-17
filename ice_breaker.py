import sys
import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
third_parties_dir = os.path.join(current_dir, 'third_parties')
sys.path.append(third_parties_dir)

from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from linkedin_response_creightonfriend import linkedin_data

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    nub_api_key = os.environ.get('NOOB_API_KEY')  # Safely get the environment variable

    if nub_api_key:
        print(f"Hello, LangChain! {nub_api_key}")
    else:
        print("NOOB_API_KEY not found in environment variables.")

    information = linkedin_data
    information = {
        k: v
        for k, v in information.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    summary_template = """
    Analyze the following info: {information}, <-- This info is about a noob on LinkedIn, I want you to create:
    1. A Short Summary
    2. Three interesting facts about them.
    3. Three reasons why they would be a good candidate for a Medical Science Liaison.  
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_template)
    llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": information})

    if 'text' in res:
        print(res['text'])
    else:
        print("No summary text found in the response.")