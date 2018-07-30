print("Please Wait!")
from tkinter import *
import tkinter.font,os,time,shutil,subprocess
from tkinter.filedialog import askopenfilename as aof
import tkinter.messagebox as tmb
import tkinter.ttk as ttk
import os,sys,importlib
from importlib import util
if os.path.exists("data") == False:
    shutil.unpack_archive("data.zip","data")
os.system("requirement.bat")
try:
    import cx_Freeze
    impoerror=False
except:
    impoerror = True
    print("Module 'cx_Freeze' not found.....")
#starting
def mainhelp():
    tmb.showinfo("Help","Including files:\n  |  Paste the files in the output (build) folder ( or zip )...\nIcon not showing?\n  |  Make sure that your .ico file is correct...\nCaution:\n  |  Don't delete or rename files else it may not work...\n"+"_"*61+"\nYou can get help about fields by clicking the help icons on the right side")
def delefiles():
    try:shutil.rmtree("build",True)
    except:pass
    try:os.remove("build.zip")
    except:pass
def mreset():
    global colo
    colo = "light blue"
    loadst.configure("red.Horizontal.TProgressbar", foreground=colo, background=colo)
    logp("",load=0)
    scrent.delete(0,"end")
    nament.delete(0,"end")
    verent.delete(0,"end")
    desent.delete(0,"end")
    basevar.set("Console")
    icovar.set(0);icoopen()
    incvar.set(0);incenen()
    excvar.set(0);excenen()
    pacvar.set(0);pacenen()
    comvar.set(0)
    while True:
        if probar["value"] == 1 or probar["value"] == 0:break
        probar["value"] = int(probar["value"]) - 2
        root.update()
        time.sleep(0.0000000000000001)
    probar["value"] = 0
    delefiles()
    root.update()
def exiit():
    root.destroy()
    mtkroot.destroy()
    sys.exit()
mtkroot = Tk()
mtkroot.iconbitmap("data/Icon.ico")
mtkroot.withdraw()
menubar = Menu(mtkroot)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Reset',command=mreset,underline=0)
filemenu.add_separator()
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help',command=mainhelp,underline=0)
menubar.add_cascade(label='File',menu=filemenu,underline=0)
menubar.add_cascade(label='Help',menu=helpmenu,underline=0)
root = Toplevel(mtkroot, menu=menubar)
filemenu.add_command(label='Exit',command=exiit,underline=0)
root.protocol('WM_DELETE_WINDOW')
root.geometry("550x650")
root.title("Executable File Maker")
root.resizable(False,False)
root.iconbitmap("data/Icon.ico")
global colo
global pname,pvers,pdesc,picon,pinit,pbase,pinc,pexc,ppac,file,zipped
zipped = False
colo = "light blue"
#useful functions
def tkbg(widget=None,color='light grey'):
    widget['bg'] = color
def butscr():
    file = aof(title="Select Script file",filetypes=[("Python file","*.py")])
    scrent.delete(0,"end")
    scrent.insert(0,file)
def butico():
    file = aof(title="Select Icon file",filetypes=[("Icon file","*.ico")])
    icoent.delete(0,"end")
    icoent.insert(0,file)
def butisc():
    file = aof(title="Select InitScript file",filetypes=[("Python file","*.py")])
    iscent.delete(0,"end")
    iscent.insert(0,file)
def incenen():
    incx = int(incvar.get())
    if incx == 0:incent.delete(0,'end');incent['state']='disabled'
    else:incent['state']='normal'
def excenen():
    excx = int(excvar.get())
    if excx == 0:excent.delete(0,'end');excent['state']='disabled'
    else:excent['state']='normal'
def pacenen():
    pacx = int(pacvar.get())
    if pacx == 0:pacent.delete(0,'end');pacent['state']='disabled'
    else:pacent['state']='normal'
def icoopen():
    icov = int(icovar.get())
    if icov == 0:
        icoent.delete(0,'end');
        icoent['state']='disabled'
        icobut['state']='disabled'
    else:
        icoent['state']='normal'
        icobut['state']='normal'
def load(value):
    probar["value"] = int(value)
    root.update()
def help1c():
    tmb.showinfo("*Script","Write the path to your main python file which you want to be compiled....")
def help2c():
    tmb.showinfo("*Name","Write the name of the application....")
def help3c():
    tmb.showinfo("*Version","Write the version of the application....")
def help4c():
    tmb.showinfo("*Description","Write the description of the application....")
def help5c():
    tmb.showinfo("Icon","Write the path to icon for your application....")
def help7c():
    tmb.showinfo("Base","Select the base or leave it as it is....")
def help8c():
    tmb.showinfo("Include","Write the names of modules to be included seperated by comma without any space....")
def help9c():
    tmb.showinfo("Exclude","Write the names of modules to be excluded seperated by comma without any space....")
def help11c():
    tmb.showinfo("Packages","Write the names of packages to be included seperated by comma without any space....")
def help22c():
    tmb.showinfo("Compress","Compress the output result to a zip file....")
def logp(text,color='#2484a3',wait=0.5,load=1,cl=False):
    if color == "red":color = "#a81151"
    global colo
    colo = "light blue"
    loadst.configure("red.Horizontal.TProgressbar", foreground=colo, background=colo)
    root.update()
    if load == 1:
        for i in range(0,4):
            probar.step(1)
            root.update()
            time.sleep(0.0000000000000001)
    loadst.configure("red.Horizontal.TProgressbar", foreground=colo, background=colo)
    clearn = Label(root,text = ('  '*100)+("\n"+" "*100),font=low)
    tkbg(clearn)
    clearn.place(relx = 0.5,rely=0.8,anchor=CENTER)
    logt = Label(root,text = text,font=low)
    logt['fg']=color;tkbg(logt)
    logt.place(relx = 0.5,rely=0.8,anchor=CENTER)
    root.update()
    if color != "#a81151":time.sleep(wait)
    else:
        colo = "#a81151"
        loadst.configure("red.Horizontal.TProgressbar", foreground=colo, background=colo)
        while not probar['value'] == 99:
            if probar["value"] == 98:probar["value"] = 97
            probar.step(2)
            root.update()
            time.sleep(0.00000000000000000001)
        buildb["state"] = "normal"
        root.update()
def break_l(listt):
    output = str(listt)
    output = output.replace("[",'')
    output = output.replace("]",'')
    return output
def open_log():
    subprocess.Popen('log_opener.pyw', shell=True)
def open_fold():
    global zipped
    if os.path.exists("build") == True or os.path.exists("build.zip") == True:
        if not zipped:os.system("start build")
        else:os.system("start build.zip")
    else:
        tmb.showerror("Folder not found","Oops! folder 'build' do not exists")
def write_setup():
    spy = open("setup.py","w")
    def nl(n=1):
        spy.write('\n'*n)
    spy.write("import sys,os\nfrom cx_Freeze import setup,Executable\n\n")
    spy.write(r"os.environ['TCL_LIBRARY'] = 'data/tcl8.6'");nl()
    spy.write(r"os.environ['TK_LIBRARY'] = 'data/tk8.6'");nl(2)
    spy.write(r"option = {'packages':["+ppac+"],'includes':["+pinc+"],'excludes':["+pexc+"],'include_files':['data/tcl86t.dll','data/tk86t.dll']}");nl(2)
    spy.write(r'name = "'+pname+'"');nl()
    spy.write(r'file = "'+file+'"');nl()
    spy.write(r'vers = "'+pvers+'"');nl()
    spy.write(r'descr = "'+pdesc+'"');nl()
    if len(picon) != 0:spy.write(r'icon = "'+picon+'"');nl()
    spy.write(r'base = "'+pbase+'"');nl()
    spy.write('setup(\n    ')
    spy.write('name = name,\n    version = vers,\n    description=descr,\n    options = {"build_exe":option},\n    ')
    spy.write('executables=[Executable(file,base=base')
    if len(picon) != 0:spy.write(',icon=icon')
    spy.write(')]\n)')
    spy.close()
def build():
    delefiles()
    global colo
    colo = "light blue"
    root.focus()
    buildb['state'] = "disabled"
    if probar["value"] == 99:
        barx = 100
        for i in range(0,100):
            if probar["value"] == 98:probar["value"] = 97
            probar["value"] = barx
            barx -= 2
            root.update()
            time.sleep(0.0000000000000001)
            
    load(3)
    global pname,pvers,pdesc,picon,pbase,pinc,pexc,ppac,file,zipped
    file = str(scrent.get())
    pname = nament.get()
    pvers = verent.get()
    pdesc = desent.get()
    picon = icoent.get()
    pbase = basevar.get()
    pinc = incent.get()
    pexc = excent.get()
    ppac = pacent.get()
    pcom = comvar.get()
    logp("Scraping data")
    #verifying
    logp("Verifying Script path")
    if os.path.exists(str(file)):
        if file.lower().endswith((".py",".pyw")) == True:pass
        else:logp("Invalid Script file","red");return 0
    else:
        if len(file) == 0:logp("Script File path is required","red")
        else:logp("FileNotFoundError: Script path not found","red")
        return 0
    logp("Verifying Name")
    if len(pname) == 0:logp("Name is required","red");return 0
    logp("Verifying Version")
    if len(pvers) == 0:logp("Version is required","red");return 0
    elif pvers.isdigit() == False:
        try:
            was = float(pvers)
        except:
            logp("Invalid Version","red")
            return 0
    logp("Verifying Description")
    if len(pdesc) == 0:logp("Description is required","red");return 0
    if len(picon) != 0:
        logp("Verifying Icon path")
        if os.path.exists(picon) == False:logp("FileNotFoundError: Icon path not found","red");return 0
        else:
            if picon.lower().endswith(".ico") == True:pass
            else:logp("Invalid Icon file","red");return 0
    if incvar.get() != 0 and int(len(pinc)) != 0:
        logp("Searching for required modules")
        was = pinc.split(",")
        pinc = []
        for modu in was:
            try:
                logp("Searching for module '"+modu+"'",wait=0.2,load=2)
                resul = util.find_spec(modu)
                if resul == None:raise ImportError
                pinc.insert(0,str(modu))
            except:
                logp("ModuleNotFoundError: no module named '"+modu+"'","red")
                return 0
        pinc = break_l(pinc)
    if excvar.get() != 0 and int(len(pexc)) != 0:
        logp("Searching for required modules")
        was = pexc.split(",")
        pexc = []
        for modu in was:
            try:
                logp("Searching for module '"+modu+"'",wait=0.2,load=2)
                iresul = util.find_spec(modu)
                if resul == None:raise ImportError
                pexc.insert(0,str(modu))
            except:
                logp("ModuleNotFoundError: no module named '"+modu+"'","red")
                return 0
        pexc = break_l(pexc)
    if pacvar.get() != 0 and int(len(ppac)) != 0:
        logp("Searching for required modules")
        was = ppac.split(",")
        ppac = []
        for modu in was:
            try:
                logp("Searching for module '"+modu+"'",wait=0.2,load=2)
                resul = util.find_spec(modu)
                if resul == None:raise ImportError
                ppac.insert(0,str(modu))
            except:
                logp("ModuleNotFoundError: no module named '"+modu+"'","red")
                return 0
        ppac = break_l(ppac)
    logp("Making file 'setup.py'")
    os.system("echo > setup.py")
    logp("Cleaning file 'setup.py'")
    was = open("setup.py","w")
    was.write('')
    was.close()
    logp("Writing setup.py",wait=1)
    write_setup()
    logp("Success",wait = 0.4)
    root.focus()
    logp("Building setup.py\nPlease Wait!")
    def builddd():
        subprocess.call("execute.bat", shell=True)
    root.after(0,builddd())
    logp("Command executed Successfully")
    logp("Looking for output folder",wait=0.4)
    if os.path.exists("build"):
        logp("Ouput folder found")
    else:
        logp("Output folder not found","red")
        tmb.showerror("Output folder not found","Output folder not found, Please look inside the script directory manually, read log.txt file and check if your data is incorrect.")
        return 0
    if int(pcom) == 1:
        logp("Compressing Output")
        try:os.remove("build.zip")
        except:pass
        shutil.make_archive("build",'zip',"build")
        logp("Compressed Successfully")
        logp("Deleting build folder")
        shutil.rmtree("build",True)
        logp("Deleted Successfully")
        zipped = True
    else:zipped = False
    logp("Done")
    load(100)
    ologs = Button(root,text="Open log file",font=sign,command=open_log)
    ologs.place(x=100,y=600)
    oout = Button(root,text="Open Output folder",font=sign,command=open_fold)
    oout.place(x=350,y=600)
    buildb["state"] = "normal"
    root.update()

#initializing
tkbg(root)
#fonts
high = tkinter.font.Font(root,family="Courier New",size=20,weight="bold")
high1 = tkinter.font.Font(root,family="Courier New",size=15,weight="bold")
low = tkinter.font.Font(root,family="Courier New",size=13)
low1 = tkinter.font.Font(root,family="Courier New",size=11)
sign = tkinter.font.Font(root,family="Courier New",size=8)

#heading

titlimg = PhotoImage(file="data/title.png")
titll = Label(root,image=titlimg)
titll["bg"] = "light grey"
titll.place(x=97,y=10)
#script
script = Label(root,text="Script File:",font=low)
script.place(x=12,y=60)
tkbg(script)
scrent = Entry(root,width = 31,font=low1,bd=2)
scrent.place(x=150,y=64)
scrbut = Button(root,text="Select",font=low1,command=butscr)
scrbut.place(x=440,y=60)
#name
name = Label(root,text="Name:",font=low)
name.place(x=12,y=100)
tkbg(name)
nament = Entry(root,width = 39,font=low1,bd=2)
nament.place(x=150,y=104)
#version
version = Label(root,text="Version:",font=low)
version.place(x=12,y=140)
tkbg(version)
verent = Entry(root,width = 39,font=low1,bd=2)
verent.place(x=150,y=144)
#description
descript = Label(root,text="Description:",font=low)
descript.place(x=12,y=180)
tkbg(descript)
desent = Entry(root,width = 39,font=low1,bd=2)
desent.place(x=150,y=184)
#base
basescr = Label(root,text="Base:",font=low)
basescr.place(x=12,y=220)
tkbg(basescr)
basevar = StringVar(root)
basevar.set("Console")
baselist = OptionMenu(root, basevar, "Console", "Win32GUI")
baselist['width'] = '31'
baselist['font'] = low
baselist['bg'] = "white"
baselist.place(x=150,y=220)
#icon
icovar = StringVar(root)
icovar.set(0)
icoop = Checkbutton(root,variable=icovar,text="Icon:",font=low,command=icoopen)
icoop.place(x=12,y=260)
tkbg(icoop)
icoop["activebackground"] = "light grey"
icoent = Entry(root,width = 31,font=low1,bd=2)
icoent.place(x=150,y=264)
icobut = Button(root,text="Select",font=low1,command=butico)
icobut.place(x=440,y=260)
if int(icovar.get()) == 0:icoent['state']='disabled';icobut["state"] = "disabled"
#include
incvar = StringVar(root)
incvar.set(0)
inclu = Checkbutton(root,variable=incvar,text="Include:",font=low,command=incenen)
inclu.place(x=12,y=300)
tkbg(inclu);inclu['activebackground']='light grey'
incent = Entry(root,width = 39,font=low1,bd=2)
incent.place(x=150,y=304)
if int(incvar.get()) == 0:incent['state']='disabled'
#exclude
excvar = StringVar(root)
excvar.set(0)
exclu = Checkbutton(root,variable=excvar,text="Exclude:",font=low,command=excenen)
exclu.place(x=12,y=340)
tkbg(exclu);exclu['activebackground']='light grey'
excent = Entry(root,width = 39,font=low1,bd=2)
excent.place(x=150,y=344)
if int(excvar.get()) == 0:excent['state']='disabled'
#packages
pacvar = StringVar(root)
pacvar.set(0)
paclu = Checkbutton(root,variable=pacvar,text="Packages:",font=low,command=pacenen)
paclu.place(x=12,y=380)
tkbg(paclu);paclu['activebackground']='light grey'
pacent = Entry(root,width = 39,font=low1,bd=2)
pacent.place(x=150,y=384)
if int(pacvar.get()) == 0:pacent['state']='disabled'
#compress
comvar = StringVar(root)
comvar.set(0)
comlu = Checkbutton(root,variable=comvar,text="Compress Output",font=low)
tkbg(comlu);comlu['activebackground']='light grey'
comlu.place(x=12,y=420)
#Build Button
buildb = Button(root,text="Build",font=high1,command=build,bg="light blue",activebackground="skyblue")
buildb.place(x=238,y=600)
#progress bar
loadframe = Frame(root)
loadframe.grid()
loadst = ttk.Style()
loadst.theme_use('clam')
loadst.configure("red.Horizontal.TProgressbar", foreground=colo, background=colo)
probar = ttk.Progressbar(loadframe, style="red.Horizontal.TProgressbar", orient="horizontal", length=400, mode="determinate", maximum=100, value=0)
probar.grid(row=1, column=1)
loadframe.place(x=75,y=560)
#help1
helpim = PhotoImage(file="data/help.gif")
help1 = Button(root, text="Help",bd=0,bg="light grey",command=help1c)
help1["activebackground"] = "light grey"
help1.config(image=helpim)
help1.place(x=512,y=65)
#help2
help2 = Button(root, text="Help",bd=0,bg="light grey",command=help2c)
help2["activebackground"] = "light grey"
help2.config(image=helpim)
help2.place(x=512,y=105)
#help3
help3 = Button(root, text="Help",bd=0,bg="light grey",command=help3c)
help3["activebackground"] = "light grey"
help3.config(image=helpim)
help3.place(x=512,y=145)

#help4
help4 = Button(root, text="Help",bd=0,bg="light grey",command=help4c)
help4["activebackground"] = "light grey"
help4.config(image=helpim)
help4.place(x=512,y=185)
#help7
help7 = Button(root, text="Help",bd=0,bg="light grey",command=help7c)
help7["activebackground"] = "light grey"
help7.config(image=helpim)
help7.place(x=512,y=225)

#help5
help5 = Button(root, text="Help",bd=0,bg="light grey",command=help5c)
help5["activebackground"] = "light grey"
help5.config(image=helpim)
help5.place(x=512,y=265)
#help8
help8 = Button(root, text="Help",bd=0,bg="light grey",command=help8c)
help8["activebackground"] = "light grey"
help8.config(image=helpim)
help8.place(x=512,y=305)

#help9
help9 = Button(root, text="Help",bd=0,bg="light grey",command=help9c)
help9["activebackground"] = "light grey"
help9.config(image=helpim)
help9.place(x=512,y=345)

#help11
help11 = Button(root, text="Help",bd=0,bg="light grey",command=help11c)
help11["activebackground"] = "light grey"
help11.config(image=helpim)
help11.place(x=512,y=385)

#help22
help22 = Button(root, text="Help",bd=0,bg="light grey",command=help22c)
help22["activebackground"] = "light grey"
help22.config(image=helpim)
help22.place(x=512,y=425)

#signature
signa = Label(root,text="Made by M.Nouman")
signa['bg'] = "light grey"
signa['fg'] = "#888888"
signa.place(x = 434, y = 630)


if impoerror == True:
    logp("ModuleNotFoundError: No module named 'cx_Freeze'","red")
mainloop()
