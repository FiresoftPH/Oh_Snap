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

        elif self.Mode == 2:
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
            
            BG_Image_Vertical = Image.open("D:\Saved Images\BLACK_Vertical.png") 
            self.BG = BG_Image_Vertical.resize((1240, 1432)) 

    
    def Resize_Image(self, Modify):
        LIST = [] # blank list to store resize picture

        Horizontal_x = 512
        Horizontal_y = 320
        Vertical_x = 556.8
        Vertical_y = 348
        
        if self.Mode == 1: # Mode 1 = Vertical, Mode 2 = Horizontal
            for i in range(6): 
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

                Output_Vertical_Name = f"D:Saved Images\Photo_Vertical_{i}.jpg" # กำหนดชื่อไฟล์รูปหลังจาก Resize save ลงในโฟลเดอร์ Saved Images
                LIST.append(Output_Vertical_Name) # เก็บชื่อรูปเข้า List
                img_resize_Vertical.save(Output_Vertical_Name) # Save imgae แนวนอน

        elif self.Mode == 2: # โหมด 1 คือแนวตั้ง โหมด 2 คือ แนวนอน
            for i in range(6): # วนลูป Resize image 6 รูป
                InputName = self.Images[i] # ดึงรูปมาทีละ index ใน List   

                img = Image.open(InputName) # open image
                img_resize_Horizontal = img.resize((int(Horizontal_x), int(Horizontal_y))) # Resize แนวนอน

                if Modify == 1:
                    img_resize_Horizontal = ImageOps.grayscale(img_resize_Horizontal)

                elif Modify == 2:
                    enhancer = ImageEnhance.Brightness(img_resize_Horizontal)
                    
                    factor = 50
                    
                    Level = 1 + (factor/100)         #brightens the image
                    
                    img_resize_Horizontal = enhancer.enhance(Level)

                Output_Horizontal_Name = f"D:Saved Images\Photo_Horizontal_{i}.jpg" # กำหนดชื่อไฟล์รูปหลังจาก Resize save ลงในโฟลเดอร์ Saved Images
                LIST.append(Output_Horizontal_Name) # เก็บชื่อรูปเข้า List
                
                img_resize_Horizontal.save(Output_Horizontal_Name) # Save imgae แนวนอน


        else:
            print("Mode Error")

        return LIST

    def combine_images(self, Images):
        background = self.BG

        x = 0 # ค่า Pixel แกน X เริ่มต้น
        y = 0 # ค่า Pixel แกน Y เริ่มต้น
        for i, image in enumerate(Images): # วนลูปดึง Image จากใน List มาทีละรูป
            img = Image.open(image) # open image
            
            background.paste(img, (x + self.x_offset, y + self.y_offset)) # วางรูปที่ถ่ายมา ลงบน Background Image ที่ละรูป
            x += self.new_size_x + self.space_x # เปลี่ยนค่าตำแหน่งแกน X ในการวางรูป ไปที่บล็อกถัดไป
            
            if (i + 1) % self.columns == 0: # วางตามค่า Column ที่รับมา
                y += self.new_size_y + self.space_y  # เปลี่ยนค่าตำแหน่งแกน Y ในการวางรูป ไปที่บล็อกถัดไป
                x = 0 # เมื่อวางครบตามเลข Column ที่รับมา ให้ขึ้นบรรทัดใหม่
                
        background.save(self.Output) # เมื่อวางครบ 6 รูป ให้ Save Image ลงใน Path ตามค่า image_name



        

IMAGE = ["D:\Saved Images\Photo_0.jpg",   # ตอนไปเชื่อมต่อกับเพื่อน ให้ Comment List นี้
         "D:\Saved Images\Photo_1.jpg",
         "D:\Saved Images\Photo_2.jpg",
         "D:\Saved Images\Photo_3.jpg",
         "D:\Saved Images\Photo_4.jpg",
         "D:\Saved Images\Photo_5.jpg"
         ]

Mode = 1 # โหมด 1 คือแนวตั้ง โหมด 2 คือ แนวนอน
Frame = 1 # เลือก Frame Image
Modify = 2 # เลือกปรับ Grayscale หรือ Brightness
Output_IMAGE = "D:\Output Image\Posted_Image.png" # ชื่อไฟล์ Output 


Process = ImageProcessing(IMAGE, Mode, Frame, Output_IMAGE)
IMAGE_Resize = Process.Resize_Image(Modify) # เรียกใช้ฟังก์ชั่น resize
Process.combine_images(Images=IMAGE_Resize) # เรียกใช้ฟังก์ชั่นรวมรูป


