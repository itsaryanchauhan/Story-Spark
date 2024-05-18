from llmware.models import ModelCatalog
from llmware.prompts import Prompt


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
  model_name = "bling-phi-3-gguf"

  # Use LLMWare to generate creative text formats
  model = Prompt().load_model(model_name)
  response = model.prompt_main(
    prompt=f"Generate a list of story ideas for {formatted_prompt}",
    # Remove format="list" argument
    #num_items=5  # Change num_items to adjust the number of ideas generated
)
  return response.splitlines()


def main():
  # Get user input for story prompt
  prompt = input("Enter a story prompt (e.g., A young inventor stumbles upon a magical device): ")

  # Get user input for genre (optional)
  genre = input("Enter a genre (optional): ")
  if genre.lower() == "skip":
    genre = None  # Set genre to None if user skips

  # Get user input for keywords (optional)
  keywords = []
  while True:
    keyword = input("Enter a keyword (or 'done' to finish): ")
    if keyword.lower() == "done":
      break
    keywords.append(keyword)

  # Generate story ideas
  ideas = generate_story_ideas(prompt, genre, keywords)

  # Print the generated ideas
  print("Story Ideas:")
  for idea in ideas:
    print(idea)


if __name__ == "__main__":
  main()
