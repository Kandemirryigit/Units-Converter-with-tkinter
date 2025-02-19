import tkinter as tk   # To use tkinter we should import this
from tkinter import messagebox  # To use pop-up we should import this


window=tk.Tk()  # To define window
window.title("Units Converter")  # To determine window's title
window.minsize(400,300)  # To determine window's size
window.config(bg="#524C42")  # To determine window's background color


# To create texts and give them a specific location,background color,foreground color,font

title_text=tk.Label(text="Unit Converter",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
title_text.grid(column=1,row=1)

convert_text=tk.Label(text="Convert:",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
convert_text.grid(column=0,row=2,pady=30)

result_text=tk.Label(text="Result:",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
result_text.grid(column=0,row=5)

result=tk.Label(text="-",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
result.grid(column=1,row=5)

to_text=tk.Label(text="To:",fg="#E2DFD0",bg="#524C42",font=("Monospace",18,"bold"))
to_text.grid(column=0,row=3)


# to create Input and give it a specific location

first_number_entry=tk.Entry()
first_number_entry.grid(column=1,row=2)


# To determine a default value to our menu

unit1=tk.StringVar()
unit1.set("km")

unit2=tk.StringVar()
unit2.set("m")

# To create a menu

unit1_menu=tk.OptionMenu(window,unit1,"km","hm","dam","m","dm","cm","mm")
unit1_menu.config(bg="white",fg="black",highlightthickness=0)
unit1_menu.grid(column=2,row=2)

unit2_menu=tk.OptionMenu(window,unit2,"km","hm","dam","m","dm","cm","mm")
unit2_menu.config(bg="white",fg="black",highlightthickness=0)
unit2_menu.grid(column=1,row=3)


# Formats a number with a dot every 3 digits from the right
def format_number_with_dots(number):
    return "{:,}".format(number).replace(",", ".")


def get_convert():
    # If we don't write a number or we don't write anything inside input we are gonna see a pop-up in the screen
    try:
        first_number=float(first_number_entry.get())
    except ValueError:
        messagebox.showinfo(title="Error",message="please Enter a Valid Number")
    
    first_unit=unit1.get()  # To get first unit's value
    second_unit=unit2.get() # To get second unit's value

    # To determine our operations for every single situation
    conversion_factors = {
        "km": {"km": 1, "hm": 10, "dam": 100,"m":1000,"dm":10000,"cm":100000,"mm":1000000},
        "hm": {"km":0.1,"hm":1,"dam":10,"m":100,"dm":1000,"cm":10000,"mm":100000},
        "dam":{"km":0.01,"hm":0.1,"dam":1,"m":10,"dm":100,"cm":1000,"mm":10000},
        "m":{"km":0.001,"hm":0.01,"dam":0.1,"m":1,"dm":10,"cm":100,"mm":1000},
        "dm":{"km":0.0001,"hm":0.001,"dam":0.01,"m":0.1,"dm":1,"cm":10,"mm":100},
        "cm":{"km":0.00001,"hm":0.0001,"dam":0.001,"m":0.01,"dm":0.1,"cm":1,"mm":10},
        "mm":{"km":0.000001,"hm":0.00001,"dam":0.0001,"m":0.001,"dm":0.01,"cm":0.1,"mm":1}
        }


    if first_unit in conversion_factors and second_unit in conversion_factors[first_unit]:
        end = first_number * conversion_factors[first_unit][second_unit]
        formatted_end = format_number_with_dots(round(end, 2))
        result.config(text=f"{formatted_end} {second_unit}")
    
# To create a button and give it a specific location,text,width,command
convert_button=tk.Button(text="Convert",width=30,command=get_convert)
convert_button.grid(column=1,row=4,pady=30)

window.mainloop()  # If I don't click exit button the screen won't close