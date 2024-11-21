from transformers import T5Tokenizer, T5ForConditionalGeneration

class ArticleSummarizer:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
        self.model = T5ForConditionalGeneration.from_pretrained("t5-small")

    def summarize(self, text):
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
