import tkinter
import numpy
import screeninfo
import time
import threading
from datetime import datetime
now=datetime.now()


print(f"{screeninfo.get_monitors()[0].width} + {screeninfo.get_monitors()[0].height}")
cols,rows = 15,15
maxX,maxY = 35,70
plateSize = 24
isDarkMode = True

#root = tkinter.Tk()
#icon = tkinter.PhotoImage(file="./Sapper2.2/images/Icon.png")
#root.iconphoto(True,icon)


#1 мб было бы прикольно сделать типо бонусов на пустых клетках. типо сканера или чего то подобного (типо вокруг себя радиусом в 3 позиции показывает что там... бомба или нет)
#2 стоило бы сделать проверочки на некоректные данные в поля ввода. Ото кто знает этих пользователей 
#3 визуально прогресс бар над игровым поллем или в отдельном окне рядышком. Вывести статку время, колличество кликов, колличетсво открытых клеток и бомб. Можно добавить рйтинг
#4 название и иконка, ну тут и так понятно
#5 ну и визуализировать проигрыш и победу (проигрыш-временные спам окна с "бам","бом","бум" и в меню. Победа - картинка с возможностью "повторить", "меню", а ну и статистика)
#6 статистика забегов в json какой нить.
'''
def button_entered(event):
    btn = event.widget
    tkinter.Button(btn).place(1,1)
'''

def on_escape(event): #Выход в меня из игрового окна. Функция для ивента крч.
    win = event.widget.winfo_toplevel()
    win.destroy()
    meny()

def kastylniyInverse(btn = None): #Костыль, но работает. Я не представляю почему оно инверсируеться, но как есть. Я так сделал... и оно работает.
    global isDarkMode
    if(isDarkMode==False):
        isDarkMode=True
    else:
        isDarkMode=False

def darkmode(components,window,btn=None):
        global isDarkMode
        if(isDarkMode==False):
            for component in components:
                component.config(fg="white",bg="#363438") 
            window.config(bg="#252426")
            isDarkMode=True
        else:
            for component in components:
                component.config(fg="black",bg="white")
            window.config(bg="white")
            isDarkMode=False
        if (not btn is None):
            if(isDarkMode==False):
                btn.config(text="○")
            else:
                btn.config(text="☼")
        print(isDarkMode)

def win(window): #ПОБЕДА, нужно окно или что то такое для возврата в меню
        window.destroy()

        def goMeny():
            winWindow.destroy()
            meny()
        menyComponents = []

        winWindow = tkinter.Tk()
        winWindow.title("Win")
        winWindow.geometry(f"200x100+{int((screeninfo.get_monitors()[0].width)/2-(500/2))}+{int((screeninfo.get_monitors()[0].height)/2-(200/2))}")
        winWindow.resizable(False,False)

        #bgImage=tkinter.PhotoImage(file="./images/WinBG.png")
        #bg = tkinter.Label(text="adadad", image=bgImage)
        #bg.place(x=0,y=0,relheight=1,relwidth=1)

        sizeInfoLable = tkinter.Label(text=f"░░░▒▓Win▓▒░░░",background="#b9a1c9", font=("Arial",25))
        sizeInfoLable.pack(expand=True,anchor="s",fill="x")

        saveBtn = tkinter.Button(text="meny",height=2)
        saveBtn.pack(expand=True,anchor="center")
        saveBtn.config(command=goMeny)
        menyComponents.append(saveBtn)
        kastylniyInverse()
        darkmode(menyComponents,winWindow)
        winWindow.mainloop()

        
        
        
        #window.after(3000,window.destroy())
def lose(window): #ПОРАЖЕНИЕ (Наверняка это можно сделать более элегантно, но мне лень)
    def makeTimeWindow():
        '''
        boomWindow = tkinter.Tk()
        boomWindow.title("BOOM")
        boomWindow.geometry(f"300x200+{int((screeninfo.get_monitors()[0].width)/2-(300/2))}+{int((screeninfo.get_monitors()[0].height)/2-(200/2))}")
        boomWindow.config(bg="red")
        boomWindow.resizable(False,False)
        boomWindow.after(250,boomWindow.destroy)
        bgImage=tkinter.PhotoImage(file="./images/LoseBG.png")
        bg = tkinter.Label(boomWindow,text="adadad", image=bgImage)
        bg.place(x=0,y=0,relheight=1,relwidth=1)
        boomWindow.mainloop()
        
    window.destroy()
    makeTimeWindow()
    makeTimeWindow()
    makeTimeWindow()
    meny()
    '''
    window.destroy()

    def goMeny():
        winWindow.destroy()
        meny()
    menyComponents = []

    winWindow = tkinter.Tk()
    winWindow.title("Win")
    winWindow.geometry(f"200x100+{int((screeninfo.get_monitors()[0].width)/2-(500/2))}+{int((screeninfo.get_monitors()[0].height)/2-(200/2))}")
    winWindow.resizable(False,False)

    sizeInfoLable = tkinter.Label(text=f"░░░▒▓Lose▓▒░░░",background="#b9a1c9", font=("Arial",25))
    sizeInfoLable.pack(expand=True,anchor="s",fill="x")

    saveBtn = tkinter.Button(text="meny",height=2)
    saveBtn.pack(expand=True,anchor="center")
    saveBtn.config(command=goMeny)
    menyComponents.append(saveBtn)
    kastylniyInverse()
    darkmode(menyComponents,winWindow)
    winWindow.mainloop()
    pass

def meny():
    def save_size():
        global cols,rows
        if(int(xInput.get())>maxX):
            rows = maxX
        else:
            rows = int(xInput.get())
        if(int(yInput.get())>maxY):
            cols = maxY
        else:
            cols = int(yInput.get())
        
        sizeInfoLable["text"] = f"░░░▒▓{cols} X {rows}▓▒░░░"
        print(f"{xInput.get()} {yInput.get()}    {cols} {rows}")
    def initStart():
        menyWindow.destroy()
        start_game()
        
    menyWindow = tkinter.Tk()
    menyWindow.title("meny")
    winSize = 300 
    menyWindow.geometry(f"{winSize}x{winSize}+{int((screeninfo.get_monitors()[0].width)/2-(winSize/2))}+{int((screeninfo.get_monitors()[0].height)/2-(winSize/2))}") #print(f"{screeninfo.get_monitors()[0].width} + {screeninfo.get_monitors()[0].height}")
    menyWindow.resizable(False,False)
    
    #icon = tkinter.PhotoImage(file="./images/Icon.png")
    #menyWindow.iconphoto(True,icon)
    menyComponents = []

    
    xInput = tkinter.Spinbox(font=("Arial",20),width=3,from_=1, to=maxX,command=save_size , textvariable=tkinter.StringVar(value=rows))
    xInput.place(x=10,y=10)
    #menyComponents.append(yInput)

    yInput = tkinter.Spinbox(font=("Arial",20),width=3, from_=1, to=maxY, command=save_size, textvariable=tkinter.StringVar(value=cols)) #state="readonly"
    yInput.place(x=10,y=50)
    #menyComponents.append(xInput)
    
    saveBtn = tkinter.Button(text="save size",height=2)
    saveBtn.place(x=80,y=10)
    saveBtn.config(command=save_size)
    menyComponents.append(saveBtn)
    
    darkModeBtn = tkinter.Button(text="○",height=1)
    darkModeBtn.place(x=275,y=10)
    darkModeBtn.config(command=lambda cmps=menyComponents, wnd=menyWindow, btn=darkModeBtn :darkmode(cmps,wnd,btn)) #command=lambda rr=r, cc=c, b=btn:click(rr,cc,b)
    menyComponents.append(darkModeBtn)
    
    sizeInfoLable = tkinter.Label(text=f"░░░▒▓{cols} X {rows}▓▒░░░",background="#b9a1c9", font=("Arial",25))
    sizeInfoLable.pack(expand=True,anchor="s",fill="x")

    print({menyWindow.winfo_height()})
    startBtn = tkinter.Button(text="Start",height=2)
    startBtn.pack(expand=True,anchor="s")
    startBtn.config(command=initStart)
    #startBtn.bind("<Enter>",button_entered)
    menyComponents.append(startBtn)

    kastylniyInverse()
    darkmode(menyComponents,menyWindow,darkModeBtn)
    menyWindow.mainloop()


def start_game():
    
   

    window = tkinter.Tk()
    window.title("Sapper")
    window.geometry(f"{plateSize*cols}x{(plateSize+2)*rows}+{int((screeninfo.get_monitors()[0].width)/2-((plateSize*cols)/2))}+{int((screeninfo.get_monitors()[0].height)/2-(((plateSize+2)*rows)/2))}") #{plateSize*cols}x{plateSize*rows}
    window.bind("<Escape>",on_escape)
    window.resizable(False,False)
    gameComponents = []
    bombs = [[0 for _ in range(cols)] for _ in range(rows)]
    playerMarks = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
      for c in range(cols):
        playerMarks[r][c] = -1
        bombs[r][c] = numpy.random.randint(0,100)
        if((bombs[r][c]%2 and bombs[r][c]>70) == 1):
            bombs[r][c] = 1
        else:
            bombs[r][c] = 0
      
      
    for row in bombs:
        print(row)
    

    def isWin():
        no = 0
        for r in range(rows):
            for c in range(cols):
                if not (playerMarks[r][c]==bombs[r][c]):
                    return 
        #да, это победа \/

        win(window)

    def flag(event):
        btn = event.widget
        btn.config(text="▼",fg="red",bg="#873200")
        info = btn.grid_info()
        print(f"{info["row"]} {info["column"]}")
        playerMarks[info["row"]][info["column"]] = 1
        isWin()

    def click(r,c,btn):
        print(f"{r} {c} = {bombs[r][c]}")
        bCounter=0
        if (isDarkMode==True):
            btn.config(fg="white",bg="#15111c")
        else:
            btn.config(fg="black",bg="white")
        if(bombs[r][c]==1):
            btn.config(state = "disabled")
            btn["text"] = "Ø"
            lose(window)
            #ПРОИГРЫШ!!!! нужна анимация из появляющихся окн или чего то подобного
        else:
            playerMarks[r][c] = 0
            isWin()
            for i in range(-1,2):
                for j in range(-1,2):
                    if((r+i<rows and c+j<cols) and (r+i>=0 and c+j>=0)):
                        if(bombs[r+i][c+j]==1):
                          bCounter+=1
        btn["text"] = bCounter
     

    for r in range(rows):
        for c in range(cols):
            btn = tkinter.Button(text=f"∙",height=1,width=2)
            btn.grid(row=r,column=c)
            btn.config(command=lambda rr=r, cc=c, b=btn:click(rr,cc,b))
            btn.bind("<Button-3>",flag)
            gameComponents.append(btn)

    kastylniyInverse()
    darkmode(gameComponents,window)
    #-------------------ОСНОВНОЕ-ОКНО------------------
    
    window.mainloop()

#---------------------/\-Функции-/\----------------------------#

meny()