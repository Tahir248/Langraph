import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
# from langchain_community.tools.tavily_search import TavilySearchResults # OLD
from langchain_tavily import TavilySearch # NEW
from langgraph.prebuilt import create_react_agent # OLD WAY - BUT STABLE
# from langchain.agents import create_react_agent # NEW WAY (as suggested by warning)
import warnings
warnings.filterwarnings("ignore") # Ye sari faltu warnings chhupa dega

load_dotenv()  # Ye command khud hi .env file se keys utha legi

# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

# 1. Tool Setup
tools = [TavilySearch(max_results=2)]

# 2. Model Setup (Gemini)
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite-preview",
    temperature=0  # Ye AI ko thora natural aur conversational banayega
)

# 3. Agent Creation
agent = create_react_agent(model, tools, prompt="Your name is Ladla. You are a helpful and friendly assistant.")

# 4. Run Agent
# response = agent.invoke({"messages": [("user", "How today's weather in Karachi?")]})
# print("Agent Response:", response["messages"][-1].content)

print("--- Ladla AI Research Agent (Type 'exit' to quit) ---")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Ladla: Allah Hafiz!")
        break
        
    response = agent.invoke({"messages": [("user", user_input)]})
    
    content = response["messages"][-1].content

    print("\nLadla:", content[0]['text'])  # Assuming the response is in the expected format