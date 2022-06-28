# Program to make a simple
# login screen 
 
 

import tkinter as tk

  
root=tk.Tk()
 
# setting the windows size
root.geometry("630x100")

  
# defining some required variables

voltage = tk.DoubleVar()
discharge_time = ("")


# defining a function that will
# get the volt
# print them on the screen

def volt_return():
    result.config(text = "")
    voltage = volt_entry.get()
    if voltage == ("11"):
        print("working")
    if voltage <= ('3.64'):
        result.config(text = "Node below voltage please charge node.")
    if voltage >= ('3.65') and voltage <= ('3.85'):
        result.config(text = "Node within charging range please ship.")
    if voltage == ('3.86'):
        result.config(text = "Node should take approximately 2 and a half hours to discharge.")
    if voltage == ('3.87'):
        result.config(text = "Node should take approximately 5 hours to discharge.")
    if voltage == ('3.88'):
        result.config(text = "Node should take approximately 7 and a half hours to discharge.")
    if voltage == ('3.89'):
        result.config(text = "Node should take approximately 10 hours to discharge.")
    if voltage == ('3.90'):
        result.config(text = "Node should take approximately 12 and a half hours to discharge.")
    if voltage == ('3.91'):
        result.config(text = "Node should take approximately 15 hours to discharge.")
    if voltage == ('3.92'):
        result.config(text = "Node should take approximately 17 and a half hours to discharge.")
    if voltage == ('3.93'):
        result.config(text = "Node should take approximately 20 hours to discharge.")
    if voltage == ('3.94'):
        result.config(text = "Node should take approximately 22 and a half hours to discharge.")
    if voltage >= ('3.95'):
        result.config(text = 'Node should take approximately over 24 hours to discharge, recheck tommorow.')



# creating a label for
# volt using widget Label
volt_label = tk.Label(root, text = 'Voltage', font=('calibre',10, 'bold'))

# creating a label for
# volt using widget Label

volt_label2 = tk.Label(root, text = 'Voltage', font=('calibre',10, 'bold'))

# creating a entry for input
# volt using widget Entry

volt_entry = tk.Entry(root, textvariable= 'voltage' )


#creating a label for the output based on voltage

result = tk.Label(root, text = (discharge_time))

# creating a button using the widget
# Button that will call the submit function

sub_btn=tk.Button(root, text = 'Submit', command = volt_return)

#defining submit function to output text based on voltage


# placing the label entry and result in
# the required position using grid
# method


volt_label.grid(row=0,column=0)
volt_entry.grid(row=0, column=1)
result.grid(row= 2, column = 2)
sub_btn.grid(row=1,column=1)

# performing an infinite loop
# for the window to display


root.mainloop()