import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.iconbitmap('../assets/icon.ico')
root.title('Калькулятор')

def insert_value():
    pass

def init():
    flame_top = tk.Frame(root, width=500, height=100, bg='grey')
    flame_bottom_left = tk.Frame(root, width=350, height=100, bg='grey' )
    flame_bottom_right = tk.Frame(root, width=150, height=100, bg='grey')
    return [flame_top.pack(side="top"), flame_bottom_left.pack(side="bottom"), flame_bottom_right.pack(side="bottom")]

def gui():
    frame_bottom_left = init()
    for button in range(10):
        button = tk.Button(root, text='button', command=insert_value)
        button.pack()

gui()
