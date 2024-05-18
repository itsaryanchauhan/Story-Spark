from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name):
  model = Prompt().load_model(model_name)
  current_story = ""
  while True:
    # Initial story generation (run only once)
    if not current_story:
      genre = input("Enter story genre (e.g., fantasy, sci-fi): ")
      character = input("Describe the main character (briefly): Gove, a young technician. ")
      setting = input("Describe the story setting (briefly): The Rustbucket, an aging asteroid mining vessel. ")
      conflict = input("Describe the initial conflict the character faces: Gove discovers a strange anomaly within an asteroid. ")
  
      user_input = f"Write a {genre} story about {character} in {setting} facing the challenge of {conflict}. Make it suspenseful and character-driven. {current_story}"

    output = model.prompt_main(user_input,
                                prompt_name="generate_story",
                                temperature=0.7)
    story = output["llm_response"].strip("\n")
    current_story += story + "\n\n"

    # Print generated story with a separator
    print("*** Generated Story ***")
    print(current_story)
    print("*** End of Generated Story ***")

    user_feedback = input("Do you want to continue the story (y/n) or are you happy with this length? ")
    
    # Continue using the existing story for subsequent prompts
    if user_feedback.lower() == 'n':
      break
    else:
      user_input = f"What happens next in the story? {current_story}"

if __name__ == "__main__":
  model_name = "phi-3-gguf"
  generate_story_ideas(model_name)
