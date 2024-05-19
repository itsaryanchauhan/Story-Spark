from flask import Flask, request, jsonify
from story_generator import generate_story_ideas  # Import the generate_story_ideas function

app = Flask(__name__)

@app.route('/')
def root():
    """Returns a welcome message and instructions for using the app."""
    return jsonify({
        'message': 'Welcome to the Story Generator!',
        'instructions': 'To generate a story, please send a POST request to the /generate_story endpoint with the following JSON data in the request body:',
        'data_fields': {
            'genre': 'The genre of your story (e.g., fantasy, sci-fi)',
            'character': 'A description of your main character',
            'setting': 'The setting of your story',
            'conflict': 'The initial conflict your character faces'
        }
    })

@app.route('/generate_story', methods=['POST'])
def generate_story_api():
    """Generates a story based on user input received as JSON."""

    # Extract user input from the request body
    try:
        user_input = request.json
        genre = user_input.get('genre')
        character = user_input.get('character')
        setting = user_input.get('setting')
        conflict = user_input.get('conflict')
    except (KeyError, TypeError) as e:
        return jsonify({'error': f'Invalid JSON data: {e}'}), 400

    # Validate required input fields
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
