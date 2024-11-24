import cohere
import pandas as pd
import time

co = cohere.ClientV2(
    api_key="wHTzipjDKS7rkm4LkIp0ryuOFBmwzmjvpDQneGlC",
)

def generate_text_input(message):
    # Generate the response by streaming it
    bot_response = ""
    response = co.chat_stream(model="command-r-plus-08-2024",
                              messages=chat_log_input,
                              max_tokens=30,
                              temperature=0.5,
                              k=0,
                              p=0.9
                              )
    for event in response:
        if event.type == "content-delta":
            bot_response += event.delta.message.content.text
    return bot_response
        
def generate_text_output(message):
    # Generate the response by streaming it
    bot_response = ""
    response = co.chat_stream(model="command-r-plus-08-2024",
                              messages=chat_log_output,
                              max_tokens=24,
                              temperature=0.5,
                              k=0,
                              p=0.9
                              )
    for event in response:
        if event.type == "content-delta":
            bot_response += event.delta.message.content.text
    return bot_response

#---------------------------------------#

# Load the original data
data = pd.read_json('prompts.jsonl', lines=True)

# Extract the 'User' and 'Chatbot' messages
input_output_pairs = []
for index, row in data.iterrows():
    user_message = row["messages"][1]['content']
    chatbot_message = row["messages"][2]['content']
    input_output_pairs.append({'Input': user_message, 'Output': chatbot_message})

# Create a DataFrame with the extracted messages
input_output_df = pd.DataFrame(input_output_pairs)


system_preset_input = """## Task and Context
Reword the input as a message from a very straight-forward customer who is inquiring about car characteristics for their requirements. Always mention your requirements. Very important sentences must be under 100 characters. 
"""
system_preset_output = """## Task and Context
Reword the input as a message from a friendly, straight forward salesman would give to a customer about a car. Mention the model you recommend with information related to the customers inquiries. Very important sentences must be under 100 characters.
"""

# Print the resulting DataFrame
print(input_output_df.head())
i = 0
counter = 0

for index, row in data.iterrows():
    if i <= 4:
        chat_log_input = [{'role': 'system', 'content': system_preset_input}] #getting the chat history
        chat_log_output = [{'role': 'system', 'content': system_preset_output}]

        input_message = data.at[index, 'messages'][1]['content'] #getting the string messages of each
        output_message = data.at[index, 'messages'][2]['content']

        chat_log_input.append({'role': 'user', 'content': input_message}) #getting into a chat history
        chat_log_output.append({'role': 'user', 'content': output_message})

        data.at[index, 'messages'][1]['content'] = generate_text_input(data.at[index, 'messages'][1]['content'])
        data.at[index, 'messages'][2]['content'] = generate_text_output(data.at[index, 'messages'][1]['content'])
        
        i += 1
        counter += 1
        print(f'Currently at the {counter}th iteration')

    else:
        time.sleep(60) #wait 60s because we have the free version. Limited to 40 API calls per minute
        i = 0

# Save the updated DataFrame to a new JSONL file
data.to_json('updated_prompts.jsonl', orient='records', lines=True)