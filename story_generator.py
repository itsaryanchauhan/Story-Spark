from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name, genre, character, setting, conflict):
    model = Prompt().load_model(model_name)
    current_story = ""
    continue_story = True

    while continue_story:
        user_input = f"Write a suspenseful and character-driven continuation of the story:\n{current_story}" \
                     f"\nGenre: {genre}\nCharacter: {character}\nSetting: {setting}\nConflict: {conflict}"

        output = model.prompt_main(user_input, prompt_name="generate_story", temperature=0.7)
        story = output["llm_response"].strip("\n")
        current_story += story + "\n\n"

        user_decision = input("Is the story length sufficient? (y/n): ")
        if user_decision.lower() == 'y':
            continue_story = False

    return current_story

if __name__ == "__main__":
    model_name = "phi-3-gguf"
    genre = input("Enter story genre (e.g., fantasy, sci-fi): ")
    character = input("Describe the main character (briefly): ")
    setting = input("Describe the story setting (briefly): ")
    conflict = input("Describe the initial conflict the character faces: ")
    print(generate_story_ideas(model_name, genre, character, setting, conflict))
