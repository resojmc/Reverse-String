import tkinter as tk

root = tk.Tk()
root.geometry("300x600")
root.title("Reverse String")

def reverse_str(s):
    s = str(s)
    s = s[::-1]
    return s
    
def update_str():
    string = top_entry.get()
    string = reverse_str(string)
    result_label.config(text=f"Result: {string}")

top_label = tk.Label(root, text="Input String")
top_label.pack()

top_entry = tk.Entry(root, )
top_entry.pack()

button = tk.Button(root, text="Go", command=update_str)
button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()