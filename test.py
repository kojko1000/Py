import tkinter
import numpy
import screeninfo
from datetime import datetime
now=datetime.now()

cols,rows = 8,8

def meny():
    
    def save_size():
        global cols,rows
        rows = int(xInput.get())
        cols = int(yInput.get())
        
        sizeInfoLable["text"] = f"░░░▒▓{cols} X {rows}▓▒░░░"
        print(f"{xInput.get()} {yInput.get()}    {cols} {rows}")
    def initStart():
        menyWindow.destroy()
        start_game()
        
    menyWindow = tkinter.Tk()
    menyWindow.geometry(f"300x300")
    menyWindow.resizable(False,False)

    xInput = tkinter.Entry(font=("Arial",20),width=3)
    xInput.insert(0,f"{cols}")
    xInput.place(x=10,y=10)

    yInput = tkinter.Entry(font=("Arial",20),width=3)
    yInput.insert(0,f"{rows}")
    yInput.place(x=10,y=50)

    saveBtn = tkinter.Button(text="save size",height=2)
    saveBtn.place(x=70,y=10)
    saveBtn.config(command=save_size)
    
    sizeInfoLable = tkinter.Label(text=f"░░░▒▓{cols} X {rows}▓▒░░░",background="#b9a1c9", font=("Arial",25))
    sizeInfoLable.pack(expand=True,anchor="s",fill="x")

    print({menyWindow.winfo_height()})
    startBtn = tkinter.Button(text="111111",height=2)
    startBtn.pack(expand=True,anchor="s")


    startBtn.config(command=initStart)
    menyWindow.mainloop()


def start_game():
    window = tkinter.Tk()
    window.geometry("300x250")

    print(f"_{cols} {rows}_")

    bombs = [[0 for _ in range(cols)] for _ in range(rows)]


    for r in range(rows):
      for c in range(cols):
        bombs[r][c] = numpy.random.randint(0,100)
        if((bombs[r][c]%2 and bombs[r][c]>60) == 1):
            bombs[r][c] = 1
        else:
            bombs[r][c] = 0
      
      
    for row in bombs:
        print(row)

    def flag(event):
        btn = event.widget
        btn.config(text="╕",fg="red",bg="gray")
        info = btn.grid_info()
        print(f"{info["row"]} {info["column"]}")

    def click(r,c,btn):
        print(f"{r} {c} = {bombs[r][c]}")
        bCounter=0
        if(bombs[r][c]==1):
            btn.config(state = "disabled")
            btn["text"] = "Ø"
            window.destroy()
            #проигрыш
        else:
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

    window.geometry("300x300")
    window.mainloop()

#---------------------/\-Функции-/\----------------------------#

meny()
#start_game()

