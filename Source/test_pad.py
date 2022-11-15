import customtkinter

window = customtkinter.CTk()

frame_1 = customtkinter.CTkFrame(master = window,
                                 width = 100,
                                 height = 100,
                                 fg_color = "Green"
                                 )

frame_2 = customtkinter.CTkFrame(master = frame_1,
                                 width = 50,
                                 height = 50,
                                 fg_color = "Blue")

button_1 = customtkinter.CTkButton(master = frame_1)
button_2 = customtkinter.CTkButton(master = frame_2,
                                   text = "cringe")

button_1.pack()
button_2.pack()
frame_1.pack()
frame_2.pack()

window.mainloop()