# Import required Libraries

import customtkinter
from PIL import Image, ImageTk
from time import sleep

"""
Description: This UI_Interface is for development in windows. Adapting to Linux version is simple, changing the directory
of the images and files to Linux syntax and everything should work fine.
"""

"""
Command Codes List (The number corresponds to the command)
1. Show the countdown widget with the camera
2. 
"""

# Importing other python scripts from other files

from data_structure import Stack, SinglyLinkedList
from camera import ShowFrame

class MainUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Main window Setup
        self.geometry("1280x800")
        self.title("Oh Snap!")
        self.bind('<Escape>',lambda e: quit(e))
        self.configure(fg_color = "#BFD4FF")

        # Universal class variables
        self.confirmation_window = None
        self.command_code = 0 # For issuing similar commands at different conditions
        self.number_to_text = {5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One", 0: "Zero"}
        self.camera = ShowFrame()

        # First Frame
        self.start_frame = customtkinter.CTkFrame(master = self,
                                                  width = 1280,
                                                  height = 800,
                                                  corner_radius = 0,
                                                  fg_color = "#BFD4FF")
        
        self.logo = Image.open("Pictures/logo.png")
        self.logo_resize = self.logo.resize((806, 576))
        self.logo_picture = ImageTk.PhotoImage(self.logo_resize)
        self.logo = customtkinter.CTkLabel(master = self.start_frame,
                                           image = self.logo_picture)

        self.start_button = customtkinter.CTkButton(master = self.start_frame,
                                                    text = "Tap to start",
                                                    text_font = ("Imprima", 30),
                                                    command = self.change_to_select_frame,
                                                    fg_color = "#4A6EAF",
                                                    hover = True,
                                                    height = 70,
                                                    text_color = "White",
                                                    corner_radius = 50)
        
        # Placing Elements in the first frame
        self.logo.grid(row = 0, column = 0, pady = 60, padx = 220)
        self.start_button.grid(row = 1, column = 0, pady = 0, padx = 0)
        self.start_frame.pack(fill = "both", expand = 1)

        # "Frame Selection" Elements

        # Vertical frame widgets

        self.frame_selection = customtkinter.CTkFrame(master = self,
                                                      width = 1280,
                                                      height = 800,
                                                      corner_radius = 0,
                                                      fg_color = "#BFD4FF")
        
        self.vertical_frame = Image.open("Pictures/Frame_Vertical.png")
        self.vertical_frame_resize = self.vertical_frame.resize((503, 791))
   
        self.vertical_frame_picture = ImageTk.PhotoImage(self.vertical_frame)

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

        self.horizontal_frame = Image.open("Pictures/Frame_Horizontal.png")
        self.horizontal_frame_resize = self.horizontal_frame.resize((791, 503))
        self.horizontal_frame_picture = ImageTk.PhotoImage(self.horizontal_frame)

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
        self.vertical_frame_button.grid(row = 1, column = 0, padx = 50, pady = 100, sticky = "nsew")
        self.horizontal_frame_label.grid(row = 0, column = 2, padx = 0, pady = 160, sticky = "new", rowspan = 10)
        self.horizontal_frame_button.grid(row = 1, column = 2, padx = 0, pady = 0, sticky = "nsew")
        self.select_frame_label.grid(row = 2, column = 1, padx = 20, pady = 0, rowspan = 1, columnspan = 1)

        # Camera.py dummy UI here

        self.camera_ui_frame = customtkinter.CTkFrame(master = self,
                                                      width = 960,
                                                      height = 600,
                                                      corner_radius = 0,
                                                      fg_color = "#BFD4FF")

        # Camera start UI

        self.camera_icon = Image.open("Pictures/Camera_Icon.png")
        self.camera_icon_resize = self.camera_icon.resize((self.camera_icon.size[0] * 1, self.camera_icon.size[1] * 1))
        self.camera_icon_picture = ImageTk.PhotoImage(self.camera_icon_resize)

        self.camera_start_button = customtkinter.CTkButton(master = self.camera_ui_frame,
                                                           image = self.camera_icon_picture,
                                                           hover = False,
                                                           text = "",
                                                           fg_color = "#BFD4FF",
                                                           command = self.change_to_camera_instructions_frame)

        # Placing elements in the third frame
        self.camera_start_button.place(x = 400, y = 200)

        # Camera controlling UI
        self.camera_controller_frame = customtkinter.CTkFrame(master = self,
                                                              width = 960,
                                                              height = 600,
                                                              corner_radius = 0,
                                                              fg_color = "#5C5C5C",
                                                              border_width = 0)

        self.hand_icon = Image.open("Pictures/Hand_Icon.png")
        self.hand_icon_resize = self.hand_icon.resize((290, 290))
        self.hand_icon_picture = ImageTk.PhotoImage(self.hand_icon_resize)

        self.hand_icon = customtkinter.CTkLabel(master = self.camera_controller_frame,
                                                image = self.hand_icon_picture)
        
        self.hand_label = customtkinter.CTkLabel(master = self.camera_controller_frame,
                                                 anchor = "center",
                                                 text = "Raise your hand to\ntake a picture",
                                                 text_color = "White",
                                                 text_font = ("Inter", 35))

        self.manual_button_icon = Image.open("Pictures/Arrow_Button.png")
        # print(self.manual_button_icon.size)
        self.manual_button_icon_resize = self.manual_button_icon.resize((45, 45))
        self.manual_button_picture = ImageTk.PhotoImage(self.manual_button_icon)

        self.manual_button = customtkinter.CTkButton(master = self.camera_controller_frame,
                                                     command = self.take_picture,
                                                     text = "",
                                                     hover = False,
                                                     image = self.manual_button_picture,
                                                     bg_color = "#5C5C5C",
                                                     fg_color = "#5C5C5C")

        self.manual_button_label = customtkinter.CTkLabel(master = self.camera_controller_frame,
                                                          text = "Or skip",
                                                          text_color = "White",
                                                          text_font = ("Inter", 30))
        
        # Packing elements in fourth frame
        self.hand_label.grid(row = 0, column = 0, padx = 300, pady = 100)
        self.hand_icon.grid(row = 1, column = 0)
        self.manual_button_label.grid(row = 2, column = 1)
        self.manual_button.grid(row = 3, column = 1)

        # Countdown frame for camera
        self.countdown_frame = customtkinter.CTkFrame(master = self,
                                                      width = 960,
                                                      height = 600,
                                                      corner_radius = 0,
                                                      fg_color = "#5C5C5C",
                                                      border_width = 0)

        # Countdown display
        self.countdown_icon = customtkinter.CTkLabel(master = self.countdown_frame,
                                                     text = "",
                                                     image = None)

        # Packing the elements in the fifth frame
        self.countdown_icon.place(x = 475, y = 250)

        # Camera frame

    def quit(self, e):
        self.destroy()

    # Change to selecting frame style for the photobooth
    def change_to_select_frame(self):
        self.start_frame.pack_forget()
        self.frame_selection.pack(fill = "both", expand = 1)

    # Pop-Up Button controls
    def change_to_taking_picture_frame(self):
        self.frame_selection.pack_forget()
        self.camera_ui_frame.pack(fill = "both", expand = 1)
        self.confirmation_window.destroy()

    def close_pop_up(self):
        self.confirmation_window.destroy()

    # Change from photo taking frame to selecting pictures frame
    def change_to_camera_instructions_frame(self):
        self.camera_ui_frame.pack_forget()
        self.camera_controller_frame.pack(padx = 20, pady = 20, fill = "both")

    # Taking a photo
    def take_picture(self):
        self.camera.show_cam()


    # Timer (input in seconds) (Unused Asset)
    def timer(self, initial_time):
        if self.command_code == 1:
            self.countdown_frame.pack(fill = "both", padx = 20, pady = 20, expand = 1)

        while initial_time >= 0:
            mins, secs = divmod(initial_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            if self.command_code == 1:
                image_index = self.number_to_text[initial_time]
                image_directory = "Pictures/Countdown_display/{}.png".format(image_index)
                display_image = Image.open(image_directory)
                display_image_python = ImageTk.PhotoImage(display_image)
                self.countdown_icon.configure(image = display_image_python)
                self.countdown_icon.image = display_image_python
            
            self.update()
            sleep(1)
            initial_time -= 1

    # Create a pop-up confirmation window
    def confirmation_pop_up(self):

        # Confirmation Pop-up window setup
        self.confirmation_window = customtkinter.CTkToplevel(self)
        
        self.confirmation_window.geometry("320x200")
        self.confirmation_window.title("Frame")

        main_window_x = self.winfo_x()
        main_window_y = self.winfo_y()

        self.confirmation_window.geometry("+%d+%d" % (main_window_x + 700, main_window_y + 500))

        # Confirmation Pop-up window frame
        confirmation_frame = customtkinter.CTkFrame(master = self.confirmation_window,
                                                    width = 320,
                                                    height = 200,
                                                    corner_radius = 0,
                                                    fg_color = "#FFFFFF")
        
        # Frame elements
        confirmation_label = customtkinter.CTkLabel(master = confirmation_frame,
                                                    text = "Are you sure?",
                                                    text_font = ("Imprima", 20),
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

app = MainUI()
app.mainloop()
