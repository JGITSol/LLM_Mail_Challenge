import tkinter as tk
from tkinter import ttk, messagebox
# MANUALLY TESTED, WORKING

# Define the models and their applicable methods
MODEL_METHODS = {
    "ChatGPT": [
        "CustomGPT (Guide)",
        "Custom Instructions (Guide)",
        "File Method (4o/4o Mini, Guide)",
        "Canvas Method",
        "o1 One Shot Smut Method"
    ],
    "Claude": [
        "Style Method (Best Option, Guide)",
        "Easiest Option (Perplexity Only)",
        "File Method (Claude.AI)"
    ],
    "Google Gemini": [
        "2.0 Flash Experimental Method (Temporary, Guide)",
        "AIStudio Filter Off Method",
        "Project Jailbreak GEM Method"
    ],
    "Mistral": [
        "Easiest Method: Override System Prompt"
    ],
    "Grok": [
        "Easiest Method: Override System Prompt"
    ],
    "DeepSeek": [
        "Upload Jailbreak Document"
    ],
    "Qwen": [
        "Upload Jailbreak Document (QwQ)",
        "System Prompt Jailbreak (Qwen2.5)"
    ],
    "Nova": [
        "System Prompt + Chat Combination",
        "Chat Prompts (Guide)"
    ]
}

def show_methods():
    """Display the applicable methods for the selected model."""
    selected_model = model_var.get()
    if not selected_model:
        messagebox.showwarning("Warning", "Please select a model!")
        return

    methods = MODEL_METHODS.get(selected_model, [])
    if not methods:
        messagebox.showinfo("Info", f"No methods available for {selected_model}.")
        return

    # Clear the methods listbox
    methods_listbox.delete(0, tk.END)

    # Add methods to the listbox
    for method in methods:
        methods_listbox.insert(tk.END, method)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("LLM Jailbreak Methods")
root.geometry("500x400")

# Dropdown label
label = tk.Label(root, text="Select a Model:", font=("Arial", 14))
label.pack(pady=10)

# Dropdown for models
model_var = tk.StringVar()
model_dropdown = ttk.Combobox(root, textvariable=model_var, state="readonly", font=("Arial", 12))
model_dropdown["values"] = list(MODEL_METHODS.keys())
model_dropdown.pack(pady=10)

# Button to display methods
show_methods_button = tk.Button(root, text="Show Methods", command=show_methods, font=("Arial", 12))
show_methods_button.pack(pady=10)

# Label for methods
methods_label = tk.Label(root, text="Applicable Methods:", font=("Arial", 14))
methods_label.pack(pady=10)

# Listbox to display methods
methods_listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12))
methods_listbox.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
