# Textbook-Analysis-with-GPT
Summary

I created this program to help out fellow college students like myself quickly get information they need from large textbooks. The use of this program is to take a textbook provided by the user and use OpenAI in order to summarize the desired parts of the textbook and gives the user an oppurtunity to have a conversation with a chatbot created to answer their questions. First the program will make the textbook into a form that python is able to read. Then the user will provide the pages that they want information on, once the pages are inputted a link to a user interface will be provided. Each question that is asked will be added to the conversation history so the user will be able to have a full conversation with the chatbot to get all the information they need from their textbook.


Implemenatation

First enter your OpenAi key and the pathway to where your textbook is saved on your computer. Then when you run the program input the range of pages you would like information on. You then will be able to have a conversation with GPT chatbot about these pages in order to obtain the information you needed. Once you are done asking questions, you can close the chatbot.


Imports

import openai, from PyPDF2 import PdfReader, import gradio as gr
