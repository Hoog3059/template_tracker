import sys
import os
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import cv2 as cv
import numpy as np
from PIL import Image, ImageTk


clicks = []
line = None
text = None
real_distance_input = None
canvas = None
rod_line = None
rod_text = None


def main():
    global real_distance_input, canvas
    window = tk.Tk()

    video_path = filedialog.askopenfilename()

    cap = cv.VideoCapture(video_path)
    frame_available, frame = cap.read()
    cap.release()
    if not frame_available:
        # Error
        pass

    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame = ImageTk.PhotoImage(frame)

    canvas = tk.Canvas(window, width=frame.width(), height=frame.height())
    image_object = canvas.create_image(0, 0, anchor=tk.NW, image=frame)
    canvas.tag_bind(image_object, '<Button-1>', canvas_onclick_measure_scale)
    canvas.tag_bind(image_object, '<Button-3>', canvas_onclick_measure_rod)
    canvas.pack()

    real_distance_input = tk.Entry()
    real_distance_input.pack()

    scale_button = tk.Button(text="Give scale")
    scale_button.bind("<Button-1>", scale_button_onclick)
    scale_button.pack()

    reset_button = tk.Button(text="Reset")
    reset_button.bind("<Button-1>", restart)
    reset_button.pack()
    window.mainloop()


def restart(event):
    python = sys.executable
    os.execl(python, python, * sys.argv)


def scale_button_onclick(event):
    global real_distance_input, clicks

    real_distance = float(real_distance_input.get())
    pixel_distance = ((clicks[0][0] - clicks[1][0])**2 + (clicks[0][1] - clicks[1][1])**2)**0.5

    scale_value = pixel_distance / real_distance
    messagebox.showinfo("Result", f"Scale = {scale_value} pixels/meter")


def canvas_onclick_measure_scale(event):
    global clicks, line, text

    clicks.append((event.x, event.y))

    if len(clicks) == 2:
        event.widget.delete(line)
        line = event.widget.create_line(*clicks[0], *clicks[1], fill="red")

        distance = ((clicks[0][0] - clicks[1][0])**2 + (clicks[0][1] - clicks[1][1])**2)**0.5

        event.widget.delete(text)
        text = event.widget.create_text(0, 0, anchor=tk.NW, fill="red", font="Times 20 bold", text=f"{distance}")
    elif len(clicks) == 3:
        clicks = clicks[-1:]


def canvas_onclick_measure_rod(event):
    global rod_line, rod_text

    event.widget.delete(rod_line)

    begin_pos = (0, event.y)
    end_pos = (event.x, event.y)

    rod_line = event.widget.create_line(*begin_pos, *end_pos, fill="orange")

    event.widget.delete(rod_text)
    rod_text = event.widget.create_text(0, 100, anchor=tk.NW, fill="orange", font="Times 20 bold", text=f"{event.x}")


if __name__ == "__main__":
    main()
