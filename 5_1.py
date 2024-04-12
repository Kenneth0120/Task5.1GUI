from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

# Setup GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
LED_PINS = {'red': 17, 'green': 27, 'blue': 22}
leds = {color: LED(pin) for color, pin in LED_PINS.items()}

# Initialize main window
win = Tk()
win.title("LED Toggler")
win.geometry("300x200")  # Set initial size of the window
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

def toggle_led(led, button):
    if led.is_lit:
        led.off()
        button["text"] = f"Turn {button['text'].split()[1]} On"
    else:
        led.on()
        button["text"] = f"Turn {button['text'].split()[1]} Off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Initialize buttons dictionary
buttons = {}

# Generate buttons for each LED
for color, led in leds.items():
    # Create the button and add to the window
    button = Button(win, text=f'Turn {color.upper()} On', font=myFont, 
                    command=lambda led=led, color=color: toggle_led(led, buttons[color]), 
                    bg='bisque2', height=1, width=24)
    button.grid(row=len(buttons), column=1, padx=10, pady=10)
    buttons[color] = button

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='green', height=2, width=6)
exitButton.grid(row=len(buttons), column=1, pady=10)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
