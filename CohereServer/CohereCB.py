import cohere

co = cohere.ClientV2(
    api_key="EsKtqXFZyqTucUpb66KxyQ0lSZzN8kforHVAnJko",
)

system_preset = """ ## Task and Context
    An Assistant for the company Matador with knowledge on the companies dataset of 2230 cars classified as follows:
    - Type, Stock, VIN, Year, Make, Model, Body, ModelNumber, Doors, ExteriorColor,
      InteriorColor, EngineCylinders, EngineDisplacement, Transmission, Miles, SellingPrice, 
      MSRP, BookValue, Invoice, Certified, Options, Style_Description, Ext_Color_Generic, 
      Ext_Color_Code, Int_Color_Generic, Int_Color_Code, Int_Upholstery, Engine_Block_Type, 
      Engine_Aspiration_Type, Engine_Description, Transmission_Speed, Transmission_Description, 
      Drivetrain, Fuel_Type, CityMPG, HighwayMPG, EPAClassification, Wheelbase_Code, Internet_Price, 
      MarketClass, PassengerCapacity, ExtColorHexCode, IntColorHexCode, EngineDisplacementCubicInches.
      The user will specify preferences, and you should match them as closely as possible with cars in the dataset.
      If exact matches are unavailable, provide alternative cars in the dataset. Be concise and friendly! Remember to give the model not the stock
"""

chat_log = [{'role': 'system', 'content': system_preset}]


def generate_text(user_message):
    # Generate the response by streaming it
    bot_response = ""
    response = co.chat_stream(model="0e7a4366-cf7d-4bd9-8a99-e9f0c9667bdc-ft",
                              messages = chat_log,
                              max_tokens=128,
                              temperature=0.7,
                              k=0,
                              p=0.9
                              )
    
    for event in response:
        if event.type == "content-delta":
            bot_response += event.delta.message.content.text
            print(event.delta.message.content.text, end='')

    chat_log.append({'role': 'Chatbot', 'content': bot_response})

def main():
    while True:
        if len(chat_log) == 1:
            start = "Hi! I am your Matador virtual assistant for today, how can I help you?"

        message = input("You: ")
        chat_log.append({"role": "user", "content": message})

        if message == "exit":
            print("Goodbye!")
            break

        bot_response = generate_text(message)
        return bot_response

main()