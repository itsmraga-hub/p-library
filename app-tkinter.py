import tkinter as tk
from PIL import ImageTk, Image


def load_frame1():
    frame1.pack_propagate(False)    

    logo_image = Image.open("assets/unsplash-tree.jpg")
    fixed_width = 300
    fixed_height = 200
    resized_logo_image = logo_image.resize((fixed_width, fixed_height))

    logo_img = ImageTk.PhotoImage(resized_logo_image)
    # logo_img = ImageTk.PhotoImage(file="assets/unsplash-tree.jpg")

    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack(pady=50)

    tk.Label(
        frame1,
        text='Welcome to P-Library',
        bg=bg_color,
        fg="white",
        font=("TkMenuFont", 14)
    ).pack(pady=20)

    tk.Button(frame1,
              text="Log in",
              bg="#28393a",
              fg="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              command=lambda: load_frame2()).pack()


def load_frame2():
    print("William")


bg_color = "#3d6466"
root = tk.Tk()
root.title("P-Library")  # title
root.eval("tk::PlaceWindow . center")  # Place at center

frame1 = tk.Frame(root, width=720, height=480, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)

for frame in (frame1, frame2):
  frame.grid(row=0, column=0)

load_frame1()

root.mainloop()
