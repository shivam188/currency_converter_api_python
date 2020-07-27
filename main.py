from tkinter import *
import sys
import json
import urllib.request
import country_list

def currency_converter():
    first = variable1.get()
    first = first[0:3]
    second = variable2.get()
    second = second[0:3]

    amount = int(txt3.get())
    convert = first + "_" +second
    url = "https://free.currconv.com/api/v7/convert?q=" + convert + "&compact=ultra&apiKey=d5d687fa6c9b6ac1836f"
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
    for i in data.values():
        c = amount * i
    s.set(str(c))

def exitFun():
    sys.exit(0)


options = country_list.cur_list
options.sort()
root = Tk()
root.geometry("600x600+200+200")
root.title("Currency Converter")

lbl1 = Label(root, text='Currency From : ')

variable1 = StringVar(root)
variable1.set(options[0])
txt1 = OptionMenu(root, variable1, *options)


lbl2 = Label(root, text='Currency To : ')
variable2 = StringVar(root)
variable2.set(options[0])
txt2 = OptionMenu(root, variable2, *options)


lbl3 = Label(root, text='Amount : ')
txt3 = Entry(root)


btn1 = Button(root, text='Convert', command=currency_converter)
btn2 = Button(root, text='exit', command=exitFun)

lbl1.place(x=100, y=100)
txt1.place(x=220, y=100)

lbl2.place(x=100, y=150)
txt2.place(x=220, y=150)

lbl3.place(x=100, y=200)
txt3.place(x=220, y=200)

btn1.place(x=120, y=250)
btn2.place(x=200, y=250)

s = StringVar()
lbl3 = Label(root, textvariable=s)
lbl3.place(x=100, y=300)

root.mainloop()
