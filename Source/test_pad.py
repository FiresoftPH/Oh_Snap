import customtkinter
from PIL import Image, ImageTk
app = customtkinter.CTk()
app.geometry("1280x800")

frame = customtkinter.CTkFrame(master = app,
                               width = 1280,
                               height = 800)

frame.pack()

bg = Image.open("Pictures/BG_PG1.png")
bg_picture = ImageTk.PhotoImage(bg)

bg = customtkinter.CTkLabel(master = app,
                            image = bg_picture)

trans = Image.open("Pictures/BG_PG1.png")
trans_picture = ImageTk.PhotoImage(trans)

layer = customtkinter.CTkLabel(master = frame,
                               image = trans_picture)

arrow = Image.open("Pictures/Bond/Green Bond.png")
arrow_resize = arrow.resize((428, 450))
arrow_picture = ImageTk.BitmapImage(arrow_resize)

button = customtkinter.CTkButton(master = frame,
                                 image = arrow_picture,
                                 text = "",
                                 fg_color = "#E7D1FF",
                                 bg_color = "#E7D1FF",

                                 width = 90,
                                 height = 90,
                                 corner_radius = 1000)

button.place(x = 100, y = 100)
layer.place(x = 0, y = 0)

app.mainloop()