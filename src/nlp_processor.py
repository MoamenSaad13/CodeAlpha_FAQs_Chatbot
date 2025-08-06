
import json
import spacy
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class NLPProcessor:
    def __init__(self, faqs_file="faqs.json"):
        self.nlp = spacy.load("en_core_web_sm")
        # Get the absolute path to the faqs.json file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        faqs_path = os.path.join(current_dir, faqs_file)
        self.faqs = self._load_faqs(faqs_path)
        self.vectorizer = TfidfVectorizer()
        self.faq_vectors = self._vectorize_faqs()

    def _load_faqs(self, faqs_file):
        with open(faqs_file, 'r') as f:
            return json.load(f)

    def _preprocess_text(self, text):
        doc = self.nlp(text.lower())
        return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

    def _vectorize_faqs(self):
        preprocessed_questions = [self._preprocess_text(faq['question']) for faq in self.faqs]
        return self.vectorizer.fit_transform(preprocessed_questions)

    def get_best_match(self, user_question):
        preprocessed_user_question = self._preprocess_text(user_question)
        user_question_vector = self.vectorizer.transform([preprocessed_user_question])
        similarities = cosine_similarity(user_question_vector, self.faq_vectors)
        best_match_index = similarities.argmax()
        return self.faqs[best_match_index]['answer']

if __name__ == '__main__':
    processor = NLPProcessor()
    while True:
        user_input = input("Ask a question: ")
        if user_input.lower() == 'exit':
            break
        answer = processor.get_best_match(user_input)
        print(f"Chatbot: {answer}")


