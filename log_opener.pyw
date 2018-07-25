try:
	file = open("log.txt","r")
	__doc__ = file.read()
	file.close()
except:
	__doc__ = """(log.txt don't exists)"""

	

__all__ = ['ScrolledText']

from tkinter import Frame, Text, Scrollbar, Pack, Grid, Place
from tkinter import *
from tkinter.constants import RIGHT, LEFT, Y, BOTH

master = Tk()
master.title('Log')
master.iconbitmap("data/Icon.ico")
class ScrolledText(Text):
    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame,height=20,width=150,fg = "white")
        self.config({'yscrollcommand':self.vbar.set})
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)



from tkinter.constants import END
stext = ScrolledText()
stext['bg'] = "black"
stext.insert(END, __doc__)
stext.pack(fill=BOTH, side=LEFT, expand=True)

stext.focus_set()
stext.mainloop()

