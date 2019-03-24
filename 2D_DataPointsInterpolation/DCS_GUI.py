import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import filedialog
import tkinter as tk
import numpy as np
from tkinter import ttk
from tkinter import *
from scipy.interpolate import interp2d
import math
from tkinter import messagebox


## things that can be done outside the main GUI class
dose_1, perm_1, fa_1 = np.loadtxt('dcs_plot_1.txt', skiprows = 2).transpose()
dcs_data_2 = np.loadtxt('dcs_plot_2.txt', skiprows = 1)
dose_2 = dose_1
perm_2 = perm_1
fa_2 = np.array([])
for col in range(1, dcs_data_2.shape[1])[::2]:
    fa_2 = np.concatenate((fa_2, dcs_data_2[:, col]))
# convert dose data to log 10 base
dose_1_log10 = np.log10(dose_1)
dose_2_log10 = dose_1_log10
fa_1_log10 = np.log10(fa_1)
fa_2_log10 = np.log10(fa_2)

# interpolation
f1 = interp2d(dose_1_log10, perm_1, fa_1_log10, kind = 'cubic')
f2 = interp2d(dose_2_log10, perm_2, fa_2_log10, kind = 'quintic')

N = 200
dose_new = np.linspace(1, 8, N)
perm_new = np.linspace(1, 10, N)
X, Y = np.meshgrid(dose_new, perm_new)
Z1 = np.loadtxt('interpolated_fa_1.txt')
Z2 = np.loadtxt('interpolated_fa_2.txt')

class Query_Points:

    def __init__(self, master):
        self.master = master
        self.master.title("Find fraction absorbed!")
        self.master.minsize(900, 750)
        #self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('TFrame')
        self.style.configure('TButton', font=('Helvetica', 14))

        ##define a top frame where the canvas will be placed
        self.top_frame = ttk.Frame(self.master, padding = (30, 15))
        self.top_frame.pack()

        self.fig = plt.figure(figsize=(12, 6), dpi=100) ##create a figure; modify the size here
        self.fig.add_subplot(121)
    
        plt.title("250 nm Particle Size, Log D = 3")
        plt.xlabel("Dose/Solubility Ratio, log10", labelpad = 20, fontsize = 15)
        plt.ylabel("Permeability", labelpad = 20, fontsize = 15)
        plt.pcolor(X, Y, Z1, cmap = 'seismic')
        plt.colorbar()

        self.fig.add_subplot(122)
    
        plt.title("25 um Particle Size, Log D = 3")
        plt.xlabel("Dose/Solubility Ratio, log10", labelpad = 20, fontsize = 15)
        plt.ylabel("Permeability", labelpad = 20, fontsize = 15)
        plt.pcolor(X, Y, Z2, cmap = 'seismic')
        plt.colorbar()

        self.fig.tight_layout()

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.top_frame)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.top_frame)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        ##define buttons at bottom frame

        self.bottom_frame = ttk.Frame(self.master, padding = (30, 15))
        self.bottom_frame.pack()
        self.dose = StringVar()
        self.solub = StringVar()
        self.perm = StringVar()
        
        ttk.Label(self.bottom_frame, text = "Input Dose", justify = CENTER,
                  font = ('Arial', 16, 'bold')).grid(row=0, column = 0, columnspan = 3, padx = 5, sticky = "sw")
        ttk.Entry(self.bottom_frame, width = 10, font = ('Arial', 14),
                  textvariable = self.dose).grid(row=0, column = 3, columnspan = 3, padx = 5, sticky = "sw")

        ttk.Label(self.bottom_frame, text = "Input Solubility", justify = CENTER,
                  font = ('Arial', 16, 'bold')).grid(row=0, column = 6, columnspan = 3, padx = 5, sticky = "sw")
        ttk.Entry(self.bottom_frame, width = 10,
                  font = ('Arial', 14), textvariable = self.solub).grid(row=0, column = 9, columnspan = 3, padx = 5, sticky = "sw")

        ttk.Label(self.bottom_frame, text = "Input Permeability", justify = CENTER,
                  font = ('Arial', 16, 'bold')).grid(row=0, column = 12, columnspan = 3, padx = 5, sticky = "sw")
        ttk.Entry(self.bottom_frame, width = 10,
                  font = ('Arial', 14), textvariable = self.perm).grid(row=0, column = 15, columnspan = 3, padx = 5, sticky = "sw")

        ttk.Button(self.bottom_frame, text = "Find Fraction of Absorbed",
                   command = self.find_fa, style = "TButton").grid(row=1, column = 0, columnspan = 5, padx = 5, sticky = "sw")

        ttk.Button(self.bottom_frame, text = "Clear Query Point",
                   command = self.clear_plot, style = "TButton").grid(row=2, column = 0, columnspan = 5, padx = 5, sticky = "sw")

        self.fa = ttk.Label(self.bottom_frame, text = "", justify = CENTER, font = ('Arial', 16, 'bold'))
        self.fa.grid(row=1, column = 8, columnspan = 6, padx = 5, sticky = "sw")        

    def find_fa(self):

        a = float(self.dose.get())
        b = float(self.solub.get())
        dose_solub_ratio = math.log10(a/b)
        c = float(self.perm.get())

        ## Write down some constraints
        ## (1) b cannot be zero
        ## (2) log10(dose_solub_ratio) within 1 and 8
        ## (3) Permeability within 1 and 10.
        
        if b != 0:
            pass
        else:
            messagebox.showwarning("Warning!", "Solubility value cannot be zero, not divisible...")

        if dose_solub_ratio >=1.0 and dose_solub_ratio <=8.0:
            pass
        else:
            messagebox.showwarning("Warning!", "Dose/Solubility ratio out of range, please check inputs!")

        if c>=1.0 and c<=10.0:
            pass
        else:
            messagebox.showwarning("Warning!", "Permeability out of range, please check input!")

        fa_1_pred = 10**f1(dose_solub_ratio,  c)
        fa_2_pred = 10**f2(dose_solub_ratio,  c)
        
        self.fa.configure(text = "Predicted FA are: {} and {}".format(fa_1_pred, fa_2_pred)) 
        self.fig.clf()
        self.fig.add_subplot(121)
        plt.title("250 nm Particle Size, Log D = 3")
        plt.xlabel("Dose/Solubility Ratio, log10", labelpad = 20, fontsize = 15)
        plt.ylabel("Permeability", labelpad = 20, fontsize = 15)
        plt.plot([dose_solub_ratio], [c], marker = 'x', markersize = 8, color = 'y')
        plt.pcolor(X, Y, Z1, cmap = 'seismic')
        plt.colorbar()
        
        self.fig.add_subplot(122)
        plt.title("25 um Particle Size, Log D = 3")
        plt.xlabel("Dose/Solubility Ratio, log10", labelpad = 20, fontsize = 15)
        plt.ylabel("Permeability", labelpad = 20, fontsize = 15)
        plt.plot([dose_solub_ratio], [c], marker = 'x', markersize = 8, color = 'y')
        plt.pcolor(X, Y, Z2, cmap = 'seismic')
        plt.colorbar()
        self.fig.tight_layout()
        self.canvas.draw()

    def clear_plot(self):
        self.fig.clf()
        self.fa.configure(text = "")
        self.dose.set("")
        self.solub.set("")
        self.perm.set("")

        self.fig.add_subplot(121)
        plt.title("250 nm Particle Size, Log D = 3")
        plt.xlabel("Dose/Solubility Ratio, log10", labelpad = 20, fontsize = 15)
        plt.ylabel("Permeability", labelpad = 20, fontsize = 15)
        plt.pcolor(X, Y, Z1, cmap = 'seismic')
        plt.colorbar()

        self.fig.add_subplot(122)
        plt.title("25 um Particle Size, Log D = 3")
        plt.xlabel("Dose/Solubility Ratio, log10", labelpad = 20, fontsize = 15)
        plt.ylabel("Permeability", labelpad = 20, fontsize = 15)
        plt.pcolor(X, Y, Z2, cmap = 'seismic')
        plt.colorbar()
        self.fig.tight_layout()
        self.canvas.draw()

def main():        
    root = Tk()
    GUI = Query_Points(root)
    root.mainloop()
    
if __name__ == "__main__": main()          
