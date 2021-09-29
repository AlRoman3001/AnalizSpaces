from tkinter import *
from tkinter import scrolledtext
import os, time
import psutil

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def sysinfo():

    print('************* системная информация *******************')
    print("Тип ОС: "+str(os.name))
    print("Общая информация: "+str(os.environ))
    # print(os.path.getsize("c:"))
    totalsize = psutil.disk_usage('C:').total / 2 ** 30
    free = psutil.disk_usage("c:").free / (1024 * 1024 * 1024)
    print('Данные диска: ' + str(psutil.disk_usage('c:')))
    print('Размер диска: ', f"{totalsize:.4}", 'GB,  ',f"{free:.4} Gb свободно на диске: {'C:'}")
    print('Системная статистика диска: ' + str(psutil.disk_io_counters('c:')))
    # print(f"{free:.4} Gb free on disk {'C:'}")

    print('Статистика процессора: (кол переключений, прерываний, прог прерываний, сис вызовов) :' + str(psutil.cpu_stats()))
    # print('Температура процессора: '+str(psutil.sensors_temperatures()))
    # print('Вентилятор: '+str(psutil.sensors_fans()))
    print('Время автономной работы батареи: ' + str(psutil.sensors_battery()))
    print('Затраченое время процессора (секунд) на пользователя, сис процессы, простоя, апарат прерыв, отл вызовы : ' + str(psutil.cpu_times()))
    print('Загрузка процессора (%): ' + str(psutil.cpu_percent(interval=1))) # есть нюансы!
    print('Количество ядер процессора (шт.): ' + str(psutil.cpu_count(logical=False)))
    print('Виртуальная память: ' + str(psutil.virtual_memory()))
    print('Статистика подкачки памяти: ' + str(psutil.swap_memory()))


    print('Статистика сетевого вводв вывода: ' + str(psutil.net_io_counters()))
    print('Общесистемные соединения сокетов: ' + str(psutil.net_connections()))
    print('Адреса сетевой карты: ' + str(psutil.net_if_addrs()))
    print('Информация о сетевых картах: ' + str(psutil.net_if_stats()))

    # print('Время загрузки системы (???): ' + str(psutil.bot_time()))
    print('Подключенные пользователи: ' + str(psutil.users()))
    print('Запущеные PID (id процессов): ' + str(psutil.pids()))
    print('Запущенные процессы:', end=' ')
    for proc in psutil.process_iter(['pid', 'name', 'username']):
              print(proc.info, end=' ')
    print(' ')
    print('Соединения сокитов: ' + str(psutil.net_connections()))

    print(': ' + str(psutil.Process().open_files()))

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

    sysinfo()


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
    sysinfo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
