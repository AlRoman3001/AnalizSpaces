from tkinter import *
from tkinter import scrolledtext
import os, time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def lookmf(d, dn):

    txt.delete(1.0, END)



    for root, dirs, files in os.walk(''+str(d)+':'):

        for f in files:
            # print('hello')
            ph = os.path.join(root, f)
            t_m = os.path.getmtime(ph)
            t_sys = time.time()
            t_f = (t_sys - t_m) / (60 * 60 * 24)
            # print(t_f)
            if t_f < int(dn):
                # print(root, dirs, files)
                print(ph)
                txt.insert(INSERT, ''+str(int(t_f))+' : '+ph+'\n')
                # if
                # print(os.path.abspath(file_name))

                print(t_m, t_sys, t_f)

    with open('resultat.txt','w') as f:
        f.write(str(txt.get(1.0, END)))
        f.close()
    # print(str(txt.get(1.0, END)))

def clicked():

    # lbl.configure(text=res)
    # print(res)
    lookmf(disk.get(), dney.get())

def start():
    global disk, dney, txt
    window = Tk()
    window.title('Analiz spaces')
    window.geometry('800x500')

    t_disk = Label(window, text="Укажите диск для анализа", font=("Arial Bold", 10))
    t_disk.grid(column=0, row=0)
    disk = Entry(window, width=10)
    disk.insert(0,"C")
    disk.grid(column=1, row=0)

    t_dney = Label(window, text="количество дней для анализа", font=("Arial Bold", 10))
    t_dney.grid(column=0, row=1)
    dney = Entry(window, width=10)
    dney.insert(0,'10')
    dney.grid(column=1, row=1)

    btn = Button(window, text="Анализировать!", command=clicked)
    btn.grid(column=1, row=2)

    txt = scrolledtext.ScrolledText(window, width=90, height=25)
    txt.grid(column=0, row=3, columnspan=2)

    window.mainloop()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    start()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
