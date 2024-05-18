from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name):
  model = Prompt().load_model(model_name)
  while True:
    genre = input("Enter story genre (e.g., fantasy, sci-fi): ")
    character = input("Describe the main character (briefly): ")
    setting = input("Describe the story setting (briefly): ")
    user_input = f"Write a {genre} story about {character} in {setting}. Make it suspenseful and character-driven. Here are some story elements you can consider including: [List specific elements if desired]"

    if user_input.lower() == 'end':
      print("Exiting ..")
      break

    output = model.prompt_main(user_input,
                                prompt_name="generate_story",
                                temperature=0.6)
    story = output["llm_response"].strip("\n")

    print("Story: ", story)
    user_feedback = input("Do you like this story (y/n)? ")
    if user_feedback.lower() == 'y':
      break
    else:
      print("Try refining the prompt based on your preferences.")

if __name__ == "__main__":
  model_name = "phi-3-gguf"
  generate_story_ideas(model_name)
