from langchain.tools import DuckDuckGoSearchRun,WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain import hub
from langchain.agents import Tool,AgentExecutor,initialize_agent,create_react_agent
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv,find_dotenv
import google.generativeai as genai
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv(find_dotenv(),override=True)

llm=ChatOpenAI(model='gpt-3.5-turbo',temperature=0)

template='''
Answer the question:
{q}
'''

prompt_template=PromptTemplate.from_template(template)
prompt=hub.pull('hwchase17/react')
#print(prompt.template)
python_repl=PythonREPLTool()
python_repl_tool=Tool(
    name='Python REPL',
    func=python_repl.run,
    description='usefull for python code'
)

api_wrapper=WikipediaAPIWrapper()
wikipedia=WikipediaQueryRun(api_wrapper=api_wrapper)
wiki_tool=Tool(
    name='Wikipedia',
    func=wikipedia.run,
    description='for searching about countries,person,etc'
)

seaarch=DuckDuckGoSearchRun()
duckgo_tool=Tool(
    name='DuckDuckGoSearch',
    func=search.run,
    description='to search the info that other web cannot provide'
)

tools=[python_repl_tool,wiki_tool,duckgo_tool]

agent=create_react_agent(llm,tools,prompt)
agent_executor=AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iteration=10
)
#question='sum of all prime numbers from 1 to 30'
question='who is draupadi murmu'
res=agent_executor.invoke({
    'input':prompt_template.format(q=question)
})