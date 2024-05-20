# story_generator.py
from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name, genre, character, setting, conflict, continue_story=False, current_story=""):
    model = Prompt().load_model(model_name)
    if not continue_story:
        current_story = ""

    user_input = f"Write a suspenseful and character-driven continuation of the story:\n{current_story}" \
                 f"\nGenre: {genre}\nCharacter: {character}\nSetting: {setting}\nConflict: {conflict}"

    output = model.prompt_main(user_input, prompt_name="generate_story", temperature=0.7)
    story = output["llm_response"].strip("\n")
    current_story += story + "\n\n"

    return current_story
