from llmware.models import ModelCatalog
from llmware.prompts import Prompt

# Function to generate story ideas
def generate_story_ideas(prompt, genre=None, keywords=[]):
  """
  Generates creative story ideas based on user input.

  Args:
    prompt: A string describing the desired story elements.
    genre: (Optional) A specific genre to focus on (e.g., sci-fi, fantasy).
    keywords: (Optional) A list of keywords to include in the generated ideas.

  Returns:
    A list of creative story ideas as strings.
  """
  # Combine prompt with genre and keywords if provided
  formatted_prompt = prompt
  if genre:
    formatted_prompt += f" in the genre of {genre}"
  if keywords:
    formatted_prompt += f"  including the keywords: {', '.join(keywords)}"

  # Load the appropriate model for story generation
  model_name = ModelCatalog.get_model_for_task("story_generation")

  # Use LLMWare to generate creative text formats
  model = Prompt().load_model(model_name)
  response = model.prompt_main(
      prompt=f"Generate a list of story ideas for {formatted_prompt}",
      format="list",
      num_items=5  # Change num_items to adjust the number of ideas generated
  )
  return response.splitlines()

# Example usage
prompt = "A young inventor stumbles upon a magical device."
ideas = generate_story_ideas(prompt, genre="fantasy", keywords=["friendship"])

print("Here are some story spark ideas for you:")
for idea in ideas:
  print(idea)
