# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 21:55:15 2023

@author: USER
"""

import guilib as obj

state = {
    "textbox": None,
    "points": [] 
}

def choose_point(event):
    # Access the x and y data values from the MouseEvent object
    x = event.xdata
    y = event.ydata

    # Print the values into the textbox
    message = f"Value at x={x:.2f} is y={y:.2f}\n"
    obj.write_to_textbox(state["textbox"], message)

    # Save the point to the points list in the state dictionary
    state["points"].append((x, y)) 
    
def main(datax, datay):
    # Create the window
    window = obj.create_window("pointing")

    # Create the main frame
    lower_frame = obj.create_frame(window, side = obj.BOTTOM)

    # Create the upper frame for the figure
    upper_frame = obj.create_frame(window, side = obj.TOP)

    # Create the figure and add it to the upper frame
    canvas,figure, subplot = obj.create_figure(upper_frame, choose_point, 500, 500)
    subplot.plot(datax, datay, 'blue')
    canvas.draw()

    # Create the textbox and assign it to the state dictionary
    textbox = obj.create_textbox(lower_frame)
    state["textbox"] = textbox 

    # Start the program
    obj.start()
    
    
if __name__ == "__main__":
    datax = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    datay = [0.0, 0.19, 0.36, 0.51, 0.64, 0.75, 0.84, 0.91, 0.96, 0.99, 1.0, 0.99, 0.96, 0.91, 0.84, 0.75, 0.64, 0.51, 0.36, 0.19, 0.0]
    main(datax, datay)
    