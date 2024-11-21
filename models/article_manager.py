import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ArticleManager:
    def __init__(self, storage_dir='data/articles'):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def save_article(self, article_id, article_data):
        #Save Article data to PDF file.
        file_path = os.path.join(self.storage_dir, f"{article_id}.pdf")     

        # Create a PDF document
        c = canvas.canvas(file_path, pagesize=letter)
        
        #Title and Author
        c.setFont("Helvetica-Bold", 14)
        c.drawString(72, 750, f"Title: {article_data.get('title', 'No Title')}")
        c.setFont("Helvetica", 12)
        c.drawString(72, 730, f"Author(s): {', '.join(article_data.get('authors', ['Unknown']))}")

        #Abstract
        c.setFont("Helvetica-Bold", 12)
        c.drawString(72, 700, "Abstract:")
        c.setFont("Helvetica", 10)
        y_position = 680
        abstract = article_data.get('abstract', 'No abstract available.')
        for line in abstract.split('\n'):
            c.drawString(72, y_position, line)
            y_position -= 12
        
        # Save the PDF
        c.save()

    def load_article(self, article_id):
        """Load article data from a PDF file (Note: This would require PDF parsing, handled differently)."""
        # Loading a PDF is non-trivial and requires a library like PyPDF2 or PDFMiner.
        # Here we are assuming the load function isn't needed since we're focusing on saving PDFs.
        return None