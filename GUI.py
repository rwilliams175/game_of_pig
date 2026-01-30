import tkinter as tk

def say_hi():
    label.config(text = "You clicked the button...")
def unclick():
    label.config(text = "Hello, TKinter")
#create the main window
root = tk.Tk()
root.title("My First TKinter Project")
root.geometry("400x300")

label = tk.Label(root, text = "Hello, TKinter")
label.pack()

button = tk.Button(root, text = "Don't click me!", command = say_hi)
button.pack()
unclick_button = tk.Button(root, text = "Wanna retry?", command = unclick)
unclick_button.pack()

#runs the program above
root.mainloop()