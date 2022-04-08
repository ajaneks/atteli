# importing the tkinter module and PIL
# that is pillow module
#from ctypes import alignment, resize
#from sqlite3 import PARSE_DECLTYPES
from tkinter import *
from PIL import ImageTk, Image

image = Image.open('1.jpg')
new_image = image.resize((600,400))
new_image.save('11.jpg')

image = Image.open('2.jpg')
new_image = image.resize((400, 400))
new_image.save('22.jpg')

image = Image.open('3.jpg')
new_image = image.resize((600,400))
new_image.save('33.jpg')

image = Image.open('4.jpg')
new_image = image.resize((600,400))
new_image.save('44.jpg')

image = Image.open('5.jpg')
new_image = image.resize((250,400))
new_image.save('55.jpg')

image = Image.open('6.jpg')
new_image = image.resize((650,400))
new_image.save('66.jpg')

image = Image.open('7.jpg')
new_image = image.resize((300,400))
new_image.save('77.jpg')

image = Image.open('8.jpg')
new_image = image.resize((400,400))
new_image.save('88.jpg')



def forward(img_no):

	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	label = Label(image=List_images[img_no-1])

	label.grid(row=1, column=0, columnspan=3)
	button_for = Button(root, text="Talak", command=lambda: forward(img_no+1))

	if img_no == 4:
		button_forward = Button(root, text="Talak",state=DISABLED)

	button_back = Button(root, text="Atpakal",command=lambda: back(img_no-1))

	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)



def back(img_no):

	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	label = Label(image=List_images[img_no - 1])
	label.grid(row=1, column=0, columnspan=3)
	button_forward = Button(root, text="Talak",
							command=lambda: forward(img_no + 1))
	button_back = Button(root, text="Atpakal",
						command=lambda: back(img_no - 1))
	print(img_no)

	if img_no == 1:
		button_back = Button(root, Text="Atpakal", state=DISABLED)

	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_forward.grid(row=5, column=2)



root = Tk()
root.resizable(1,1)
root.title("Attēlu apskatītājs")
#root.grid(padx=10, pady=10)

root.geometry("700x450")


#frame=Frame(root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
#frame.pack(padx=10, pady=10)

image_no_1 = ImageTk.PhotoImage(Image.open("11.jpg"))
image_no_2 = ImageTk.PhotoImage(Image.open("22.jpg"))
image_no_3 = ImageTk.PhotoImage(Image.open("33.jpg"))
image_no_4 = ImageTk.PhotoImage(Image.open("44.jpg"))
image_no_5 = ImageTk.PhotoImage(Image.open("55.jpg"))
image_no_6 = ImageTk.PhotoImage(Image.open("66.jpg"))
image_no_7 = ImageTk.PhotoImage(Image.open("77.jpg"))
image_no_8 = ImageTk.PhotoImage(Image.open("88.jpg"))

List_images = [image_no_1, image_no_2, image_no_3, image_no_4, image_no_5, image_no_6, image_no_7, image_no_8]
label = Label(image=image_no_1)
label.grid(padx=(100, 100), pady=(0, 0))
#label.grid(row=1, column=0, columnspan=3)


#     POGAS

button_back = Button(root, text="Atpakal", command=back, state=DISABLED)
button_exit = Button(root, text="Iziet", command=root.quit)
button_forward = Button(root, text="Talak", command=lambda: forward(1))




button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

root.mainloop()
