class SearchResults:
    def __init__(self, results=None):
        self.results = results or []

    def filter_by_keyword(self, keyword):
        #Filter Articles by Keyword in the title or Abstract.
        return [article for article in self.results if keyword.lower() in article ['title'].lower()]    
    
    def get_titles(self):
        #Return a list of article titles.
        return [article['title'] for article in self.results]
    
    def get_abstracts(self):
        #Return a list of article abstracts.
        return [article.get('abstract', '') for article in self.results]