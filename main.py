#Tenisce Richelieu

#Your algorithm should go here OR you should use comments throughout

#Your code goes here
 #Tenisce Richelieu
import tkinter
import tkinter.messagebox
#as box

class FahrenConverterGUI:
    def __init__(self):
        #Create the main window
        self.main_window = tkinter.Tk()

        #Create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create widgets for the top frame we need a prompt label and an entry box
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter a Fahrenheit temp: ")
        self.f_entry = tkinter.Entry(self.top_frame, width = 10)

        #Pack the top frame's widgets TOP FRAME, pack both widgets in the frame, create widgets for the bottom frame
        self.prompt_label.pack(side = 'left')
        self.f_entry.pack(side = 'left')
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Calculate", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        #Pack the button frame's widgets
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
    def convert(self):
        #Get the value entered by the user into the f widget
        f = float(self.f_entry.get())

        #Convert fahrenheit to celcius
        c = (f - 32) * 5/9

        #Display the results in an info dialog box
        tkinter.messagebox.showinfo('Results', str(f) + ' Fahrenheit is equal to ' + str(c) + ' Celcius.')
        
temp_converter = FahrenConverterGUI()
