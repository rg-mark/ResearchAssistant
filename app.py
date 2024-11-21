import os
from models.ieee import IEEE_Xplore
from models.summarizer import ArticleSummarizer
from models.article_manager import ArticleManager
from models.search import SearchResults
from models.interaction import Chatbot
from transformers import T5Tokenizer
from transformers import logging
from transformers import T5ForConditionalGeneration

logging.set_verbosity_info()

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def main():
    api_key = os.getenv("IEEE_API_KEY")
    if not api_key:
        print ("Error: API key not found.")
    ieee_api = IEEE_Xplore(api_key)
    summarizer = ArticleSummarizer()
    article_manager = ArticleManager()

    #Initialize chatbot
    chatbot = Chatbot(ieee_api, summarizer, article_manager)

    print("Welcome to the IEEE Xplore Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        #Get chatbot response
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()