from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from Ken.cars import cars

# Summarize or provide instructions for the dataset
DATASET_INSTRUCTIONS = """
The dataset contains 2230 cars with these attributes:
- Type, Stock, VIN, Year, Make, Model, Body, ModelNumber, Doors, ExteriorColor, InteriorColor, EngineCylinders, EngineDisplacement, Transmission, Miles, SellingPrice, MSRP, BookValue, Invoice, Certified, Options, Style_Description, Ext_Color_Generic, Ext_Color_Code, Int_Color_Generic, Int_Color_Code, Int_Upholstery, Engine_Block_Type, Engine_Aspiration_Type, Engine_Description, Transmission_Speed, Transmission_Description, Drivetrain, Fuel_Type, CityMPG, HighwayMPG, EPAClassification, Wheelbase_Code, Internet_Price, MarketClass, PassengerCapacity, ExtColorHexCode, IntColorHexCode, EngineDisplacementCubicInches.
The user will specify preferences, and you should match them as closely as possible with cars in the dataset. If exact matches are unavailable, provide alternative cars in the dataset.
"""
DATASET = cars

# LLM and chain setup
model = OllamaLLM(model="llama3.2:1b")
template = """
Answer the question below or help the user find a car using the provided dataset instructions.

Datasetinstructions: {datasetinstructions}
Dataset: {dataset}
Conversation History: {context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def filter_context(context, max_length=1000):
    """Truncate the context if it exceeds a certain token limit."""
    return context[-max_length:] if len(context) > max_length else context

def handle_conversation():
    context = ""  # Start with an empty conversation history
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Invoke the LLM with the dataset instructions, current context, and user query
        inputs = {
            "dataset": DATASET,
            "datasetinstructions": DATASET_INSTRUCTIONS,
            "context": context,
            "question": user_input,
        }
        try:
            result = chain.invoke(inputs)
            if isinstance(result, dict) and "text" in result:
                response = result["text"]
            else:
                response = str(result)
        except Exception as e:
            response = f"Error: {str(e)}"

        print("Bot: ", response)

        # Update context and ensure it doesn't bloat
        context += f"\nUser: {user_input}\nAI: {response}"
        context = filter_context(context)  # Truncate if necessary

if __name__ == "__main__":
    handle_conversation()