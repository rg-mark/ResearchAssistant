
# Intelligent Research Assistant

The **Intelligent Research Assistant** is a modular and extensible application designed to simplify research workflows by retrieving, summarizing, and presenting information. Its architecture allows seamless integration of APIs and tools, making it a valuable asset for academics, professionals, and enthusiasts.


## Project Structure

```plaintext
intelligent_research_assistant/
├── data/ articles                     # Store Articles after retrieval
├── models/
│   ├── article_manager.py    # Transforms retreived document into PDF.
│   ├── ieee.py               # Fetches Article data
│   ├── interaction.py        # Handles user input and output  
│   ├── search.py             # Handles searches
│   ├── summarizer.py         # Summarizes fetched data

├── modules/

├── static/                   # Frontend (if using Flask)
├── templates/                # HTML templates (if using Flask)
├── tests/                    
│   ├── api_test.py           # Tests whether the API works.
├── app.py                    # Main script to run the app
└── README.md                 # Documentation
