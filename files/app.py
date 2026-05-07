import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()  # Ye command khud hi .env file se keys utha legi

# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

# Custom tools
def deposite_money(name: str, account: int, amount: float) -> dict:
    print("---Deposite Money Tool Invoked---")
    """
        Deposite money into an account.
        Args:
            name (str): Account holder's name.
            account (int): Account number.
            amount (float): Amount to be deposited.
        Returns:
            dict: Confirmation message.
    """
    return {"message": f"Successfully deposited {amount} into account {account} for {name}."}

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite-preview",
    # api_key=google_key, // no need to pass api key here as it's already set in environment variables
    temperature=0.7  # Ye AI ko thora natural aur conversational banayega
)
model_with_tools = model.bind_tools([deposite_money])
user_input = input("\nYou: ")
message1 = user_input

messages = [
    # SystemMessage(content="Your name is Ladla. You are a helpful and friendly assistant."),
    HumanMessage(content=message1)
]

response = model_with_tools.invoke(messages)
print("AI Response:", response)

# # tavily tool initialize
# tool = TavilySearchResults(max_results=2)

# # tool use
# search_query = "What is the capital of France?"
# search_results = tool.invoke(search_query)
# print(search_results)