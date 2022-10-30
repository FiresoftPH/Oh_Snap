from PIL import Image, ImageTk
import customtkinter

window = customtkinter.CTk()

label = customtkinter.CTkLabel(master = window, image = None)
def test_fun(index):

    number_to_text = {5: "Five", 4: "Four", 3: "Three", 2: "Two", 1: "One"}
    image_index = number_to_text[index]
    image_directory = "Pictures\Countdown_display\{}.png".format(image_index)
    print(image_directory)
    print("Pictures\Countdown_display\Five.png")
    test_1 = Image.open(image_directory)
    test_2 = ImageTk.PhotoImage(test_1)
    label.configure(image = test_2)
    label.image = test_2

test_fun(5)

label.pack()
window.mainloop()