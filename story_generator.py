# story_generator.py
from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name, genre, character, setting, conflict):
    model = Prompt().load_model(model_name)
    current_story = ""
    iterations = 10  # Set the number of iterations to generate longer content

    for _ in range(iterations):
        user_input = f"Write a suspenseful and character-driven continuation of the story:\n{current_story}" \
                     f"\nGenre: {genre}\nCharacter: {character}\nSetting: {setting}\nConflict: {conflict}"

        output = model.prompt_main(user_input, prompt_name="generate_story", temperature=0.7)
        story_segment = output["llm_response"].strip("\n")
        current_story += story_segment + "\n\n"

    return current_story
