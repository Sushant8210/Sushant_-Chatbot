import requests
from bs4 import BeautifulSoup
import re

url = "https://www.lifehack.org"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def get_content(soup):
    content = []
    for article in soup.find_all('article'):
        text = article.get_text()
        # Clean the text data
        text = re.sub(r'\s+', ' ', text)
        content.append(text)
    return content

blog_content = get_content(soup)
print(blog_content)
import spacy 

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


# Process blog content with NLP
for text in blog_content:
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.label_)  # Entity and its type (e.g., 'PRODUCT', 'ORG', etc.)
class ChatBot:
    def __init__(self):
        self.context = {}

    def get_response(self, user_input):
        if 'article' in user_input.lower():
            return self.ask_article_topic()
        elif 'recommendation' in user_input.lower():
            return self.ask_recommendation_type()
        else:
            return "I'm here to help. Could you please provide more details?"

    def ask_article_topic(self):
        return "What topic are you interested in? E.g., technology, health, travel."

    def ask_recommendation_type(self):
        return "Would you like article recommendations, or something else?"

bot = ChatBot()
print(bot.get_response("Can you recommend an article?"))
print(bot.get_response("What topics are available?"))
