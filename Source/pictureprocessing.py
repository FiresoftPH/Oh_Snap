from PIL import Image

def Resize_Image(LIST, Horizontal_x, Horizontal_y, Vertical_x, Vertical_y):
    LIST_1 = [] 
    LIST_2 = [] 
    
    for i in range(6): 
        InputName = LIST[i] 
        Output_Horizontal_Name = f"D:Saved Images\Photo_Horizontal_{i}.jpg" 
        Output_Vertical_Name = f"D:Saved Images\Photo_Vertical_{i}.jpg" 
        LIST_1.append(Output_Horizontal_Name) 
        LIST_2.append(Output_Vertical_Name) 
        
        img = Image.open(InputName) 
        img_resize_Horizontal = img.resize((int(Horizontal_x), int(Horizontal_y))) 
        img_resize_Vertical = img.resize((int(Vertical_x), int(Vertical_y))) 
        img_resize_Horizontal.save(Output_Horizontal_Name) 
        img_resize_Vertical.save(Output_Vertical_Name) 
    return LIST_1, LIST_2

def combine_images(columns, BG_width, BG_height, BG_color, new_size_x, new_size_y, space_x, space_y, x_offset, y_offset, image_name, images, BG):
    #background = Image.new('RGBA', (BG_width, BG_height), BG_color) # create Image Background
    background = BG

    x = 0 
    y = 0 
    for i, image in enumerate(images): 
        img = Image.open(image) 
        
        background.paste(img, (x + x_offset, y + y_offset)) 
        x += new_size_x + space_x 
        
        if (i + 1) % columns == 0: 
            y += new_size_y + space_y  
            x = 0 
            
    background.save(image_name) 

IMAGE = ["D:\Saved Images\Photo_0.jpg",  
         "D:\Saved Images\Photo_1.jpg",
         "D:\Saved Images\Photo_2.jpg",
         "D:\Saved Images\Photo_3.jpg",
         "D:\Saved Images\Photo_4.jpg",
         "D:\Saved Images\Photo_5.jpg"
         ]

#IMAGE = Selected_images     # dont forget to delete # out


# resize function
IMAGE_Horizontal_Resize, IMAGE_Vertical_Resize = Resize_Image(list(IMAGE), Horizontal_x=512, Horizontal_y=320, Vertical_x=556.8, Vertical_y=348)

Output_IMAGE_Horizontal = "D:\Output Image\Posted_Image_Horizontal.png" 
Output_IMAGE_Vertical = "D:\Output Image\Posted_Image_Vertical.png" 

BG_Image_Horizontal = Image.open("D:\Saved Images\LIGHTBLUE.png") # Background Image
BG_Image_Vertical = Image.open("D:\Saved Images\PASTELGRADIENT.png") # Background Image
BG_resize_Horizontal = BG_Image_Horizontal.resize((1665, 1100)) 
BG_resize_Vertical = BG_Image_Vertical.resize((1240, 1432)) 


# combine function
combine_images(columns=3, BG_width=1665, BG_height=1100, BG_color=(255, 99, 71, 100),
               new_size_x=512, new_size_y=320, space_x=23, space_y=123, x_offset=40, y_offset=232,
               image_name=Output_IMAGE_Horizontal, images=IMAGE_Horizontal_Resize,
               BG=BG_resize_Horizontal)

combine_images(columns=2, BG_width=1240, BG_height=1432, BG_color=(255, 99, 71, 100),
               new_size_x=557, new_size_y=348, space_x=22, space_y=23, x_offset=52, y_offset=220,
               image_name=Output_IMAGE_Vertical,images=IMAGE_Vertical_Resize,
               BG=BG_resize_Vertical)
