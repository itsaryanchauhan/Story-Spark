from llmware import LLMWare
import tkinter as tk

# Replace with your actual credentials
access_key = "YOUR_ACCESS_KEY"
secret_key = "YOUR_SECRET_KEY"

def generate_ideas(prompt, genre=None, keywords=[]):
  # Same logic as before for generating ideas
  # ...

def get_ideas():
  prompt_text = prompt_entry.get()
  genre_text = genre_entry.get()
  keywords_text = keywords_entry.get().split(",")  # Split comma-separated keywords
  ideas = generate_ideas(prompt_text, genre_text, keywords_text)
  idea_list.delete(0, tk.END)  # Clear existing ideas
  for idea in ideas:
    idea_list.insert(tk.END, idea)

# Initialize LLMWare connection
llmware = LLMWare(access_key=access_key, secret_key=secret_key)

# Create the main window
root = tk.Tk()
root.title("Creative Spark Generator")

# Prompt label and entry
prompt_label = tk.Label(root, text="Enter your creative prompt:")
prompt_label.pack()
prompt_entry = tk.Entry(root)
prompt_entry.pack()

# Genre label and entry (optional)
genre_label = tk.Label(root, text="Genre (optional):")
genre_label.pack()
genre_entry = tk.Entry(root)
genre_entry.pack()

# Keywords label and entry (optional)
keywords_label = tk.Label(root, text="Keywords (comma-separated, optional):")
keywords_label.pack()
keywords_entry = tk.Entry(root)
keywords_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Ideas", command=get_ideas)
generate_button.pack()

# Listbox to display ideas
idea_list = tk.Listbox(root)
idea_list.pack()

# Run the main event loop
root.mainloop()
