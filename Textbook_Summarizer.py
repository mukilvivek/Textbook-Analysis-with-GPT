import openai
from PyPDF2 import PdfReader

openai.api_key = 'enter your openai key'


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
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()


# Example conversation loop
print("Chat with OpenAI:")
print("You can start the conversation by typing a message. Enter 'exit' to quit.")

pdf_path = 'enter your pdf path'  # Specify the correct PDF path
start_page = int(input("Enter the start page number: "))
end_page = int(input("Enter the end page number: "))

text = extract_text_from_pdf(pdf_path, start_page, end_page)
preprocessed_text = preprocess_text(text)

conversation_history = []

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chat ended.")
        break

    conversation_history.append(f"User: {user_input}")
    prompt = preprocessed_text + "\n" + "\n".join(conversation_history)

    response = generate_response(prompt)
    print("OpenAI:", response)

    # Add OpenAI's response to the conversation history
    conversation_history.append(f"OpenAI: {response}")