import matplotlib.pyplot as plt
import numpy as np
from datetime import date
from workalendar.asia import Singapore
import calendar
import csv


# Make data: I have 3 groups and 7 subgroups
def create_qrqrc_calendar(colors_A_list,colors_B_list,colors_C_list):
    #size + name + section of the chart
    group_size= [11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6,11.6]
    group_A=['','','','','','','','A','','','','','','','','','','','','','','','','','','','','','','','']
    group_B=['','','','','','','','B','','','','','','','','','','','','','','','','','','','','','','','']
    group_C=['','','','','','','','C','','','','','','','','','','','','','','','','','','','','','','','']
    group_D=['8','7','6','5','4','3','2','1','31','30','29','28','27','26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','9']

    # Create colors
    a, b, c, d = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Greys]
    white = a(0)
    red = b(180)
    green = c(160)
    black = a(0)

    #colors_A_list=[red, green, d(255),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6)]
    #colors_B_list=[a(0.6), a(0.6), a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6)]
    #colors_C_list=[a(0.6), a(0.6), a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6),a(0.6)]
    # First Ring (outside)
    fig, ax = plt.subplots()
    ax.axis('equal')
    # create Rings
    mypie, _ = ax.pie(group_size, radius=1.5, labels=group_A,labeldistance=0.9, colors=colors_A_list)
    plt.setp(mypie, width=0.3, edgecolor='black')
    mypie2, _ = ax.pie(group_size, radius=1.5 - 0.3, labels=group_B,labeldistance=0.9,colors=colors_B_list)
    plt.setp(mypie2, width=0.3, edgecolor='black')
    mypie3, _ = ax.pie(group_size, radius=1.5- 0.6, labels=group_C,labeldistance=0.9,colors=colors_C_list)
    plt.setp(mypie3, width=0.3, edgecolor='black')
    #this one is for the number (as legend)
    mypie4, _ = ax.pie(group_size, radius=1.8, labels=group_D,labeldistance=0.9,colors=colors_C_list)
    plt.setp(mypie4, width=0, edgecolor='white')
    plt.margins(0, 0)
    # show it
    return plt.show()

def qrqc_calendar():
    cal=Singapore()
    c= calendar.TextCalendar(calendar.SATURDAY)
    str1 = c.itermonthdays2(date.today().year,date.today().month)
    mylist=[]
    for x in str1:
        mylist.append(x)
    blackdaylist=[]
    j=0
    for i in mylist:
        if i[0]!=0:
            if cal.is_working_day(date(date.today().year,date.today().month, i[0]))== False:
                blackdaylist.append('black')
            if cal.is_working_day(date(date.today().year,date.today().month, i[0]))==True:
                blackdaylist.append('white')
    while len(blackdaylist)<31 :
        blackdaylist.append('black')

    blackdaylist.reverse()
    blackdaylist = np.roll(blackdaylist, 8)
    colors_A_list = []
    colors_B_list = []
    colors_C_list = []
    colors_A_list =blackdaylist
    colors_B_list =blackdaylist
    colors_C_list =blackdaylist
    create_qrqrc_calendar(colors_A_list,colors_B_list,colors_C_list)

def save(last_qrqc_date):
    with open('record.csv', 'r') as f:
        reader = csv.reader(f)
        record = list(reader)
    file_name="qrqc_"+str(last_qrqc_date)+".csv"
    with open(file_name, mode='w+') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(record)
    return
def loading():
    with open('record.csv', 'r') as f:
        reader = csv.reader(f)
        record = list(reader)
    colors_A_list = record[0]
    colors_B_list = record[1]
    colors_C_list = record[2]
    i=0
    while i < 4:
        colors_A_list.pop(0)
        colors_B_list.pop(0)
        colors_C_list.pop(0)
        i=i+1
    colors_A_list.reverse()
    colors_A_list=np.roll(colors_A_list,8)
    colors_B_list.reverse()
    colors_B_list = np.roll(colors_B_list, 8)
    colors_C_list.reverse()
    colors_C_list = np.roll(colors_C_list, 8)
    print("A:", colors_A_list)
    print("B:", colors_B_list)
    print("C:", colors_C_list)
    create_qrqrc_calendar(colors_A_list, colors_B_list, colors_C_list)

if __name__ == "__main__":
    # execute only if run as a script
    with open('record.csv', 'r') as f:
        reader = csv.reader(f)
        record = list(reader)
    last_qrqc_date = date(int(record[0].pop(0)),int(record[0].pop(0)),int(record[0].pop(0)))
    if date.today().month == last_qrqc_date.month and date.today().year == last_qrqc_date.year:
        loading()
    elif date.today().month != last_qrqc_date.month or date.today().year != last_qrqc_date.year:
        save(last_qrqc_date)
        qrqc_calendar()
    else:
        print("error")
        print("default mode")
        qrqc_calendar()
    #    save()
    #    qrqc_calendar()
    #else:
    #    loading()




    #    blackdaylist=['red', 'red', 'red', 'white', 'black', 'black', 'white', 'white', 'black', 'black', 'white', 'white',
     #    'white', 'white', 'white', 'black', 'black', 'white', 'white', 'white', 'white', 'white', 'black', 'black',
      #   'white', 'white', 'white', 'white', 'black', 'black', 'black']
        #create_qrqrc_calendar(blackdaylist)
