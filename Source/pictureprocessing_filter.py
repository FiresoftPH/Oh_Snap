from PIL import Image, ImageEnhance, ImageOps

class ImageProcessing:
    def __init__(self, Images, Mode, Frame, Output):
        self.Images = list(Images)
        self.Mode = Mode
        self.Output = Output

        if self.Mode == 1: # Mode 1 = Vertical, Mode 2 = Horizontal
            self.new_size_x = 557
            self.new_size_y = 348
            self.space_x = 22
            self.space_y = 23
            self.x_offset = 52
            self.y_offset = 220

            self.columns = 2
            
            if Frame == 1:
                BG_Image_Vertical = Image.open("D:\Saved Images\BLACK_Vertical.png") # Background Image
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 
                
            elif Frame == 2:
                BG_Image_Vertical = Image.open("D:\Saved Images\WHITE_Vertical.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif Frame == 3:
                BG_Image_Vertical = Image.open("D:\Saved Images\RED_Vertical.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif Frame == 4:
                BG_Image_Vertical = Image.open("D:\Saved Images\LIGHTBLUE_Vertical.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            elif Frame == 5:
                BG_Image_Vertical = Image.open("D:\Saved Images\PASTELGRADIENT_Vertical.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

            else:
                BG_Image_Vertical = Image.open("D:\Saved Images\BLACK_Vertical.png") 
                self.BG = BG_Image_Vertical.resize((1240, 1432)) 

        elif self.Mode == 2: # Mode 1 = Vertical, Mode 2 = Horizontal
            self.new_size_x = 512
            self.new_size_y = 320
            self.space_x = 23
            self.space_y = 123
            self.x_offset = 40
            self.y_offset = 232

            self.columns = 3
            
            if Frame == 1:
                BG_Image_Horizontal = Image.open("D:\Saved Images\BLACK_Horizontal.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 
                
            elif Frame == 2:
                BG_Image_Horizontal = Image.open("D:\Saved Images\WHITE_Horizontal.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            elif Frame == 3:
                BG_Image_Horizontal = Image.open("D:\Saved Images\RED_Horizontal.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            elif Frame == 4:
                BG_Image_Horizontal = Image.open("D:\Saved Images\LIGHTBLUE_Horizontal.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            elif Frame == 5:
                BG_Image_Horizontal = Image.open("D:\Saved Images\PASTELGRADIENT_Horizontal.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

            else:
                BG_Image_Horizontal = Image.open("D:\Saved Images\BLACK_Horizontal.png") 
                self.BG = BG_Image_Horizontal.resize((1665, 1100)) 

        else: # default
            self.new_size_x = 557
            self.new_size_y = 348
            self.space_x = 22
            self.space_y = 23
            self.x_offset = 52
            self.y_offset = 220

            self.columns = 2
            
            BG_Image_Vertical = Image.open("D:\Saved Images\BLACK_Vertical.png") # Background Image
            self.BG = BG_Image_Vertical.resize((1240, 1432)) 

    
    def Resize_Image(self, Modify):
        LIST = [] # blank list to store resize image

        Horizontal_x = 512
        Horizontal_y = 320
        Vertical_x = 556.8
        Vertical_y = 348
        
        if self.Mode == 1: # Mode 1 = Vertical, Mode 2 = Horizontal
            for i in range(6): # loop Resize 6 images 
                InputName = self.Images[i] 
                 
                img = Image.open(InputName) # open image 
                img_resize_Vertical = img.resize((int(Vertical_x), int(Vertical_y))) 

                if Modify == 1:
                    img_resize_Vertical = ImageOps.grayscale(img_resize_Vertical)

                elif Modify == 2:
                    enhancer = ImageEnhance.Brightness(img_resize_Vertical)
                    
                    factor = 50
                    
                    Level = 1 + (factor/100)         #brightens the image
                    
                    img_resize_Vertical = enhancer.enhance(Level)

                Output_Vertical_Name = f"D:Saved Images\Photo_Vertical_{i}.jpg" # Determine filename in Resize save in the folder Saved Images
                LIST.append(Output_Vertical_Name) # store image in list
                img_resize_Vertical.save(Output_Vertical_Name) 

        elif self.Mode == 2: # Mode 1 = Vertical, Mode 2 = Horizontal
            for i in range(6): 
                InputName = self.Images[i]   

                img = Image.open(InputName) # open image
                img_resize_Horizontal = img.resize((int(Horizontal_x), int(Horizontal_y))) 

                if Modify == 1:
                    img_resize_Horizontal = ImageOps.grayscale(img_resize_Horizontal)

                elif Modify == 2:
                    enhancer = ImageEnhance.Brightness(img_resize_Horizontal)
                    
                    factor = 50
                    
                    Level = 1 + (factor/100)         #brightens the image
                    
                    img_resize_Horizontal = enhancer.enhance(Level)

                Output_Horizontal_Name = f"D:Saved Images\Photo_Horizontal_{i}.jpg" 
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
                y += self.new_size_y + self.space_y  ]
                x = 0 
                
        background.save(self.Output) 



        

IMAGE = ["D:\Saved Images\Photo_0.jpg",   # dont forget to comment this list
         "D:\Saved Images\Photo_1.jpg",
         "D:\Saved Images\Photo_2.jpg",
         "D:\Saved Images\Photo_3.jpg",
         "D:\Saved Images\Photo_4.jpg",
         "D:\Saved Images\Photo_5.jpg"
         ]

Mode = 1 # Mode 1 = Vertical, Mode 2 = Horizontal
Frame = 1 # choose Frame Image
Modify = 2 # choose Grayscale or Brightness
Output_IMAGE = "D:\Output Image\Posted_Image.png" # naming Output file


Process = ImageProcessing(IMAGE, Mode, Frame, Output_IMAGE)
IMAGE_Resize = Process.Resize_Image(Modify) # call resize function
Process.combine_images(Images=IMAGE_Resize) # call combine function


