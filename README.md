Summary

I created this program to help out fellow college students like myself quickly get information they need from large textbooks. The use of this program is to take a textbook provided by the user and use OpenAI in order to summarize the desired parts of the textbook and gives the user an oppurtunity to ask questions as well. First the program will make the textbook into a form that python is able to read. Then the user will provide the pages that they want information on. After the program accesess the specific pages the user will be able to ask questions about the contents of those pages. The program takes each question asked and adds it to the conversation history, so the user is able to have a full conversation with the OpenAI. After the user has finished asking questions they can use the escape option provided to end the program.


Implemenatation

First enter your OpenAi key and the pathway to where your textbook is saved on your computer. Then when you run the program input the range of pages you would like information on. You then will be able to have a conversation with GPT about these pages in order to obtain the information you needed. Once you are done asking questions, type exit to end the program.


Imports

You need to import openai and from PyPDF2 import PdfReader
