import tkinter as tk
from PIL import Image, ImageTk


########################################################
# Koodi genereeris ChatGPT
#######################################################

class ImageCropper:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.image = image
        self.photo_image = ImageTk.PhotoImage(image)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        self.rect = None
        self.start_x = None
        self.start_y = None
        self.cur_x = None
        self.cur_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        # Save the starting position of the rectangle
        self.start_x = event.x
        self.start_y = event.y

        # Create a rectangle if not yet created
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y,
                                                     outline='red')

    def on_mouse_drag(self, event):
        # Update the current position as the mouse is dragged
        self.cur_x, self.cur_y = (event.x, event.y)

        # Update the rectangle's size
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.cur_x, self.cur_y)

    def on_button_release(self, event):
        # Get the end position of the rectangle
        end_x, end_y = (event.x, event.y)

        # Crop the image based on the rectangle's coordinates
        self.crop_image(self.start_x, self.start_y, end_x, end_y)

    def crop_image(self, start_x, start_y, end_x, end_y):
        # Ensure the coordinates are within the image bounds
        start_x, start_y = max(0, start_x), max(0, start_y)
        end_x, end_y = min(self.image.width, end_x), min(self.image.height, end_y)

        # Calculate the coordinates of the rectangle
        left = min(start_x, end_x)
        upper = min(start_y, end_y)
        right = max(start_x, end_x)
        lower = max(start_y, end_y)

        # Crop the image
        cropped_image = self.image.crop((left, upper, right, lower))

        # Update the canvas with the cropped image
        self.update_canvas(cropped_image)

    def update_canvas(self, cropped_image):
        # Clear the canvas
        self.canvas.delete("all")

        # Update the image and canvas
        self.photo_image = ImageTk.PhotoImage(cropped_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        # Resize the canvas to fit the new image
        self.canvas.config(width=cropped_image.width, height=cropped_image.height)
