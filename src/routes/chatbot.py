from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from src.nlp_processor import NLPProcessor

chatbot_bp = Blueprint('chatbot', __name__)

# Initialize the NLP processor
nlp_processor = NLPProcessor()

@chatbot_bp.route('/ask', methods=['POST'])
@cross_origin()
def ask_question():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'Question is required'}), 400
        
        user_question = data['question']
        answer = nlp_processor.get_best_match(user_question)
        
        return jsonify({
            'question': user_question,
            'answer': answer
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

