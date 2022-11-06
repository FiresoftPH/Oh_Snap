import customtkinter
app = customtkinter.CTk()
def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button = customtkinter.CTkOptionMenu(master=app,
                                                values=["Value 1", "Value 2", "Value 3"],
                                                command=segmented_button_callback)
segemented_button.pack(padx=20, pady=10)
segemented_button.set("Value 1")  # set initial value

app.mainloop()