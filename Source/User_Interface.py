# Import required Libraries
import os
import customtkinter
from PIL import Image, ImageTk
import threading
import shutil

# Created By Pattarapark Chutisamoot (FiresoftGH) with other pieces of code

"""
Command Codes List (The number corresponds to the command)
1. Destroying the widget packing inside the picture_selection frame

"""

# Importing other python scripts from other files

from camera import ShowFrame
from image_processing import ImageProcessing, Output_IMAGE
from webserver import Website

# print(os.getcwd())
default_directory = os.getcwd()

os.chdir(default_directory)

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

class MainUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Main window Setup
        self.geometry("1280x800")
        self.title("Oh Snap!")
        self.bind('<Escape>',lambda e: quit(e))
        # self.attributes('-fullscreen', True)
        
        # self.configure(fg_color = "#BFD4FF")

        self.main_background = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/BG_PG1.png")
        self.main_background_image = ImageTk.PhotoImage(self.main_background)

        # Background Label

        self.background_label = customtkinter.CTkLabel(master = self,
                                                       image = self.main_background_image)
                                                       
        self.background_label.place(x = 0, y = 0)

        # Global class variables
        self.confirmation_window = None
        self.number_to_text = {5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One", 0: "Zero"}
        self.camera = ShowFrame()
        self.image_processing = ImageProcessing()
        self.website = Website()

        # First Frame
        self.start_frame = customtkinter.CTkFrame(master = self,
                                                  width = 900,
                                                  height = 600,
                                                  corner_radius = 0,
                                                  fg_color = "#BFD4FF")
        
        self.logo = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/New_Logo.png")
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
        
        self.vertical_frame = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2).png")
        self.vertical_frame_resize = self.vertical_frame.resize((round(0.375 * self.vertical_frame.size[0]), round(0.375 * self.vertical_frame.size[1])))
   
        self.vertical_frame_picture = ImageTk.PhotoImage(self.vertical_frame_resize)

        self.vertical_frame_button = customtkinter.CTkButton(master = self.frame_selection,
                                                             image = self.vertical_frame_picture,
                                                             hover = False,
                                                             text = "",
                                                             command = lambda: self.confirmation_pop_up(1),
                                                             fg_color = "#BFD4FF")

        self.vertical_frame_label = customtkinter.CTkLabel(master = self.frame_selection,
                                                           text = "Vertical",
                                                           text_font = ("Inter", 25, "underline"),
                                                           text_color = "Black")
        
        # Horizontal frame widgets

        self.horizontal_frame = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3).png")
        self.horizontal_frame_resize = self.horizontal_frame.resize((round(0.25 * self.horizontal_frame.size[0]), round(0.25 * self.horizontal_frame.size[1])))
        self.horizontal_frame_picture = ImageTk.PhotoImage(self.horizontal_frame_resize)

        self.horizontal_frame_button = customtkinter.CTkButton(master = self.frame_selection,
                                                               image = self.horizontal_frame_picture,
                                                               hover = False,
                                                               text = "",
                                                               fg_color = "#BFD4FF",
                                                               command = lambda: self.confirmation_pop_up(2))

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

        self.camera_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Camera_Icon.png")
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

        self.hand_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Hand_Icon.png")
        self.hand_icon_resize = self.hand_icon.resize((290, 290))
        self.hand_icon_picture = ImageTk.PhotoImage(self.hand_icon_resize)

        self.hand_icon = customtkinter.CTkLabel(master = self.camera_controller_frame,
                                                image = self.hand_icon_picture)
        
        self.hand_label = customtkinter.CTkLabel(master = self.camera_controller_frame,
                                                 anchor = "center",
                                                 text = "Raise your hand to\ntake a picture",
                                                 text_color = "White",
                                                 text_font = ("Inter", 35))

        self.manual_button_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Arrow_Button.png")
        # print(self.manual_button_icon.size)
        self.manual_button_icon_resize = self.manual_button_icon.resize((61, 61))
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



        # Picture Preview frame for theme selection
        self.picture_preview_frame = customtkinter.CTkFrame(master = self,
                                                            width = 960,
                                                            height = 600,
                                                            corner_radius = 0,
                                                            fg_color = "#5C5C5C",
                                                            border_width = 0)

        # Theme color selection button frame
        self.theme_color_selection_frame = customtkinter.CTkFrame(master = self.picture_preview_frame,
                                                                  width = 480,
                                                                  height = 400,
                                                                  corner_radius = 10,
                                                                  fg_color = "#FFFFFF",
                                                                  border_width = 0)
        
        # Instruction label
        self.theme_color_selection_frame_label = customtkinter.CTkLabel(master = self.picture_preview_frame,
                                                                        text = "Select Frame Color",
                                                                        fg_color = "#5C5C5C",
                                                                        text_color = "White",
                                                                        text_font = ("Inter", 30, "underline"),
                                                                        corner_radius = 10)

        # Theme selection buttons
        self.black_bond_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Bond/Black_Bond.png")
        self.black_bond_icon_resize = self.black_bond_icon.resize((self.black_bond_icon.size[0] // 10, self.black_bond_icon.size[1] // 10))
        self.black_bond_icon_picture = ImageTk.PhotoImage(self.black_bond_icon_resize)
        self.black_bond_button = customtkinter.CTkButton(master = self.theme_color_selection_frame,
                                                         width = 0,
                                                         image = self.black_bond_icon_picture,
                                                         height = 0,
                                                         text = "",
                                                         fg_color = "#FFFFFF",
                                                         hover = False,
                                                         command = lambda: self.change_theme_color(1))

        self.blue_bond_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Bond/Blue_Bond.png")
        self.blue_bond_icon_resize = self.blue_bond_icon.resize((self.blue_bond_icon.size[0] // 10, self.blue_bond_icon.size[1] // 10))
        self.blue_bond_icon_picture = ImageTk.PhotoImage(self.blue_bond_icon_resize)
        self.blue_bond_button = customtkinter.CTkButton(master = self.theme_color_selection_frame,
                                                         width = 0,
                                                         image = self.blue_bond_icon_picture,
                                                         height = 0,
                                                         text = "",
                                                         fg_color = "#FFFFFF",
                                                         hover = False,
                                                         command = lambda: self.change_theme_color(4))

        self.purple_pink_bond_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Bond/Purple-Pink_Bond.png")
        self.purple_pink_bond_icon_resize = self.purple_pink_bond_icon.resize((self.purple_pink_bond_icon.size[0] // 10, self.purple_pink_bond_icon.size[1] // 10))
        self.purple_pink_bond_icon_picture = ImageTk.PhotoImage(self.purple_pink_bond_icon_resize)
        self.purple_pink_bond_button = customtkinter.CTkButton(master = self.theme_color_selection_frame,
                                                         width = 0,
                                                         image = self.purple_pink_bond_icon_picture,
                                                         height = 0,
                                                         text = "",
                                                         fg_color = "#FFFFFF",
                                                         hover = False,
                                                         command = lambda: self.change_theme_color(5))

        self.red_bond_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Bond/Red_Bond.png")
        self.red_bond_icon_resize = self.red_bond_icon.resize((self.red_bond_icon.size[0] // 10, self.red_bond_icon.size[1] // 10))
        self.red_bond_icon_picture = ImageTk.PhotoImage(self.red_bond_icon_resize)
        self.red_bond_button = customtkinter.CTkButton(master = self.theme_color_selection_frame,
                                                         width = 0,
                                                         image = self.red_bond_icon_picture,
                                                         height = 0,
                                                         text = "",
                                                         fg_color = "#FFFFFF",
                                                         hover = False,
                                                         command = lambda: self.change_theme_color(3))

        self.original_bond_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Bond/White_Bond.png")
        self.original_bond_icon_resize = self.original_bond_icon.resize((self.original_bond_icon.size[0] // 10, self.original_bond_icon.size[1] // 10))
        self.original_bond_icon_picture = ImageTk.PhotoImage(self.original_bond_icon_resize)
        self.original_bond_button = customtkinter.CTkButton(master = self.theme_color_selection_frame,
                                                            width = 0,
                                                            image = self.original_bond_icon_picture,
                                                            height = 0,
                                                            text = "",
                                                            fg_color = "#FFFFFF",
                                                            hover = False,
                                                            command = lambda: self.change_theme_color(2))

        self.purple_bond_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Bond/Purple_Bond.png")
        self.purple_bond_icon_resize = self.purple_bond_icon.resize((self.purple_bond_icon.size[0] // 10, self.purple_bond_icon.size[1] // 10))
        self.purple_bond_icon_picture = ImageTk.PhotoImage(self.purple_bond_icon_resize)
        self.purple_bond_button = customtkinter.CTkButton(master = self.theme_color_selection_frame,
                                                            width = 0,
                                                            image = self.purple_bond_icon_picture,
                                                            height = 0,
                                                            text = "",
                                                            fg_color = "#FFFFFF",
                                                            hover = False,
                                                            command = lambda: self.change_theme_color(6))

        # Placing the buttons on the frame
        self.black_bond_button.grid(row = 0, column = 0)
        self.blue_bond_button.grid(row = 0, column = 1)
        self.purple_pink_bond_button.grid(row = 0, column = 2)
        self.red_bond_button.grid(row = 1, column = 0)
        self.original_bond_button.grid(row = 1, column = 1)
        self.purple_bond_button.grid(row = 1, column = 2)

        # Filter selection frame preview
        self.filter_preview_frame = customtkinter.CTkFrame(master = self,
                                                           width = 960,
                                                           height = 600,
                                                           corner_radius = 0,
                                                           fg_color = "#5C5C5C",
                                                           border_width = 0)

        # Filter selection button frame
        self.filter_selection_frame = customtkinter.CTkFrame(master = self.filter_preview_frame,
                                                                  width = 480,
                                                                  height = 400,
                                                                  corner_radius = 10,
                                                                  fg_color = "#D3D3D3",
                                                                  border_width = 0)
        
        # Instruction label
        self.filter_selection_frame_label = customtkinter.CTkLabel(master = self.filter_preview_frame,
                                                                   text = "Select Filter",
                                                                   fg_color = "#5C5C5C",
                                                                   text_color = "White",
                                                                   text_font = ("Inter", 30, "underline"),
                                                                   corner_radius = 10)

        # Filter Selection Button
        self.bright_filter_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Bright_Button.png")
        self.bright_filter_icon_resize = self.bright_filter_icon.resize((160, 160))
        self.bright_filter_picture = ImageTk.PhotoImage(self.bright_filter_icon_resize)
        self.bright_filter_button = customtkinter.CTkButton(master = self.filter_selection_frame,
                                                            width = 0,
                                                            image = self.bright_filter_picture,
                                                            height = 0,
                                                            text = "",
                                                            fg_color = "#D3D3D3",
                                                            hover = False,
                                                            command = lambda: self.change_filter_mode(2))

        self.normal_filter_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Normal_Color_Button.png")
        self.normal_filter_icon_resize = self.normal_filter_icon.resize((160, 160))
        self.normal_filter_picture = ImageTk.PhotoImage(self.normal_filter_icon_resize)
        self.normal_filter_button = customtkinter.CTkButton(master = self.filter_selection_frame,
                                                            width = 0,
                                                            image = self.normal_filter_picture,
                                                            height = 0,
                                                            text = "",
                                                            fg_color = "#D3D3D3",
                                                            hover = False,
                                                            command = lambda: self.change_filter_mode(0))

        self.grayscale_filter_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Grayscale_Button.png")
        self.grayscale_filter_icon_resize = self.grayscale_filter_icon.resize((160, 160))
        self.grayscale_filter_picture = ImageTk.PhotoImage(self.grayscale_filter_icon_resize)
        self.grayscale_filter_button = customtkinter.CTkButton(master = self.filter_selection_frame,
                                                               width = 0,
                                                               image = self.grayscale_filter_picture,
                                                               height = 0,
                                                               text = "",
                                                               fg_color = "#D3D3D3",
                                                               hover = False,
                                                               command = lambda: self.change_filter_mode(1))

        self.bright_filter_button_label = customtkinter.CTkLabel(master = self.filter_selection_frame,
                                                                 text = "Bright",
                                                                 fg_color = "#D3D3D3",
                                                                 text_color = "Black",
                                                                 text_font = ("Inter", 15, "underline"),
                                                                 corner_radius = 0)

        self.normal_filter_button_label = customtkinter.CTkLabel(master = self.filter_selection_frame,
                                                                 text = "Normal",
                                                                 fg_color = "#D3D3D3",
                                                                 text_color = "Black",
                                                                 text_font = ("Inter", 15, "underline"),
                                                                 corner_radius = 0)

        self.grayscale_filter_button_label = customtkinter.CTkLabel(master = self.filter_selection_frame,
                                                                    text = "Grayscale",
                                                                    fg_color = "#D3D3D3",
                                                                    text_color = "Black",
                                                                    text_font = ("Inter", 15, "underline"),
                                                                    corner_radius = 0)                                                             
        # Placing filter selection buttons to the frame

        self.bright_filter_button.grid(row = 0, column = 0)
        self.normal_filter_button.grid(row = 0, column = 1)
        self.grayscale_filter_button.grid(row = 0, column = 2)
        self.bright_filter_button_label.grid(row  = 1, column = 0)
        self.normal_filter_button_label.grid(row = 1, column = 1)
        self.grayscale_filter_button_label.grid(row = 1, column = 2)

        # QR Code UI button frame and elements

        self.qr_code_frame = customtkinter.CTkFrame(master = self,
                                                    width = 960,
                                                    height = 600,
                                                    corner_radius = 0,
                                                    fg_color = "#BFD4FF",
                                                    border_width = 0)

        self.qr_code_frame_label = customtkinter.CTkLabel(master = self.qr_code_frame,
                                                          text = "Scan QR Code for Image",
                                                          fg_color = "#BFD4FF",
                                                          text_color = "Black",
                                                          text_font = ("Inter", 30, "underline"),
                                                          corner_radius = 0)

        self.home_button_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Home_Button.png")
        self.home_button_icon_picture = ImageTk.PhotoImage(self.home_button_icon)
        self.home_button = customtkinter.CTkButton(master = self.qr_code_frame,
                                                   width = 0,
                                                   image = self.home_button_icon_picture,
                                                   height = 0,
                                                   text = "",
                                                   fg_color = "#BFD4FF",
                                                   hover = False,
                                                   command = self.go_home)

    # Destroy the window
    def quit(self, e):
        self.destroy()

    # Change to selecting frame style for the photobooth
    def change_to_select_frame(self):
        self.start_frame.pack_forget()
        self.frame_selection.pack(anchor = "center", padx = 20, pady = 20, fill = "both", expand = 1)

    # Close the pop up window
    def close_pop_up(self):
        self.confirmation_window.destroy()

    # Pop-Up Button controls
    def change_to_taking_picture_frame(self):
        self.frame_selection.pack_forget()
        self.camera_ui_frame.pack(anchor = "center", padx = 20, pady = 20, fill = "both", expand = 1)
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
        thread_2 = threading.Thread(target = self.run_hand_detect)

        thread_1.start()
        thread_2.start()

    # Taking a photo
    def take_picture(self):
        if self.camera.image_list.size() < 8:
            self.camera.show_cam()
            self.threaded_opencv()

        else:
            self.camera.close_all()
            self.camera_controller_frame.pack_forget()
            self.make_picture_grid_label()
            self.make_picture_button()

    # Create a frame grid label for preview image
    def make_picture_grid_label(self):

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

        self.next_button_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Arrow_Button.png")
        self.next_button_icon_resize = self.next_button_icon.resize((61, 61))
        self.next_button_image = ImageTk.PhotoImage(self.manual_button_icon_resize)

        # Next Page button for the picture selection frame
        self.next_page_button = customtkinter.CTkButton(master = self.picture_grid_frame, 
                                                        width = 0,
                                                        height = 0,
                                                        image = self.next_button_image,
                                                        hover = False,
                                                        command = self.change_to_theme_selection_frame,
                                                        fg_color = "#BFD4FF",
                                                        text = "")
        
        print(frame_mode)
        if frame_mode == 1:
            self.frame_image = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2).png")
            self.frame_scale = tuple([round(self.frame_image.size[0] * 0.46), round(self.frame_image.size[1] * 0.46)])
            self.frame_image_resize = self.frame_image.resize(self.frame_scale)
            self.frame_image_python = ImageTk.PhotoImage(self.frame_image_resize)
            self.picture_grid_label = customtkinter.CTkLabel(master = self.picture_grid_frame,
                                                             image = self.frame_image_python)

            self.reset_button = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Reset_Button.png")
            self.reset_button_scale = (61, 61)
            self.reset_button_resize = self.reset_button.resize(self.reset_button_scale)
            self.reset_button_image_python = ImageTk.PhotoImage(self.reset_button_resize)
            self.reset_picture_selection_button = customtkinter.CTkButton(master = self.picture_grid_frame,
                                                                        image = self.reset_button_image_python,
                                                                        text = "",
                                                                        width = 0,
                                                                        height = 0,
                                                                        command = self.reset_all_selection,
                                                                        bg_color = "#FFFFFF",
                                                                        fg_color = "#FFFFFF",
                                                                        hover = False)
                                                                      
            self.picture_grid_label.place(x = 50, y = 90)
            self.reset_picture_selection_button.place(x = 550, y = 110)

        elif frame_mode == 2:
            self.frame_image = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3).png")
            self.frame_scale = tuple([round(self.frame_image.size[0] * 0.4), round(self.frame_image.size[1] * 0.4)])
            self.frame_image_resize = self.frame_image.resize(self.frame_scale)
            self.frame_image_python = ImageTk.PhotoImage(self.frame_image_resize)
            self.picture_grid_label = customtkinter.CTkLabel(master = self.picture_grid_frame,
                                                             image = self.frame_image_python)

            self.reset_button = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Reset_Button.png")
            self.reset_button_scale = (61, 61)
            self.reset_button_resize = self.reset_button.resize(self.reset_button_scale)
            self.reset_button_image_python = ImageTk.PhotoImage(self.reset_button_resize)
            self.reset_picture_selection_button = customtkinter.CTkButton(master = self.picture_grid_frame,
                                                                          image = self.reset_button_image_python,
                                                                          text = "",
                                                                          width = 0,
                                                                          height = 0,
                                                                          command = self.reset_all_selection,
                                                                          bg_color = "#FFFFFF",
                                                                          fg_color = "#FFFFFF",
                                                                          hover = False)
                                                                      
            self.picture_grid_label.place(x = 35, y = 150)
            self.reset_picture_selection_button.place(x = 600, y = 160)
        
    # Create similar button and frame for the picture selection
    def make_picture_button(self):

        global selected_button
        selected_button = []
        global selected_images
        selected_images = []
        global picture_button_dictionary
        picture_button_dictionary = {}
        
        self.next_page_button.place_forget()
        self.picture_selection_frame_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        for x in range(self.camera.image_list.size()):
            directory = "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images"
            
            index = self.camera.image_list.search(x)
            # print(index)
            image_directory = directory + "/{}".format(index)
            raw_picture = Image.open(image_directory)

            if frame_mode == 2:
                scale = tuple([round(raw_picture.size[0] * 0.4 / 2.53), round(raw_picture.size[1] * 0.4 / 2.53)])
                
            else:
                scale = tuple([round(raw_picture.size[0] * 0.435 / 2.19), round(raw_picture.size[1] * 0.435 / 2.19)])

            if x > 3:
                row_number = (x + 1) - 4
                column_number = 1

            else:
                row_number = x + 1
                column_number = 0

            # Defining Picture selection buttons functions according to the padding position
            raw_picture_resize = raw_picture.resize(scale)
            raw_picture_python = ImageTk.PhotoImage(raw_picture_resize)

            def picture_selection_button_function(selected_photo = raw_picture_python, image_dir  = image_directory):

                # The array down here reference the image position relative to the strip (right-left)
                selected_images.append(image_dir)

                selected_button.append(selected_photo)
                selected_button[len(selected_images) - 1] = customtkinter.CTkButton(master = self.picture_grid_frame,
                                                         image = selected_photo,
                                                         text = "",
                                                         command = None,
                                                         fg_color = "#FFFFFF",
                                                         bg_color = "#FFFFFF",
                                                         hover = False)
                
                selected_photo = selected_button[len(selected_button) - 1]
                # print(selected_images)
                if frame_mode == 1:

                    if len(selected_button) == 1:
                        selected_photo.place(x = 74, y = 191)

                    elif len(selected_button) == 2:
                        selected_photo.place(x = 340, y = 191)

                    elif len(selected_button) == 3:
                        selected_photo.place(x = 74, y = 361)

                    elif len(selected_button) == 4:
                        selected_photo.place(x = 340, y = 361)

                    elif len(selected_button) == 5:
                        selected_photo.place(x = 74, y = 531)

                    elif len(selected_button) == 6:
                        selected_photo.place(x = 340, y = 531)
                        self.next_page_button.place(x = 550, y = 20)

                    else:
                        print("Picture Strip is full")

                elif frame_mode == 2:

                    if len(selected_button) == 1:
                        selected_photo.place(x = 51, y = 242)

                    elif len(selected_button) == 2:
                        selected_photo.place(x = 265, y = 242)

                    elif len(selected_button) == 3:
                        selected_photo.place(x = 479, y = 242)

                    elif len(selected_button) == 4:
                        selected_photo.place(x = 51, y = 421)

                    elif len(selected_button) == 5:
                        selected_photo.place(x = 265, y = 421)

                    elif len(selected_button) == 6:
                        selected_photo.place(x = 479, y = 421)
                        self.next_page_button.place(x = 600, y = 20)

                    else:
                        print("Picture Strip is full")

            picture_button_dictionary[x] = customtkinter.CTkButton(master = self.picture_selection_frame,
                                                                   image = raw_picture_python,
                                                                   text = "",
                                                                   command = picture_selection_button_function,
                                                                   fg_color = "#BFD4FF",
                                                                   bg_color = "#BFD4FF")

            if frame_mode == 1:
                picture_button_dictionary[x].grid(row = row_number, column = column_number, padx = 5, pady = 5)                         

            elif frame_mode == 2:
                picture_button_dictionary[x].grid(row = row_number, column = column_number, padx = 20, pady = 20)

        self.camera_controller_frame.pack_forget()                        
        self.picture_grid_frame.pack(side = "right", padx = 20, pady = 20, fill = "both", expand = 1)
        self.picture_selection_frame.pack(side = "left", padx = 20, pady = 20, fill = "both")

    # Activating the picture strip code
    def make_picture_strip(self, color, mod):

        self.image_processing.make_picture_strip(selected_images, frame_mode, color, Output_IMAGE, mod)

    # Changing to theme selection frame and deleting unselected photos
    def change_to_theme_selection_frame(self):
        operator = self.camera.image_list.look()
        print(selected_images)
        image_list_transform = []

        for name in operator:
            new_directory = "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/" +  name
            image_list_transform.append(new_directory)
        print(image_list_transform)

        for directory in image_list_transform:
            if directory not in selected_images:
                os.remove(directory)
                print("Removed")
            else:
                print("Not Removed")

        # Clearing the image_list and making the default picture strip
        self.camera.reset_image_list()

        self.make_picture_strip(1, 2)

        self.picture_grid_frame.pack_forget()
        self.picture_selection_frame.pack_forget()

        # My Progress is right here

        self.picture_preview_frame.pack(padx = 20, pady = 20, side = "right", fill = "both", expand = 1)

        if frame_mode == 1:
            self.white_arrow_button = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Arrow_Button.png")
            self.white_arrow_button_resize = self.white_arrow_button.resize((61, 61))
            self.white_arrow_button_picture = ImageTk.PhotoImage(self.white_arrow_button_resize)
            self.change_to_filter_selection_frame_button = customtkinter.CTkButton(master = self.picture_preview_frame,
                                                                               image = self.white_arrow_button_picture,
                                                                               text = "",
                                                                               width = 0,
                                                                               height = 0,
                                                                               hover = False,
                                                                               fg_color = "#5C5C5C",
                                                                               bg_color = "#5C5C5C",
                                                                               command = self.change_to_filter_selection_frame)

            self.picture_preview = Image.open("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png")
            self.picture_preview_scale = tuple([round(self.frame_image.size[0] * 0.45), round(self.frame_image.size[1] * 0.45)])
            self.picture_preview_resize = self.picture_preview.resize(self.picture_preview_scale)
            self.picture_preview_python = ImageTk.PhotoImage(self.picture_preview_resize)
        
            self.picture_preview_label = customtkinter.CTkLabel(master = self.picture_preview_frame,
                                                                image = self.picture_preview_python)

            self.theme_color_selection_frame_label.grid(row = 0, column = 0, padx = 20)
            self.picture_preview_label.grid(row = 1, column = 0, padx = 20)
            self.theme_color_selection_frame.grid(row = 1, column = 1, padx = 20)
            self.change_to_filter_selection_frame_button.grid(row = 2, column = 2)

        elif frame_mode == 2:
            self.white_arrow_button = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/Arrow_Button.png")
            self.white_arrow_button_resize = self.white_arrow_button.resize((91, 91))
            self.white_arrow_button_picture = ImageTk.PhotoImage(self.white_arrow_button_resize)
            self.change_to_filter_selection_frame_button = customtkinter.CTkButton(master = self.picture_preview_frame,
                                                                               image = self.white_arrow_button_picture,
                                                                               text = "",
                                                                               width = 0,
                                                                               height = 0,
                                                                               hover = False,
                                                                               fg_color = "#5C5C5C",
                                                                               bg_color = "#5C5C5C",
                                                                               command = self.change_to_filter_selection_frame)

            self.picture_preview = Image.open("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png")
            self.picture_preview_scale = tuple([round(self.picture_preview.size[0] * 0.4), round(self.picture_preview.size[1] * 0.4)])
            self.picture_preview_resize = self.picture_preview.resize(self.picture_preview_scale)
            self.picture_preview_python = ImageTk.PhotoImage(self.picture_preview_resize)
        
            self.picture_preview_label = customtkinter.CTkLabel(master = self.picture_preview_frame,
                                                                image = self.picture_preview_python)

            self.theme_color_selection_frame_label.grid(row = 0, column = 0, padx = 20, pady = 20)
            self.picture_preview_label.grid(row = 1, column = 0, padx = 20, pady = 60)
            self.theme_color_selection_frame.grid(row = 1, column = 1, pady = 0)
            self.change_to_filter_selection_frame_button.grid(row = 2, column = 1)

    def change_to_filter_selection_frame(self):

        self.theme_color_selection_frame_label.grid_forget()
        self.theme_color_selection_frame.grid_forget()
        self.change_to_filter_selection_frame_button.grid_forget()
        self.picture_preview_label.grid_forget()
        self.picture_preview_frame.pack_forget()
        
        self.change_to_qrcode_frame_button = customtkinter.CTkButton(master = self.filter_preview_frame,
                                                                     image = self.white_arrow_button_picture,
                                                                     text = "",
                                                                     width = 0,
                                                                     height = 0,
                                                                     hover = False,
                                                                     fg_color = "#5C5C5C",
                                                                     bg_color = "#5C5C5C",
                                                                     command = self.run_website)

        self.filter_preview_frame.pack(padx = 20, pady = 20, side = "right", fill = "both", expand = 1)

        if frame_mode == 1:
            self.picture_preview = Image.open("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png")
            self.picture_preview_scale = tuple([round(self.frame_image.size[0] * 0.45), round(self.frame_image.size[1] * 0.45)])
            self.picture_preview_resize = self.picture_preview.resize(self.picture_preview_scale)
            self.picture_preview_python = ImageTk.PhotoImage(self.picture_preview_resize)
            self.filter_preview_label = customtkinter.CTkLabel(master = self.filter_preview_frame,
                                                               image = self.picture_preview_python)

            self.filter_selection_frame_label.grid(row = 0, column = 0, padx = 20)
            self.filter_preview_label.grid(row = 1, column = 0, padx = 20)
            self.filter_selection_frame.grid(row = 1, column = 1, padx = 20)
            self.change_to_qrcode_frame_button.grid(row = 2, column = 2)

        elif frame_mode == 2:
            self.picture_preview = Image.open("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png")
            self.picture_preview_scale = tuple([round(self.picture_preview.size[0] * 0.4), round(self.picture_preview.size[1] * 0.4)])
            self.picture_preview_resize = self.picture_preview.resize(self.picture_preview_scale)
            self.picture_preview_python = ImageTk.PhotoImage(self.picture_preview_resize)
        
            self.filter_preview_label = customtkinter.CTkLabel(master = self.filter_preview_frame,
                                                                image = self.picture_preview_python)

            self.filter_selection_frame_label.grid(row = 0, column = 0, padx = 20, pady = 20)
            self.filter_preview_label.grid(row = 1, column = 0, padx = 20, pady = 60)
            self.filter_selection_frame.grid(row = 1, column = 1, pady = 100)
            self.change_to_qrcode_frame_button.grid(row = 2, column = 1)
    
    # Run website methods
    def run_website(self):
        thread_3 = threading.Thread(target = self.website.flasK)
        thread_4 = threading.Thread(target = self.change_to_qrcode_frame)

        thread_3.start()
        thread_4.start()

    # Changing to QR Code frame

    def change_to_qrcode_frame(self):

        self.filter_preview_label.grid_forget()
        self.filter_selection_frame_label.grid_forget()
        self.change_to_qrcode_frame_button.grid_forget()
        self.filter_preview_label.grid_forget()
        self.filter_preview_frame.pack_forget()
        self.filter_selection_frame.grid_forget()

        self.qr_code_frame.pack(padx = 20, pady = 20, side = "right", fill = "both", expand = 1)

        self.qr_code_frame_label.grid(row = 0, column = 0, padx = 320, pady = 20)

        shutil.copy("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png", "/home/pi/Documents/Project/Oh_Snap/Source/static")

        self.qr_code_icon = Image.open("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/qrcodela.png")
        self.qr_code_icon_picture = ImageTk.PhotoImage(self.qr_code_icon)

        self.qr_code_picture_label = customtkinter.CTkLabel(master = self.qr_code_frame,
                                                            image = self.qr_code_icon_picture)
        self.qr_code_picture_label.grid(row = 1, column = 0, pady = 140)

        self.home_button.grid(row = 2, column = 1)

    # Packing the first frame and reset everything
    def go_home(self):
        self.qr_code_frame.pack_forget()
        self.camera.reset_image_list()
        self.start_frame.pack(anchor = "center", padx = 20, pady = 20, fill = "both", expand = 1)

    # Picture selection button function
    def reset_all_selection(self):
        
        for button in selected_button:
            button.place_forget()
        
        selected_images.clear()
        selected_button.clear()
        # self.make_picture_button()

    # Change Theme Color Button commands
    def change_theme_color(self, mode):
        global theme_color
        theme_color = mode
        self.image_processing.make_picture_strip(selected_images, frame_mode, theme_color, Output_IMAGE, 0)
        picture_preview = Image.open("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png")
        picture_preview_resize = picture_preview.resize(self.picture_preview_scale)
        picture_preview_python = ImageTk.PhotoImage(picture_preview_resize)

        self.picture_preview_label.configure(image = picture_preview_python)
        self.picture_preview_label.image = picture_preview_python

        return theme_color

    # Change Filter Mode Button commands
    def change_filter_mode(self, mode):
        global filter_mode
        filter_mode = mode
        if theme_color:
            self.image_processing.make_picture_strip(selected_images, frame_mode, theme_color, Output_IMAGE, filter_mode)
        else:
            self.image_processing.make_picture_strip(selected_images, frame_mode, 1, Output_IMAGE, filter_mode)

        picture_preview = Image.open("/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png")
        picture_preview_resize = picture_preview.resize(self.picture_preview_scale)
        picture_preview_python = ImageTk.PhotoImage(picture_preview_resize)

        self.filter_preview_label.configure(image = picture_preview_python)
        self.filter_preview_label.image = picture_preview_python

        return filter_mode
    # Change the global variable state
    def change_frame_mode(self, mode):
        global frame_mode
        frame_mode = mode
        return frame_mode

    # Create a pop-up confirmation window
    def confirmation_pop_up(self, mode):
        
        self.change_frame_mode(mode)
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
        
        print("The frame mode is ", frame_mode)
        # Packing elements in the pop-up frame
        confirmation_frame.pack(fill = "both", expand = 1)
        confirmation_label.place(x = 60, y = 40)
        confirmation_button_yes.place(x = 60, y = 100)
        confirmation_button_no.place(x = 200, y = 100)

app = MainUI()
app.mainloop()
