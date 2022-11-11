# Import required Libraries
import os
import random
import customtkinter
from PIL import Image, ImageTk
import threading

"""
Description: This UI_Interface is for development in windows. Adapting to Linux version is simple, changing the directory
of the images and files to Linux syntax and everything should work fine.
"""

"""
Command Codes List (The number corresponds to the command)
1. 
"""

# Importing other python scripts from other files

from data_structure import Stack, SinglyLinkedList
from camera import ShowFrame

# print(os.getcwd())
default_directory = os.getcwd()

# This process is here to make sure that overridden does not happen too much
def remove_cache_photo():
    os.chdir("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images")
    for x in range(8):
        file_name = "Photo_{}.jpg".format(x)
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            pass

remove_cache_photo()

os.chdir(default_directory)

# Global Variables
frame_mode = 0
selected_images = Stack([], 6)
picture_button_dictionary = {}


class MainUI(customtkinter.CTk):
    def __init__(self, frame_mode, selected_images):
        super().__init__()

        # Main window Setup
        self.geometry("1280x800")
        self.title("Oh Snap!")
        self.bind('<Escape>',lambda e: quit(e))
        # self.attributes('-fullscreen', True)
        
        # self.configure(fg_color = "#BFD4FF")

        self.main_background = Image.open("Pictures/BG_PG1.png")
        self.main_background_image = ImageTk.PhotoImage(self.main_background)

        # Background Label

        self.background_label = customtkinter.CTkLabel(master = self,
                                                       image = self.main_background_image)
                                                       
        self.background_label.place(x = 0, y = 0)

        # Global class variables
        self.confirmation_window = None
        self.command_code = 0 # For issuing similar commands at different conditions
        self.number_to_text = {5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One", 0: "Zero"}
        self.camera = ShowFrame()
        self.selected_images = selected_images
        self.frame_mode = frame_mode

        # First Frame
        self.start_frame = customtkinter.CTkFrame(master = self,
                                                  width = 900,
                                                  height = 600,
                                                  corner_radius = 0,
                                                  fg_color = "#BFD4FF")
        
        self.logo = Image.open("Pictures/New_Logo.png")
        # print(self.logo.size)
        self.logo_resize = self.logo.resize((605, 650))
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
        self.logo.grid(row = 0, column = 0, pady = 0, padx = 300)
        self.start_button.grid(row = 1, column = 0, pady = 0, padx = 0)
        self.start_frame.pack(anchor = "center", padx = 20, pady = 20, fill = "both", expand = 1)

        # "Frame Selection" Elements

        # Vertical frame widgets

        self.frame_selection = customtkinter.CTkFrame(master = self,
                                                      width = 900,
                                                      height = 600,
                                                      corner_radius = 0,
                                                      fg_color = "#BFD4FF")
        
        self.vertical_frame = Image.open("Pictures/VERTICAL_FRAME_(3X2).png")
        self.vertical_frame_resize = self.vertical_frame.resize((round(0.375 * self.vertical_frame.size[0]), round(0.375 * self.vertical_frame.size[1])))
   
        self.vertical_frame_picture = ImageTk.PhotoImage(self.vertical_frame_resize)

        self.vertical_frame_button = customtkinter.CTkButton(master = self.frame_selection,
                                                             image = self.vertical_frame_picture,
                                                             hover = False,
                                                             text = "",
                                                             command = lambda: self.confirmation_pop_up(0),
                                                             fg_color = "#BFD4FF")

        self.vertical_frame_label = customtkinter.CTkLabel(master = self.frame_selection,
                                                           text = "Vertical",
                                                           text_font = ("Inter", 25, "underline"),
                                                           text_color = "Black")
        
        # Horizontal frame widgets

        self.horizontal_frame = Image.open("Pictures/HORIZONTAL_FRAME_(2X3).png")
        self.horizontal_frame_resize = self.horizontal_frame.resize((round(0.25 * self.horizontal_frame.size[0]), round(0.25 * self.horizontal_frame.size[1])))
        self.horizontal_frame_picture = ImageTk.PhotoImage(self.horizontal_frame_resize)

        self.horizontal_frame_button = customtkinter.CTkButton(master = self.frame_selection,
                                                               image = self.horizontal_frame_picture,
                                                               hover = False,
                                                               text = "",
                                                               fg_color = "#BFD4FF",
                                                               command = lambda: self.confirmation_pop_up(1))

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

        self.vertical_frame_label.grid(row = 0, column = 0, padx = 150, pady = 30, sticky = "new", rowspan = 10)
        self.vertical_frame_button.grid(row = 1, column = 0, padx = 30, pady = 80, sticky = "nsew")
        self.horizontal_frame_label.grid(row = 0, column = 2, padx = 0, pady = 40, sticky = "new", rowspan = 10)
        self.horizontal_frame_button.grid(row = 1, column = 2, padx = 0, pady = 0, sticky = "nsew")
        self.select_frame_label.grid(row = 2, column = 1, padx = 20, pady = 0, rowspan = 1, columnspan = 1, sticky = "ns")

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
                                                           command = self.threaded_opencv)

        # Placing elements in the third frame
        self.camera_start_button.pack(anchor = "center", pady = 150)

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

        # Picture selection
        self.picture_selection_frame = customtkinter.CTkFrame(master = self,
                                                              width = 460,
                                                              height = 600,
                                                              corner_radius = 0,
                                                              fg_color = "#BFD4FF",
                                                              border_width = 0)

        # Select Image label
        self.picture_selection_frame_label = customtkinter.CTkLabel(master = self.picture_selection_frame,
                                                                    text_font = ("Inter", 25, "underline"),
                                                                    text = "Select Image",
                                                                    fg_color = "#BFD4FF")

        # Picture grid frame
        self.picture_grid_frame = customtkinter.CTkFrame(master = self,
                                                         width = 460,
                                                         height = 600,
                                                         corner_radius = 0,
                                                         fg_color = "#BFD4FF",
                                                         border_width = 0)

        if self.frame_mode == 0:
            self.frame_image = Image.open("Pictures/VERTICAL_FRAME_(3X2).png")
            self.frame_scale = tuple([round(self.frame_image.size[0] * 0.46), round(self.frame_image.size[1] * 0.46)])
            self.frame_image_resize = self.frame_image.resize(self.frame_scale)
            self.frame_image_python = ImageTk.PhotoImage(self.frame_image_resize)
            self.picture_grid_label = customtkinter.CTkLabel(master = self.picture_grid_frame,
                                                             image = self.frame_image_python)

            self.picture_grid_label.place(x = 40, y = 90)

        elif self.frame_mode == 1:
            self.frame_image = Image.open("Pictures/Horizontal_FRAME_(3X2).png")
            self.frame_scale = tuple([round(self.frame_image.size[0] * 0.4 / 2.2), round(self.frame_image.size[1] * 0.4 / 2.2)])
            self.frame_image_resize = self.frame_image.resize(self.frame_scale)
            self.frame_image_python = ImageTk.PhotoImage(self.frame_image_resize)
            self.picture_grid_label = customtkinter.CTkLabel(master = self.picture_grid_frame,
                                                             image = self.frame_image_python)
        
            self.picture_grid_label.place(x = 0, y = 0)

        self.reset_button = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Reset_Button.png")
        self.reset_button_scale = (61, 61)
        self.reset_button_resize = self.reset_button.resize(self.reset_button_scale)
        self.reset_button_image_python = ImageTk.PhotoImage(self.reset_button_resize)
        self.reset_picture_selection_button = customtkinter.CTkButton(master = self.picture_grid_frame,
                                                                      image = self.reset_button_image_python,
                                                                      text = "",
                                                                      width = 0,
                                                                      height = 0,
                                                                      command = None,
                                                                      bg_color = "#FFFFFF",
                                                                      fg_color = "#FFFFFF")
        
        self.reset_picture_selection_button.place(x = 50, y = 50)

    def quit(self, e):
        self.destroy()

    # Change to selecting frame style for the photobooth
    def change_to_select_frame(self):
        self.start_frame.pack_forget()
        self.frame_selection.pack(anchor = "center", padx = 20, pady = 20, fill = "both", expand = 1)

    # Pop-Up Button controls
    def change_to_taking_picture_frame(self):
        self.frame_selection.pack_forget()
        self.camera_ui_frame.pack(anchor = "center", padx = 20, pady = 20, fill = "both", expand = 1)
        self.confirmation_window.destroy()

    def close_pop_up(self):
        self.confirmation_window.destroy()

    # Change from photo taking frame to selecting pictures frame
    def change_to_camera_instructions_frame(self):
        self.camera_ui_frame.pack_forget()
        self.camera_controller_frame.pack(padx = 20, pady = 20, fill = "both", expand = 1)

    # Run hand detection code
    def run_hand_detect(self):
        self.camera.detect_hand()

    # Using threading, the two process can run simulataneously
    def threaded_opencv(self):
        thread_1 = threading.Thread(target = self.change_to_camera_instructions_frame)
        # thread_2 = threading.Thread(target = self.run_hand_detect)

        thread_1.start()
        # thread_2.start()

    # Taking a photo
    def take_picture(self):
        
        if self.camera.image_list.size() < 8:
            self.camera.show_cam()
            self.threaded_opencv()

        else:
            self.camera_controller_frame.pack_forget()
            self.make_picture_button()
            self.camera.close_all()

    # Create similar button and frame for the picture selection
    def make_picture_button(self):

        self.picture_selection_frame_label.grid(row = 0, column = 0)
        for x in range(self.camera.image_list.size()):
            directory = "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images"
            
            index = self.camera.image_list.search(x)
            # print(index)
            image_directory = directory + "/{}".format(index)
            raw_picture = Image.open(image_directory)

            if self.frame_mode == 1:
                scale = tuple([round(raw_picture.size[0] * 0.4 / 2.2), round(raw_picture.size[1] * 0.4 / 2.2)])
                
            else:
                scale = tuple([round(raw_picture.size[0] * 0.435 / 2.19), round(raw_picture.size[1] * 0.435 / 2.19)])

            if x > 3:
                row_number = x - 4
                column_number = 1

            else:
                row_number = x 
                column_number = 0

            # Defining Picture selection buttons functions according to the padding position
            raw_picture_resize = raw_picture.resize(scale)
            raw_picture_python = ImageTk.PhotoImage(raw_picture_resize)

            def picture_selection_button_function(photo_number = self.camera.image_list.search(x), selected_photo = raw_picture_python):
                

                selected_images.push(photo_number)
                print(selected_images.look())
                selected_photo = customtkinter.CTkButton(master = self.picture_grid_frame,
                                                         image = selected_photo,
                                                         text = "",
                                                         command = None,
                                                         fg_color = "#FFFFFF",
                                                         bg_color = "#FFFFFF")
                if self.frame_mode == 0:

                    if selected_images.size() == 1:
                        selected_photo.place(x = 64, y = 191)

                    elif selected_images.size() == 2:
                        selected_photo.place(x = 330, y = 191)

                    elif selected_images.size() == 3:
                        selected_photo.place(x = 64, y = 361)

                    elif selected_images.size() == 4:
                        selected_photo.place(x = 330, y = 361)

                    elif selected_images.size() == 5:
                        selected_photo.place(x = 64, y = 531)

                    elif selected_images.size() == 6:
                        selected_photo.place(x = 330, y = 531)

            picture_button_dictionary[x] = customtkinter.CTkButton(master = self.picture_selection_frame,
                                                                   image = raw_picture_python,
                                                                   text = "",
                                                                   command = picture_selection_button_function,
                                                                   fg_color = "#BFD4FF",
                                                                   bg_color = "#BFD4FF").grid(row = row_number, column = column_number, padx = 10, pady = 10)
        
        self.camera_controller_frame.pack_forget()                        
        self.picture_grid_frame.pack(side = "right", padx = 20, pady = 20, fill = "both", expand = 1)
        self.picture_selection_frame.pack(side = "left", padx = 20, pady = 20, fill = "both")

    # Create a pop-up confirmation window
    def confirmation_pop_up(self, mode):

        self.frame_mode = mode
        print(self.frame_mode)

        # Confirmation Pop-up window setup
        self.confirmation_window = customtkinter.CTkToplevel(self)
        self.confirmation_window.bind('<Escape>',lambda e: quit(e))
        
        self.confirmation_window.geometry("320x200")
        self.confirmation_window.title("Frame")
        self.confirmation_window.attributes('-topmost', True)

        main_window_x = self.winfo_x()
        main_window_y = self.winfo_y()

        self.confirmation_window.geometry("+%d+%d" % (main_window_x + 500, main_window_y + 300))

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
        confirmation_label.place(x = 60, y = 40)
        confirmation_button_yes.place(x = 60, y = 100)
        confirmation_button_no.place(x = 200, y = 100)

app = MainUI(frame_mode, selected_images)
app.mainloop()
