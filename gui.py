import tkinter as tk
from spellchecker import SpellChecker

window = tk.Tk()
window.configure(bg="#090A0B")
window.title("Spellchecker")
window.geometry("550x250")  





window.resizable(False, False)
entry = tk.Text(window, height=8, borderwidth=0, highlightthickness=0) 
entry.configure(bg="#121416", fg="#F1E3E4")
entry.pack(fill=tk.X, padx=10, pady=10)

words = []
def on_button_press():
    content = entry.get("1.0", tk.END).strip()  
    words = content.split(" ")
    print(words)
       


button = tk.Button(
    window,
    text="Spellcheck",
    width=15,
    height=2,
    borderwidth=0,
    highlightthickness=0,
    command=on_button_press
)
button.configure(bg="#E65F5C", fg="#F1E3E4")
button.pack()



# tooltip on hover
# red squiggly lines

window.mainloop()
