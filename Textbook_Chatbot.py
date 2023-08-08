import openai
from PyPDF2 import PdfReader
import gradio as gr

openai.api_key = 'Enter your API key'


def extract_text_from_pdf(pdf_path, start_page, end_page):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in range(start_page - 1, min(end_page, len(reader.pages))):
            text += reader.pages[page].extract_text()
    return text


def preprocess_text(text):
    # Add your text preprocessing steps here (e.g., removing unwanted characters, formatting)
    if text is None:
        return ""
    else:
        return text


def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Select the appropriate engine
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()


# Example conversation loop
print("Chat with OpenAI:")
print("You can start the conversation by typing a message. Enter 'exit' to quit.")

pdf_path = 'Enter your PDF path'  # Specify the correct PDF path
start_page = int(input("Enter the start page number: "))
end_page = int(input("Enter the end page number: "))

text = extract_text_from_pdf(pdf_path, start_page, end_page)
preprocessed_text = preprocess_text(text)

conversation_history = []


# Function to handle chatbot responses
def chatbot_response(input_message):
    if input_message.lower() == 'exit':
        return "Chat ended."

    conversation_history.append(f"User: {input_message}")
    prompt = preprocessed_text + "\n" + "\n".join(conversation_history)

    response = generate_response(prompt)
    conversation_history.append(f"OpenAI: {response}")
    return response


# Gradio Interface
iface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="User: Your message..."),
    outputs=gr.Textbox(),
    title="OpenAI Textbook Summarizer Chatbot"  # Set the title of the interface here
)

iface.launch()
