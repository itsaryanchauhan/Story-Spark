from llmware import LLMWare

# Initialize LLMWare connection (replace with your actual credentials)
llmware = LLMWare(access_key="YOUR_ACCESS_KEY", secret_key="YOUR_ SECRET_KEY")

def generate_ideas(prompt, genre=None, keywords=[]):
  """
  Generates creative ideas based on user input.

  Args:
    prompt: A string describing the creative project or area where ideas are needed.
    genre: (Optional) A specific genre to focus on (e.g., sci-fi, fantasy).
    keywords: (Optional) A list of keywords to include in the generated ideas.

  Returns:
    A list of creative ideas as strings.
  """
  # Combine prompt with genre and keywords if provided
  formatted_prompt = prompt
  if genre:
    formatted_prompt += f" in the genre of {genre}"
  if keywords:
    formatted_prompt += f"  including the keywords: {', '.join(keywords)}"

  # Use LLMWare to generate creative text formats  
  response = llmware.generate_text(
      prompt=f"Generate a list of creative ideas for {formatted_prompt}",
      format="list",
      num_items=5  # Change num_items to adjust the number of ideas generated
  )
  return response.splitlines()

# Example usage
prompt = "I'm writing a children's story about a talking animal."
ideas = generate_ideas(prompt, genre="fantasy", keywords=["friendship", "adventure"])

print("Here are some creative spark ideas for your story:")
for idea in ideas:
  print(idea)
