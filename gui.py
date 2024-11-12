import tkinter as tk

window = tk.Tk()
window.configure(bg="#090A0B")
window.title("Spellchecker")
window.geometry("550x250")  





window.resizable(False, False)
entry = tk.Text(window, height=8, borderwidth=0, highlightthickness=0) 
entry.configure(bg="#121416", fg="#F1E3E4")
def on_space_press(event):
    content = entry.get("1.0", tk.END).strip()  
    print("Text after space bar press:")
    print(content)
entry.bind("<space>", on_space_press)
entry.pack(fill=tk.X, padx=10, pady=10)




window.mainloop()
