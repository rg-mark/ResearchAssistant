class Chatbot:
    def __init__(self, ieee_api, summarizer, article_manager):
        self.ieee_api = ieee_api
        self.summarizer = summarizer
        self.article_manager = article_manager

    def get_response(self, user_input):
        # Generate response based on user input.
        user_input = user_input.lower()
          # Check if the user is trying to search for articles
        if "search" in user_input or "find" in user_input:
            return self.search_articles(user_input)
        
        # Check if the user is asking to summarize an article
        elif "summarize" in user_input:
            return self.summarize_article(user_input)
        
        # Check if the user is asking to save an article
        elif "save" in user_input:
            return self.save_article(user_input)
        
        # Check if the user is asking for article recommendations
        elif "recommend" in user_input:
            return self.generate_recommendations(user_input)
        
        # If the input doesn't match any of the above, return a generic response
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"
        
    def search_articles(self, user_input):
        # Extract query for searching IEEE Xplore.
        query = user_input.replace("search", "").replace("find", "").strip()
        if not query:
            return "Please provide a search query."

        try:
            articles = self.ieee_api.fetch_articles(query)
            if articles:
                # Format and return the article list (top 5 results).
                return f"Found {len(articles)} articles. Here are the top 5 titles:\n" + "\n".join([article['title'] for article in articles[:5]])
            else:
                return "Sorry, no articles found for that query."
        except Exception as e:
            return f"An error occurred while searching for articles: {str(e)}"
    
    def summarize_article(self, user_input):
        article_id = user_input.replace("summarize", "").strip()
        if not article_id:
            return "Please provide a valid article ID to summarize."
        
        try:
            article = self.article_manager.load_article(article_id)
            if article:
                summary = self.summarizer.summarize_article(article['abstract'])
                return f"Summary: {summary}"
            else:
                return "Sorry, I couldn't find an article with that ID to summarize."
        except Exception as e:
            return f"An error occurred while retrieving the article: {str(e)}"

    def save_article(self, user_input):
        article_id = user_input.replace("save", "").strip()
        if not article_id:
            return "Please provide a valid article ID to save."
        
        try:
            articles = self.ieee_api.fetch_articles(article_id)
            if articles:
                self.article_manager.save_article(article_id, articles[0])  # Save the first article found
                return f"Article '{articles[0]['title']}' saved successfully."
            else:
                return "Sorry, I couldn't find an article with that ID to save."
        except Exception as e:
            return f"An error occurred while saving the article: {str(e)}"

    def generate_recommendations(self, user_input):
        article_id = user_input.replace("recommend", "").strip()
        if not article_id:
            return "Please provide a valid article ID to generate recommendations."
        
        try:
            article = self.article_manager.load_article(article_id)
            if article:
                recommendations = self.summarizer.generate_article_recommendations(article['title'], article['abstract'])
                return f"Recommended articles: {recommendations}"
            else:
                return "Sorry, I couldn't find an article with that ID to generate recommendations."
        except Exception as e:
            return f"An error occurred while generating recommendations: {str(e)}"    

