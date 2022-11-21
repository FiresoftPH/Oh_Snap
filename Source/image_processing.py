from PIL import Image, ImageEnhance, ImageOps
import os

class ImageProcessing:
    
    def make_picture_strip(self, Images, Mode, Frame, Output, Modify):
        self.Images = list(Images)
        self.Mode = Mode
        self.Output = Output
        self.Modify = Modify

        if self.Mode == 1: # Mode 1 = Vertical
            self.new_size_x = 557
            self.new_size_y = 348
            self.space_x = 22
            self.space_y = 23
            self.x_offset = 52
            self.y_offset = 220

            self.columns = 2
            
            if Frame == 1:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/BLACK.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 
                
            elif Frame == 2:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/WHITE.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif Frame == 3:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/RED.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif Frame == 4:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/LIGHTBLUE.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif Frame == 5:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/PASTELGRADIENT.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif Frame == 6:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/FLOWER.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            else:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/BLACK.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

        elif self.Mode == 2: # Mode 2 = Horizontal
            self.new_size_x = 512
            self.new_size_y = 320
            self.space_x = 23
            self.space_y = 123
            self.x_offset = 40
            self.y_offset = 232

            self.columns = 3
            
            if Frame == 1:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/BLACK.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 
                
            elif Frame == 2:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/WHITE.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            elif Frame == 3:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/RED.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            elif Frame == 4:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/LIGHTBLUE.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            elif Frame == 5:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/PASTELGRADIENT.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 
            
            elif Frame == 6:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/FLOWER.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            else:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/BLACK.png")
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

        else:
            self.new_size_x = 557
            self.new_size_y = 348
            self.space_x = 22
            self.space_y = 23
            self.x_offset = 52
            self.y_offset = 220

            self.columns = 2
            
            if self.Mode == 1:
                BG_Image_Vertical = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/VERTICAL_FRAME_(3X2)/SOLIDCOLOR/BLACK.png") # Background Image
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif self.Mode == 2:
                BG_Image_Horizontal = Image.open("/home/pi/Documents/Project/Oh_Snap/Pictures/HORIZONTAL_FRAME_(2X3)/SOLIDCOLOR/BLACK.png") # Background Image
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

        IMAGE_Resize = self.Resize_Image(self.Modify) 
        self.combine_images(Images = IMAGE_Resize) 

    
    def Resize_Image(self, Modify):
        LIST = [] # blank list to store resize image

        Horizontal_x = 512
        Horizontal_y = 320
        Vertical_x = 556.8
        Vertical_y = 348
        
        if self.Mode == 1: # Mode 1 = Vertical
            for i in range(6): 
                InputName = self.Images[i] 
                 
                img = Image.open(InputName) # open image 
                img_resize_Vertical = img.resize((int(Vertical_x), int(Vertical_y))) 

                if Modify == 1: # grayscale
                    img_resize_Vertical = ImageOps.grayscale(img_resize_Vertical)

                elif Modify == 2: # brightness
                    enhancer = ImageEnhance.Brightness(img_resize_Vertical)
                    
                    factor = 50
                    
                    Level = 1 + (factor/100)         #brightens the image
                    
                    img_resize_Vertical = enhancer.enhance(Level)

                Output_Vertical_Name = f"/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Processed_Image/Photo_Vertical_{i}.jpg" # Determine filename in Resize save in the folder Saved Images
                LIST.append(Output_Vertical_Name) 
                img_resize_Vertical.save(Output_Vertical_Name) 

        elif self.Mode == 2: # Mode 2 = Horizontal
            for i in range(6): 
                InputName = self.Images[i] 

                img = Image.open(InputName) # open image
                img_resize_Horizontal = img.resize((int(Horizontal_x), int(Horizontal_y))) 

                if Modify == 1: # grayscale
                    img_resize_Horizontal = ImageOps.grayscale(img_resize_Horizontal)

                elif Modify == 2: # brightness
                    enhancer = ImageEnhance.Brightness(img_resize_Horizontal)
                    
                    factor = 50
                    
                    Level = 1 + (factor/100)         #brightens the image
                    
                    img_resize_Horizontal = enhancer.enhance(Level)

                Output_Horizontal_Name = f"/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Processed_Image/Photo_Horizontal_{i}.jpg" # Determine filename in Resize save in the folder Saved Images 
                LIST.append(Output_Horizontal_Name) 
                
                img_resize_Horizontal.save(Output_Horizontal_Name) 


        else: 
            print("Mode Error")

        return LIST

    def combine_images(self, Images):
        background = self.BG

        x = 0 # initial value for x-axis
        y = 0 # initial value for y-axis
        for i, image in enumerate(Images): 
            img = Image.open(image) # open image
            
            background.paste(img, (x + self.x_offset, y + self.y_offset)) # paste image in Background Image
            x += self.new_size_x + self.space_x # change the position of x-axis to the next block
            
            if (i + 1) % self.columns == 0: 
                y += self.new_size_y + self.space_y  
                x = 0 
                
        background.save(self.Output)

    def clear_cached_images(self):
        for x in range(6):
            os.remove

        

IMAGE = ["/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Photo_3.jpg",   
         "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Photo_3.jpg",
         "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Photo_3.jpg",
         "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Photo_3.jpg",
         "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Photo_3.jpg",
         "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Photo_3.jpg"
         ]

# Mode = 1 # Mode 1 = Vertical, Mode 2 = Horizontal
# Frame = 1 # choose Frame Image
# Modify = 2 # choose Grayscale or Brightness
Output_IMAGE = "/home/pi/Documents/Project/Oh_Snap/Source/Saved_Images/Output_Image/Posted_Image.png" # output name

app = ImageProcessing()

# app.make_picture_strip(IMAGE, Mode, Frame, Output_IMAGE, Modify)

