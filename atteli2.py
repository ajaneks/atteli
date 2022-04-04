from tkinter import *
from PIL import ImageTk, Image
#from matplotlib import image

root=Tk()
root.title("Attēlu apskate")

image = Image.open('1.jpg')
new_image = image.resize((400, 400))
new_image.save('11.jpg')

image = Image.open('2.jpg')
new_image = image.resize((400, 400))
new_image.save('22.jpg')

image = Image.open('3.jpg')
new_image = image.resize((400, 400))
new_image.save('33.jpg')

image = Image.open('4.jpg')
new_image = image.resize((400, 400))
new_image.save('44.jpg')

image = Image.open('5.jpg')
new_image = image.resize((400, 400))
new_image.save('55.jpg')

image = Image.open('6.jpg')
new_image = image.resize((400, 400))
new_image.save('66.jpg')

image = Image.open('7.jpg')
new_image = image.resize((400, 400))
new_image.save('77.jpg')

image = Image.open('8.jpg')
new_image = image.resize((400, 400))
new_image.save('88.jpg')

image_no_1 = ImageTk.PhotoImage(Image.open("1.jpg"))
image_no_2 = ImageTk.PhotoImage(Image.open("2.jpg"))
image_no_3 = ImageTk.PhotoImage(Image.open("3.jpg"))
image_no_4 = ImageTk.PhotoImage(Image.open("4.jpg"))
image_no_5 = ImageTk.PhotoImage(Image.open("5.jpg"))
image_no_6 = ImageTk.PhotoImage(Image.open("6.jpg"))
image_no_7 = ImageTk.PhotoImage(Image.open("7.jpg"))
image_no_8 = ImageTk.PhotoImage(Image.open("8.jpg"))

List_images = [image_no_1, image_no_2, image_no_3, image_no_4, image_no_5, image_no_6, image_no_7, image_no_8]
label=Label(image=image_no_1)


def forward(img_no):

	# GLobal variable so that we can have
	# access and change the variable
	# whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# This is for clearing the screen so that
	# our next image can pop up
	label = Label(image=List_images[img_no-1])

	# as the list starts from 0 so we are
	# subtracting one
	label.grid(row=1, column=0, columnspan=3)
	button_for = Button(root, text="forward", command=lambda: forward(img_no+1))

	# img_no+1 as we want the next image to pop up
	if img_no == 4:
		button_forward = Button(root, text="Forward",state=DISABLED)

	# img_no-1 as we want previous image when we click
	# back button
	button_back = Button(root, text="Back",command=lambda: back(img_no-1))

	# Placing the button in new grid
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)


def back(img_no):

	# We will have global variable to access these
	# variable and change whenever needed
	global label
	global button_forward
	global button_back
	global button_exit
	label.grid_forget()

	# for clearing the image for new image to pop up
	label = Label(image=List_images[img_no - 1])
	label.grid(row=1, column=0, columnspan=3)
	button_forward = Button(root, text="forward",
							command=lambda: forward(img_no + 1))
	button_back = Button(root, text="Back",
						command=lambda: back(img_no - 1))
	print(img_no)

	# whenever the first image will be there we will
	# have the back button disabled
	if img_no == 1:
		button_back = Button(root, Text="Back", state=DISABLED)

	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_forward.grid(row=5, column=2)