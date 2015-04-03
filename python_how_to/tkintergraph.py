import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Tkinter import *
class TkinterGraph(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.figure = Figure(figsize=(10,10), dpi=50)
        self.graph_a = self.figure.add_subplot(111)
        self.graph_a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])



        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.show()
        self.lbl = Label(text="Graph 1")
        self.lbl.pack(side=TOP,expand = True)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    def change_data(self):
        self.lbl.configure(text = "Graph 2")
        self.graph_a.clear()
        self.graph_a.plot([1,2,3,4,5,6,7,8],[15,26,51,32,8,49,73,75])
        self.canvas.draw()
        


def main():
    window = Tk()
    f1 = TkinterGraph(window)
    f1.pack(side = TOP, padx =20, pady =20)
    btn = Button( window , text = 'Change', command = f1.change_data)
    btn.pack(side = TOP, padx =20, pady =20)
    window.mainloop()

if __name__ == '__main__':
    main()
