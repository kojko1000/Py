import tkinter
import numpy
from datetime import datetime

print(datetime.now().second+datetime.now().minute+datetime.now().hour)
window = tkinter.Tk()
window.geometry("300x250")
now=datetime.now()
cols , rows = 3,3


bombs = []
for r in range(rows-1):
    bombs.append([0]*cols)

for r in range(rows-1):
    for c in range(cols-1):
   
        bombs[r][c] = 1
        #if((bombs[r][c]%2) == 1):
        #    bombs[r][c] = 1
        #else:
        #    bombs[r][c] = 0
        print(bombs[r],[c])
    print('\n')

def click(r,c,btn):
    print(f"{r} {c}")
     
    pass

for r in range(rows):
    for c in range(cols):
        btn = tkinter.Button(text=f"{r},{c}")
        btn.grid(row=r,column=c)
        btn.config(command=lambda rr=r, cc=c, b=btn:click(rr,cc,b))

window.geometry("300x300")
window.mainloop()

