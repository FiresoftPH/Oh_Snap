import customtkinter
from PIL import Image, ImageTk
app = customtkinter.CTk()
app.geometry("1280x800")

frame = customtkinter.CTkFrame(master = app,
                               width = 1280,
                               height = 800)

frame.pack()

buttonArray = {}
def makeButton():
    for count in range(3):
        def buttonCommand(index = count):
            print(index)

        buttonArray[count] = customtkinter.CTkButton(master = frame, text = count, command = buttonCommand)
        buttonArray[count].pack()


makeButton()

app.mainloop()