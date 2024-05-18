from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name):
    model = Prompt().load_model(model_name) 
    while True:
        user_input = input("Enter a story prompt (e.g., A young inventor stumbles upon a magical device): ")
        
        if user_input.lower() == 'end':
            print("Exiting ..")
            break

        output = model.prompt_main(user_input,
                                  prompt_name="generate_story",
                                  temperature=0.40)
        story = output["llm_response"].strip("\n")

        print("Story: ", story)

if __name__ == "__main__":
    model_name = "phi-3-gguf"
    generate_story_ideas(model_name)
