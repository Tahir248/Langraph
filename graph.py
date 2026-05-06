from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()  # Ye command khud hi .env file se keys utha legi

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite-preview",
    temperature=0.7  # Ye AI ko thora natural aur conversational banayega
)

# 1. State define karein (ye data nodes ke beech share hoga)
class GraphState(TypedDict):
    state: str


def router_function(state: GraphState):
    print("---Router Function Running---", state)
    if "am" in state["state"].lower():
        return "yes"
    return "no"


# 2. Nodes ke functions banayein
def node1(current_state: GraphState):
    print("---Node 1 Running---")
    input_text = current_state["state"]

    response = model.invoke(f"User said '{input_text}'. Just contate 'i am' after user text.")

    # Purane state mein " i am" jorein
    # return {"state": response.content}
    return {"state": input_text + "i am"}

def node2(current_state: GraphState):
    print("---Node 2 Running---")
    input_text = current_state["state"]

    response = model.invoke(f"User said '{input_text}'. Just contate ' happyyyyyyyyyyyyyyyyyyyyyyyyyy' after user text,  but improve the spelling as well.")

    # Purane state mein " happy" jodein
    return {"state": response.content}

# 3. Graph build karein
workflow = StateGraph(GraphState)

# Nodes add karein
workflow.add_node("node1", node1)
workflow.add_node("node2", node2)

# Edges (Raaste) connect karein
workflow.add_edge(START, "node1")
workflow.add_conditional_edges("node1", router_function, {
        "yes": "node2", 
        "no": END
    })
workflow.add_edge("node2", END)

# Graph compile karein
app = workflow.compile()

# 4. Run karein
initial_input = {"state": "hellooooooooooooooooooo"}
result = app.invoke(initial_input)

print("\nFinal Output:", result["state"])
