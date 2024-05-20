from flask import Flask, render_template, request
# Assuming your existing code (generate_story_ideas) is in a file named story_generator.py

# Import the generate_story_ideas function
from story_generator import generate_story_ideas

app = Flask(__name__)

# Route for the main page (/)
@app.route('/')
def index():
  return render_template('index.html') # This assumes you have an index.html file in your templates directory

# Route for handling form submissions (/generate_story)
@app.route('/generate_story', methods=['POST'])
def generate_story():
  # Access user input from the form
  genre = request.form['genre']
  character = request.form['character']
  setting = request.form['setting']
  conflict = request.form['conflict']

  # Call the generate_story_ideas function with user input
  generated_story = generate_story_ideas(model_name="phi-3-gguf", genre=genre, character=character, setting=setting, conflict=conflict)

  # Pass the generated story to the template for display (modified line)
  return render_template('story.html', generated_story=generated_story)

# Run the Flask development server (optional for this example)
if __name__ == '__main__':
  app.run(debug=True)
