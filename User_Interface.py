import customtkinter
from PIL import Image, ImageTk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1280}x{1024}")
        self.title("Oh Snap!")
        self.bind('<Escape>',lambda e: quit(e))

        # First Frame
        self.mainframe = customtkinter.CTkFrame(master = self,
                                                width = 1280,
                                                height = 1024,
                                                corner_radius=10,
                                                fg_color = "#BFD4FF")
        
        self.dummy = Image.open('Pictures\sticker_3.png')
        self.python_dummy = ImageTk.PhotoImage(self.dummy)

        self.logo = customtkinter.CTkLabel(master = self.mainframe,
                                           image = self.python_dummy)
        self.logo.grid(row = 0, column = 0, pady = 100, padx = 500)

        self.start_btn = customtkinter.CTkButton(master = self.mainframe,
                                              text = "Tap to start",
                                              text_font = ("Roboto Medium", -25))
        self.start_btn.grid(row = 1, column = 0, pady = 100, padx = 10)

        self.mainframe.pack(fill="both", expand=1) # Fullscreen frame?

    def quit(self,e):
        self.destroy()
        

app = App()
app.mainloop()
