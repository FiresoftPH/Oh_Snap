import customtkinter
from PIL import Image, ImageTk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Main window Setup
        self.geometry("1280x800")
        self.title("Oh Snap!")
        self.bind('<Escape>',lambda e: quit(e))

        # Universal class variables
        self.confirmation_window = None

        # First Frame
        self.start_frame = customtkinter.CTkFrame(master = self,
                                                  width = 1280,
                                                  height = 800,
                                                  corner_radius = 0,
                                                  fg_color = "#BFD4FF")
        
        self.logo = Image.open('Pictures\logo.png')
        self.logo_resize = self.logo.resize((806, 576))
        self.logo_picture = ImageTk.PhotoImage(self.logo_resize)
        self.logo = customtkinter.CTkLabel(master = self.start_frame,
                                           image = self.logo_picture)

        self.start_button = customtkinter.CTkButton(master = self.start_frame,
                                                    text = "Tap to start",
                                                    text_font = ("Inter", 40),
                                                    command = self.change_to_select_frame,
                                                    fg_color = "#4A6EAF",
                                                    hover = True,
                                                    border_color = "Black",
                                                    text_color = "White",
                                                    corner_radius = 20)
        
        # Placing Elements in the first frame
        self.logo.grid(row = 0, column = 0, pady = 100, padx = 400)

        self.start_button.grid(row = 1, column = 0, pady = 100, padx = 0)

        self.start_frame.pack(fill = "both", expand = 1)

        # "Frame Selection" Elements

        # Vertical frame widgets

        self.frame_selection = customtkinter.CTkFrame(master = self,
                                                      width = 1280,
                                                      height = 800,
                                                      corner_radius = 0,
                                                      fg_color = "#BFD4FF")
        
        self.vertical_frame = Image.open("Pictures\Frame_Vertical.png")
        self.vertical_frame_resize = self.vertical_frame.resize((503, 791))
   
        self.vertical_frame_picture = ImageTk.PhotoImage(self.vertical_frame_resize)

        self.vertical_frame_button = customtkinter.CTkButton(master = self.frame_selection,
                                                             image = self.vertical_frame_picture,
                                                             hover = False,
                                                             text = "",
                                                             command = self.confirmation_pop_up,
                                                             fg_color = "#BFD4FF")

        self.vertical_frame_label = customtkinter.CTkLabel(master = self.frame_selection,
                                                           text = "Vertical",
                                                           text_font = ("Inter", 25, "underline"),
                                                           text_color = "Black")
        
        # Horizontal frame widgets

        self.horizontal_frame = Image.open("Pictures\Frame_Horizontal.png")
        self.horizontal_frame_resize = self.horizontal_frame.resize((791, 503))
        self.horizontal_frame_picture = ImageTk.PhotoImage(self.horizontal_frame_resize)

        self.horizontal_frame_button = customtkinter.CTkButton(master = self.frame_selection,
                                                               image = self.horizontal_frame_picture,
                                                               hover = False,
                                                               text = "",
                                                               fg_color = "#BFD4FF",
                                                               command = self.confirmation_pop_up)

        self.horizontal_frame_label = customtkinter.CTkLabel(master = self.frame_selection,
                                                             text = "Horizontal",
                                                             text_font = ("Inter", 25, "underline"),
                                                             text_color = "Black")
        
        # Select Frame Label
        self.select_frame_label = customtkinter.CTkLabel(master = self.frame_selection,
                                                             text = "Select Frame",
                                                             text_font = ("Inter", 25, "underline"),
                                                             text_color = "Black")

        # Packing elements in the second frame

        self.vertical_frame_label.grid(row = 0, column = 0, padx = 150, pady = 60, sticky = "new", rowspan = 10)
        self.vertical_frame_button.grid(row = 1, column = 0, padx = 120, pady = 100, sticky = "nsew")
        self.horizontal_frame_label.grid(row = 0, column = 2, padx = 0, pady = 140, sticky = "new", rowspan = 10)
        self.horizontal_frame_button.grid(row = 1, column = 2, padx = 0, pady = 0, sticky = "nsew")
        self.select_frame_label.grid(row = 2, column = 1, padx = 20, pady = 0, sticky = "ns", rowspan = 1, columnspan = 1)

    def quit(self,e):
        self.destroy()

    # Change to selecting frame style for the photobooth
    def change_to_select_frame(self):
        self.start_frame.pack_forget()
        self.frame_selection.pack(fill = "both", expand = 1)

    # Pop-Up Button controls
    def change_to_taking_picture_frame(self):
        self.frame_selection.pack_forget()

    def close_pop_up(self):
        self.confirmation_window.destroy()
        
    # Create a pop-up confirmation window
    def confirmation_pop_up(self):

        # Confirmation Pop-up window setup
        self.confirmation_window = customtkinter.CTkToplevel(self)

        self.confirmation_window.geometry("320x200")
        self.confirmation_window.title("Frame")

        main_window_x = self.winfo_x()
        main_window_y = self.winfo_y()

        self.confirmation_window.geometry("+%d+%d" % (main_window_x + 850, main_window_y + 500))
        # Confirmation Pop-up window frame
        confirmation_frame = customtkinter.CTkFrame(master = self.confirmation_window,
                                                     width = 320,
                                                     height = 200,
                                                     corner_radius = 0,
                                                     fg_color = "#FFFFFF")
        # Frame elements
        confirmation_label = customtkinter.CTkLabel(master = confirmation_frame,
                                                    text = "Are you sure?",
                                                    text_font = ("Imprima", 20, "underline"),
                                                    text_color = "black")

        confirmation_button_yes = customtkinter.CTkButton(master = confirmation_frame,
                                                          hover = False,
                                                          text = "Yes",
                                                          text_font = ("Imprima", 20),
                                                          text_color = "white",
                                                          command = self.change_to_taking_picture_frame,
                                                          width = 60,
                                                          height = 30,
                                                          corner_radius = 8)

        confirmation_button_no = customtkinter.CTkButton(master = confirmation_frame,
                                                         hover = False,
                                                         text = "No",
                                                         text_font = ("Imprima", 20),
                                                         text_color = "white",
                                                         command = self.close_pop_up,
                                                         width = 60,
                                                         height = 30,
                                                         corner_radius = 8)
        
        # Packing elements in the pop-up frame
        confirmation_frame.pack(fill = "both", expand = 1)
        confirmation_label.place(x = 80, y = 40)
        confirmation_button_yes.place(x = 60, y = 100)
        confirmation_button_no.place(x = 200, y = 100)


app = App()
app.mainloop()
