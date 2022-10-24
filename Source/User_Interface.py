import customtkinter
from PIL import Image, ImageTk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1280}x{1024}")
        self.title("Oh Snap!")
        self.bind('<Escape>',lambda e: quit(e))

        # First Frame
        self.start_frame = customtkinter.CTkFrame(master = self,
                                                width = 1280,
                                                height = 1024,
                                                corner_radius = 0,
                                                fg_color = "#BFD4FF")
        
        self.dummy = Image.open('Pictures\sticker_3.png')
        self.python_dummy = ImageTk.PhotoImage(self.dummy)

        self.logo = customtkinter.CTkLabel(master = self.start_frame,
                                           image = self.python_dummy)
        self.logo.grid(row = 0, column = 0, pady = 100, padx = 500)

        self.start_btn = customtkinter.CTkButton(master = self.start_frame,
                                                 text = "Tap to start",
                                                 text_font = ("Roboto Medium", -25),
                                                 command = self.change_to_select_frame)
        
        # Packing first frame
        self.logo.grid(row = 0, column = 0, pady = 100, padx = 500)
        self.start_btn.grid(row = 1, column = 0, pady = 100, padx = 10)
        self.start_frame.pack(fill="both", expand=1) # Fullscreen frame?

        # "Frame Selection" Frame
        self.frame_selection = customtkinter.CTkFrame(master = self,
                                                width = 1280,
                                                height = 1024,
                                                corner_radius = 0,
                                                fg_color = "#BFD4FF")
        
        self.photo_placeholder = 
    def quit(self,e):
        self.destroy()

    # Change to selecting frame style for the photobooth
    def change_to_select_frame(self):
        self.start_frame.pack_forget()
        self.frame_selection.pack()

    def change_to_taking_picture_frame():
        pass
        
app = App()
app.mainloop()
