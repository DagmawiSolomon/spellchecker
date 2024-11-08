import tkinter as tk

window = tk.Tk()
window.configure(bg="#090A0B")
window.title("Spellchecker")
window.geometry("550x250")  

window.resizable(False, False)
entry = tk.Text(window, height=8, borderwidth=0, highlightthickness=0) 
entry.configure(bg="#121416", fg="#F1E3E4")
entry.pack(fill=tk.X, padx=10, pady=10)

button = tk.Button(
    window,
    text="Spellcheck",
    width=15,
    height=2,
    borderwidth=0,
    highlightthickness=0
)
button.configure(bg="#E65F5C", fg="#F1E3E4")
button.pack()

window.mainloop()
