# story_generator.py
from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name, genre, character, setting, conflict):
    model = Prompt().load_model(model_name)
    current_story = ""
    user_input = f"Write a suspenseful and character-driven story:\n" \
                 f"Genre: {genre}\nCharacter: {character}\nSetting: {setting}\nConflict: {conflict}"

    output = model.prompt_main(user_input, prompt_name="generate_story", temperature=0.7)
    story = output["llm_response"].strip("\n")
    current_story += story + "\n\n"

    return current_story
