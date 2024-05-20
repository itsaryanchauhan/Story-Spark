from flask import Flask, render_template, request, jsonify
from story_generator import generate_story_ideas

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.get_json()
    genre = data['genre']
    character = data['character']
    setting = data['setting']
    conflict = data['conflict']

    generated_story = generate_story_ideas(model_name="phi-3-gguf", genre=genre, character=character, setting=setting, conflict=conflict)

    return jsonify({'generated_story': generated_story})

if __name__ == '__main__':
    app.run(debug=True)
