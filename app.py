from flask import Flask, request, jsonify
from story_generator import generate_story_ideas  # Import the generate_story_ideas function

app = Flask(__name__)

@app.route('/generate_story', methods=['POST'])
def generate_story_api():
  # Receive user input from the request body
  user_input = request.json

  # Extract user input data
  genre = user_input.get('genre')
  character = user_input.get('character')
  setting = user_input.get('setting')
  conflict = user_input.get('conflict')

  # Validate input (optional)
  if not all([genre, character, setting, conflict]):
    return jsonify({'error': 'Missing required input fields'}), 400

  # Generate story using the function from story_generator.py
  generated_story = generate_story_ideas(model_name="phi-3-gguf",  # Replace with your model name
                                           genre=genre,
                                           character=character,
                                           setting=setting,
                                           conflict=conflict)

  # Return generated story as JSON
  return jsonify({'generated_story': generated_story})

if __name__ == '__main__':
  app.run(debug=True)
