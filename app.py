from flask import Flask, render_template, request, jsonify
from story_generator import generate_story_ideas

app = Flask(__name__)

# Route for the main page (/)
@app.route('/')
def index():
    return render_template('index.html')  # This assumes you have an index.html file in your templates directory

# Route for handling form submissions (/generate_story)
@app.route('/generate_story', methods=['POST'])
def generate_story():
    # Access user input from the form
    data = request.json
    genre = data['genre']
    character = data['character']
    setting = data['setting']
    conflict = data['conflict']

    # Call the generate_story_ideas function with user input
    generated_story = generate_story_ideas(model_name="phi-3-gguf", genre=genre, character=character, setting=setting, conflict=conflict)

    # Return the generated story as a JSON response
    return jsonify({'generated_story': generated_story})

# Run the Flask development server (optional for this example)
if __name__ == '__main__':
    app.run(debug=True)
