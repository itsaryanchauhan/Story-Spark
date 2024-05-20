from llmware.models import ModelCatalog
from llmware.prompts import Prompt
import sys

def generate_story_ideas(model_name, genre, character, setting, conflict):
  model = Prompt().load_model(model_name)
  current_story = ""

  user_input = f"Write a suspenseful and character-driven continuation of the story:\n{current_story}" \
              f"\nGenre: {genre}\nCharacter: {character}\nSetting: {setting}\nConflict: {conflict}"

  output = model.prompt_main(user_input, prompt_name="generate_story", temperature=0.7)
  story = output["llm_response"].strip("\n")

  current_story += story + "\n\n"

  return current_story

if __name__ == "__main__":
  model_name = "phi-3-gguf"
  genre = input("Enter story genre (e.g., fantasy, sci-fi): ")
  character = input("Describe the main character (briefly): ")
  setting = input("Describe the story setting (briefly): ")
  conflict = input("Describe the initial conflict the character faces: ")

  generated_story = generate_story_ideas(model_name, genre, character, setting, conflict)

  while True:
    print(generated_story)
    is_story_long_enough = input("Is the story length sufficient (y/n)? ")
    if is_story_long_enough.lower() == "y":
      break
    elif is_story_long_enough.lower() == "n":
      generated_story = generate_story_ideas(model_name, genre, character, setting, conflict)
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

  print("Thank you for using Story-Spark!")
  sys.exit()
