# Initial Python Top End Setup
# General note to recognize two infuencers that provided the information i needed to complete this project.
# I am new to Python and this is my first program, i do intend to improve on it.
# Thanks go to John Elder at tkinter.com, i watched many of his videos and downloaded his free Python Tkinter
# Widgets Book, so he has provided me with much skill regarding python, i would also like to mention JobinPy,
# another great youtube source on tkinter, very methodical JobinPy.

# dashWoorkZ Sovereign Society was established in 2023, Web Design is one area of which we are interested in
# developing our influence in, Python provides dashWoorkZ Sovereign Society and opertunity to build software
# as another means to provide a service or product in demand. dashWoorkZ Sovereign Society plans to improve
# the functionality of the TempCal v.001 program as well as to introduce similar programs suitable for DIY
# enthusiasists and engineers alike. Our website at http://dashwoorkz.ca/ is currently inre-construction, 
# we hope to have it completed very soon, we are excited about the future and look forward to providing 
# quality service and products in the years to com. God Bless and thank you for using our first Python 
# program releas, TempCalc v.001.

# If you find this program useful and would like to assist us in our endeauvours, you can Email us directly
# at dashwoorkz@dashwoorkz.ca and we would be happy to discuss your contribution, or you can E-Transfer directly
# to our Managing Director :Dash: La Londe at dash@dashwoorkz.ca.

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#Main Window
window = tk.Tk()
window.title("dashWoorkZ - TempCalc v.001")
window.geometry("400x500")
window.configure(background="#a1a1d9")
style=ttk.Style()   # ttk Style Library
menu = tk.Menu(window)


def changetheme():
    themeval=themevar.get()
    style.theme_use(themeval)

themevar=StringVar()
themevar.set("clam")

# subMenu
apps_menu = tk.Menu(menu, tearoff = False)
apps_menu.add_command(label = "Open  TempCalc", command = lambda: openTemp())
apps_menu.add_command(label = "Close  TempCalc", command = lambda: hideTemp())
apps_menu.add_command(label = "Exit", command = lambda: quit_main())
menu.add_cascade(label = "Apps", menu = apps_menu)

global choice
global temp
global current
sct = ["Celcius", "Kelvin", "Fahrenheit", "Rankine"]

# cel = sct[0]
# kel = sct[1]
# fah = sct[2]
# ran = sct[3]
                                                                                       
         # The "Entry Value"
#ss = scaleSet                  # The "Set Button"
#sl = scalesList[i]                # The Selected Scale

# scale = i


# DWRX Logo Image used in Frame
dwrx_logo = ImageTk.PhotoImage(Image.open("imgs/dwrx_logo_277.png"))
dwrx_logo_label = Label(master = window,image=dwrx_logo)
dwrx_logo_label.configure(relief=RAISED,
        borderwidth=0, highlightthickness=0,
        highlightcolor="#11d611", width=300, 
        highlightbackground="#a1a1d9",
        height=300, background="#a1a1d9")
dwrx_logo_label.place(x=50, y=100)

# Styles Used 
style.configure("scaleset.TButton",
        bg="#e0d5f2", cursor="umbrella", font=("Times New Roman", 12),
        activebackground="#c8bff2", activeforeground="#8317bd",
        highlightbackground="#f2c7b1", highlightcolor="#8317bd",
        highlightthickness=0, takefocus=True,
        justify=CENTER, width=3, fg="#138d96")
        
style.configure("scales.TLabel", activebackground="#c8bff2", 
        activeforeground="#1a2ddb", background="#e0d5f2", 
        bd=5, highlightbackground="#f2c7b1", highlightcolor="#8317bd", 
        highlightthickness=5, justify=CENTER, fg="#1a2ddb")
        
style.configure("button.TLabel", 
	font=("Helvetica", 15, "bold"), 
	foreground="#2c92ff", background="#c7edff", labelanchor='center')
                
style.configure("default.TLabel", 
	font=("Times New Roman", "18", "bold"),
	foreground="#300630", background="#6464dd", labelanchor='center', height='40')

style.configure("footer.TLabel", 
	font=("Times New Roman", "18", "bold"),
	foreground="#300630", background="#6464dd", labelanchor='center', height='40', width="35")
	
style.configure("default.TButton",
	background="skyblue", foreground="#1cc6ff", relief="ridge",
	font="Arial 14 bold", anchor="center", arrowsize=15,
	highlightbackground='#ebd7c8', highlightcolor='#ed24e3',
	highlightthickness=3, takefocus=True, height=2, width=20, overrelief="ridge")

def openTemp():
        main_frame.pack(side="top", expand=True)
        
def hideTemp():
        main_frame.pack_forget()

main_frame = tk.Frame(master = window)
main_frame.configure(background="#c9a7ed",
        relief="ridge", width=300, height=350, highlightbackground='#a7edea',
        highlightcolor='#c9a7ed', highlightthickness=10)
main_frame.pack(side="top", expand=True)

main_label = ttk.Label(master = main_frame)
main_label.configure(style="default.TLabel", text="TempCalc Ver .001", 
        anchor="center", width='23')
main_label.pack(side="top", fill="x", expand=True)

# =======  Scales Selection Frame

def display_selected(scales):
        scales = scale.get()
        scale.set(scales)
        temp = scaleTemp.get()

def setScaleTemp(scales, temp):
        scales = scaleSet[0].get()
        temp = scaleSet[1].get()
        
            
        # kelvin_labelframe_label.configure(style="button.TLabel",text= round(int(temp) + 273.15, 2), width=5, anchor='center')
        # fahrenheit_labelframe_label.configure(style="button.TLabel",text= round((int(temp) * (9/5)) + 32, 2), width=5, anchor='center')
        # rankine_labelframe_label.configure(style="button.TLabel",text= round(int(temp) + 491.67, 2), width=5, anchor='center')
        # celcius_labelframe_label.configure(style="button.TLabel",text= round(int(temp), 2), width=5, anchor='center')
# Math note: Source of information regarding Rounding Numbers in Python : https://bobbyhadz.com/blog/python-round-float-3-decimal-places         
# ++++++++++++++++++++++++++++++ 

# Main Frame
temperature_frame = Frame(master = main_frame, 
        bd=5, bg="#e0d5f2", container=False,
        highlightbackground="#568ef5",
        highlightcolor="#f5e856",
        takefocus=True)
temperature_frame.pack(side="top", fill="x", expand=True)

# Main Frame Label
temperature_frame_label = Label(master = temperature_frame)
temperature_frame_label.configure(text="Python User Interface", 
        font=("Times New Roman", 14), activebackground="#ebd5c3", 
        activeforeground="#ebe8c3", background="#e0d5f2", bd=0, 
        highlightbackground="#568ef5", highlightcolor="#f5e856", 
        highlightthickness=0, justify=CENTER, fg="#b30e98", takefocus=True)
temperature_frame_label.pack(fill="x", expand=True, ipady=5, side="top")

# Temperature Calculator Label
temperature_calculator_label = Label(master = temperature_frame)
temperature_calculator_label.configure(text="Temperature Calculator", 
        font=("Times New Roman", 12), activebackground="#d7eef2", 
        background="#e0d5f2", bd=2, fg="#110c99", relief=SUNKEN,
        highlightbackground="#568ef5", highlightcolor="#f5e856",
        highlightthickness=0, justify=CENTER, takefocus=True, 
        activeforeground="#ebe8c3")
temperature_calculator_label.pack(fill="x", expand=True, ipady=5, side="top")


# =========  Temperature Setting Frame Start

scaleChoice = Frame(master = temperature_frame)
scaleChoice.pack(fill="x", expand=True, ipady=5, side="top")
scaleChoice_label = Label(scaleChoice)
scaleChoice_label.configure(text='Enter a Number To Convert',
                          fg="#138d96", font=("New Times Roman", 10),
                          anchor="center")
scaleChoice_label.pack(fill="x", expand=True, side="top")
                          

temperature_setting_frame = Frame(master = scaleChoice) 
temperature_setting_frame.configure(bg="#e0d5f2", cursor="umbrella", 
        highlightcolor="#f5e856", takefocus=True, width=25)
temperature_setting_frame.pack(side="top", fill="x", expand=True)

scaleSet = tk.Button(master = temperature_setting_frame)
scaleSet.configure(text="Set", cursor="umbrella", bg="#e0d5f2",
        highlightbackground="#f2c7b1", highlightcolor="#f5e856",      
        activebackground="#c8bff2", activeforeground="#8317bd", 
        justify=CENTER, width=3,fg="#138d96", takefocus=True,
        highlightthickness=0, command=setScaleTemp)
scaleSet.pack(side="right", expand=True)

# Scale Temperature Setting
scaleTemp = tk.Entry(master = temperature_setting_frame)
scaleTemp.config(cursor="umbrella", highlightbackground="#f2c7b1",
        highlightcolor="#f5e856", bg="#c8bff2", fg="#138d96",
        takefocus=True, justify=CENTER, width=3, font=14,  textvariable=scaleTemp) 
scaleTemp.pack(side="right", expand=True)


# creating Option Menu widget
scaleSet = ['Scale Setting','Celcius','Fahrenheit', 'Kelvin', 'Rankine']

# setting variable for Integers and Strings
scale = StringVar()
scale.set(scaleSet[1])

scales = OptionMenu(
    temperature_setting_frame,
    scale,
    *scaleSet,
    command=display_selected)

scales.config(activebackground="#c8bff2",
        activeforeground="#8317bd", anchor=CENTER, cursor="umbrella",
        direction="below", width=11, highlightbackground="#f2c7b1",
        highlightcolor="#8317bd", highlightthickness=0, textvariable=scales,
        indicatoron=1, takefocus=True, fg="#138d96")
    
# positioning widget
scales.pack(side="left", fill="x", expand=True)  



sl = ["Celcius", "Kelvin", "Fahrenheit", "Rankine"]
i = 0

if  scale == sl[i] and sl[i] == sct[i]:
    sl[scale].converted_scales_frame.pack(fill='y', expand=True, side='top')
    current = sl[scale]
    st = scaleTemp.get()

# ========== Temperature Setting Frame Complete

# ====== Scales Conversion Frame 
scales_response_frame = tk.Frame(master = scaleChoice)
scales_response_frame.configure(background="#d0c7ff",
relief="ridge", width='120', highlightbackground='#1a2ddb',
highlightcolor='#c9a7ed', highlightthickness=3)
scales_response_frame.pack(side="top", fill="x", expand=True)

default_label = ttk.Label(master = scales_response_frame)
default_label.configure(style="scales.TLabel", text="Scales Response", width=15, anchor='center')
default_label.pack(fill='both', expand=True)

conversion_frame = tk.Frame(master =  scales_response_frame)
conversion_frame.configure(background="#2ecbff",
relief="ridge", width=15, highlightbackground='#a7edea',
highlightcolor='#c9a7ed', highlightthickness=3)
conversion_frame.pack(fill='both', expand=True)

setTemp = IntVar()
temp = 0

def setTemp(setTemp):
    scaletemp = round(setTemp)
       
#Converted Scales Frame
converted_scales_frame = tk.Frame(master = conversion_frame)
converted_scales_frame.configure(background="#2ecbff",
relief="sunken", width='23', highlightbackground='#a7edea',
highlightcolor='#c9a7ed', highlightthickness=3)
converted_scales_frame.pack(fill='both', expand=True, ipadx=3, ipady=5, side="bottom")

# Converted Scale Kelvin
kelvin_labelframe = ttk.Labelframe(master = converted_scales_frame)
kelvin_labelframe.configure(style="scales.TLabel", text= sct[1], width=5)
kelvin_labelframe.pack(fill='both', expand=True, side='left', padx=2)

kelvin_labelframe_label = ttk.Label(master = kelvin_labelframe)
kelvin_labelframe_label.configure(temp, style="button.TLabel",text= sct[i][1], width=5, anchor='center')
kelvin_labelframe_label.pack(fill='both', expand=True, side='bottom')

# Converted Scale Fahrenheit
fahrenheit_labelframe = ttk.Labelframe(master = converted_scales_frame)
fahrenheit_labelframe.configure(scales, style="scales.TLabel", text= sct[2], width=5, textvariable=scales)
fahrenheit_labelframe.pack(fill='both', expand=True, side='bottom', pady=3, padx=2)

fahrenheit_labelframe_label = ttk.Label(fahrenheit_labelframe)
fahrenheit_labelframe_label.configure(temp, style="button.TLabel",text= sct[i][2], width=5, anchor='center')
fahrenheit_labelframe_label.pack(fill='both', expand=True, side='bottom')

# Converted Scale Rankine
rankine_labelframe = ttk.Labelframe(master = converted_scales_frame)
rankine_labelframe.configure(style="scales.TLabel", text= sct[3], width=5)
rankine_labelframe.pack(fill='both', expand=True, side='right', padx=2)

rankine_labelframe_label = ttk.Label(rankine_labelframe)
rankine_labelframe_label.configure(style="button.TLabel",text= sct[i][3], width=5, anchor='center')
rankine_labelframe_label.pack(fill='both', expand=True, side='bottom')

# Converted Scale Celcius
celcius_labelframe = ttk.Labelframe(master = converted_scales_frame)
celcius_labelframe.configure(style="scales.TLabel",text= sct[0], width=5)
celcius_labelframe.pack(fill='y', expand=True, side='top')

celcius_labelframe_label = ttk.Label(celcius_labelframe)
celcius_labelframe_label.configure(style="button.TLabel",text= sct[i][0], width=5, anchor='center')
celcius_labelframe_label.pack(fill='both', expand=True, side='bottom')

# End of Scales Resonse
    
footer_frame = tk.Frame(master = scaleChoice)
footer_frame.configure(background="#2ecbff",
        relief="raised", width='23', highlightbackground='#a7edea',
        highlightcolor='#c9a7ed', highlightthickness=3)
footer_frame.pack(side="bottom", fill="x", expand=True)
#  Create a button with cool options

closeApp_button = ttk.Button(master = footer_frame, style="default.TButton")
closeApp_button.configure(text="Close TempCalc!", command=hideTemp)
closeApp_button.pack(side="bottom", fill="x", expand=True)

# My policy is "I am a sovereign and all rights reserved"
policy_frame_label = ttk.Label(master = main_frame)
policy_frame_label.configure(style="footer.TLabel", 
        text="dashWoorkZ Sovereign Society", 
        font=("Times New Roman", '12'),
        anchor="center", justify="center")
policy_frame_label.pack(side="bottom", fill="x", expand=True)


# =================================================================
# =================================================================
# ==================== Additional Python Script ===================


 


if  scale == sl[i] and sl[i] == sct[i]:
    sl[i].converted_scales_frame.pack(fill='y', expand=True, side='top')
    current = sl[i]
    st = scaleTemp.get()


sct[0] = [             # Celcius Conversion Table
            temp1(round(int(temp) * 1, 2)),                                    # Celcius
            temp2(round(int(temp)  + 273.15, 2)),                                  # Celcius to Kelvin
            temp3(round(int(temp)  * (9/5) + 32, 2)),                              # Celcius to Fahrenheit
            temp4(round(int(temp)  + 491.67, 2))                                   # Celcius to Rankine
        ]

sct[1][              # Kelvin Conversion Table
            temp1(round(int(temp) - 273.15, 2)),                               # Kelvin to Celcius
            temp2(round(int(temp) * 1, 2)),                                    # Kelvin       
            temp3(round(((int(temp) - 273.15) * 1.8) + 32, 2)),                # kelvin to Fahrenheit
            temp4(round((int(temp) * 1.8) + 459.67, 2))                        # Kelvin to Rankine
        ]

sct[2][            # Fahrenheit Conversion Table
            temp1(round((int(temp) - 32) * (5/9), 2)),                         # Fahrenheit to Celcius
            temp2(round(((int(temp) - 32) / 1.79999999) + 273.15, 2)),         # Fahrenheit to Kelvin
            temp3(round(int(temp) * 1, 2)),                                    # Fahrenheit       
            temp4(round(int(temp) + 459.67, 2))                                # Fahrenheit to Rankine
        ] 

sct[3][              # Rankine Conversion Table
            temp1(round((int(temp) - 491.67) / 1.79999999, 2)),                # Rankine to Celcius 
            temp2(round(((int(temp)- 491.67) / 1.79999999) + 273.15, 2)),      # Rankine to Kelvin     
            temp3(round(int(temp) - 459.67, 2)),                                # Rankine to Fahrenheit
            temp4(round(int(temp) * 1, 2)),                                    # Rankine
            
        ]

# =================================================================
# =================================================================
# ================== End Additional Python Script =================

def quit_main():
    window.quit()

window.configure(menu = menu)
# Initialize Window
window.mainloop()
