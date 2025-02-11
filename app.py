<<<<<<< HEAD
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from dotenv import load_dotenv
from langchain.callbacks import StreamlitCallbackHandler

## set up app

st.set_page_config(page_title="Text to Math Solver and Data search assistant")
st.title("Text to Math Problem Solver using Gemma")

groq_api_key = st.sidebar.text_input(label="groq api key",type ="password")

if not groq_api_key:
    st.info("Please add your groq api key")
    st.stop()

llm = ChatGroq(model="deepseek-r1-distill-llama-70b",groq_api_key=groq_api_key)

#initialize the tools
wikipedia_wrapper= WikipediaAPIWrapper()
wiki_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the internet to find the various information on the topics mentioned"
)

#initialize math tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func = math_chain.run,
    description="A tools for answering math related questions. Only input mathematical expression needs to be provided."
)

prompt = """
You are an agent tasked for solving mathematical question. Logically arrive at the solution and display it point wise
for the question below
Question:{question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

##combine all tools into chain
chain = LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func= chain.run,
    description="A tool for answering logic based and reasoning questions"
)

##initialize agents

assistant_agent = initialize_agent(
    tools=[wiki_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a math chatbot who can answer all your maths questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

question=st.text_area("Enter your question:","")

#func to generate response
def generate_response(user_question):
    response=assistant_agent.invoke({"input":question})
    return response

#start interaction

if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])

            st.session_state.messages.append({"role":"assistant","content":response})
            st.write("REsponse:")
            st.success(response)
    else:
        st.warning("Please enter question")



=======
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from dotenv import load_dotenv
from langchain.callbacks import StreamlitCallbackHandler

## set up streamlit app

st.set_page_config(page_title="Text to Math Solver and Data search assistant")
st.title("Text to Math Problem Solver using Gemma")

groq_api_key = st.sidebar.text_input(label="groq api key",type ="password")

if not groq_api_key:
    st.info("Please add your groq api key")
    st.stop()

llm = ChatGroq(model="deepseek-r1-distill-llama-70b",groq_api_key=groq_api_key)

#initialize the tools
wikipedia_wrapper= WikipediaAPIWrapper()
wiki_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the internet to find the various information on the topics mentioned"
)

#initialize math tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func = math_chain.run,
    description="A tools for answering math related questions. Only input mathematical expression needs to be provided."
)

prompt = """
You are an agent tasked for solving mathematical question. Logically arrive at the solution and display it point wise
for the question below
Question:{question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

##combine all tools into chain
chain = LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func= chain.run,
    description="A tool for answering logic based and reasoning questions"
)

##initialize agents

assistant_agent = initialize_agent(
    tools=[wiki_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a math chatbot who can answer all your maths questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

question=st.text_area("Enter your question:","")

#func to generate response
def generate_response(user_question):
    response=assistant_agent.invoke({"input":question})
    return response

#start interaction

if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])

            st.session_state.messages.append({"role":"assistant","content":response})
            st.write("REsponse:")
            st.success(response)
    else:
        st.warning("Please enter question")



>>>>>>> 62fb7aa3da928ff99218176f188de3836d0742d6
