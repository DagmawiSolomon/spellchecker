import tkinter as tk


window = tk.Tk()
window.title("Spellchecker")
window.geometry("550x250")  


entry = tk.Text(window, height=8) 
entry.pack(fill=tk.X, padx=10, pady=10)
button = tk.Button(
    window,
    text="Spellcheck",
    width=10,
    height=2,
)
button.pack()
window.mainloop()
