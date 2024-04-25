from tkinter import *
def buttonClick(number):
    global operator
    operator=operator+str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator=""
    input_value.set("")

def buttonequal():
    global operator
    result=str(eval(operator))
    input_value.set(result)
    operator=""

main=Tk()
main.title("calculator")

operator=""
input_value=StringVar()
display_text=Entry(main,font=("green",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,bg="powder blue",justify=RIGHT)
display_text.grid(columnspan=4)

#row1
btn_7=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="7",command=lambda:buttonClick(7))
btn_7.grid(row=1,column=0)
             
btn_8=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="8",command=lambda:buttonClick(8))
btn_8.grid(row=1,column=1)

btn_9=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="9",command=lambda:buttonClick(9))
btn_9.grid(row=1,column=2)

btn_plus=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="+",command=lambda:buttonClick("+"))
btn_plus.grid(row=1,column=3)



#row2
btn_4=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="4",command=lambda:buttonClick(4))
btn_4.grid(row=2,column=0)
             
btn_5=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="5",command=lambda:buttonClick(5))
btn_5.grid(row=2,column=1)

btn_6=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="6",command=lambda:buttonClick(6))
btn_6.grid(row=2,column=2)
btn_minus=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="-",command=lambda:buttonClick("-"))
btn_minus.grid(row=2,column=3)  




#row3
btn_1=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="1",command=lambda:buttonClick(1))
btn_1.grid(row=3,column=0)
             
btn_2=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="2",command=lambda:buttonClick(2))
btn_2.grid(row=3,column=1)

btn_3=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="3",command=lambda:buttonClick(3))
btn_3.grid(row=3,column=2)
btn_mult=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="*",command=lambda:buttonClick("*"))
btn_mult.grid(row=3,column=3)  




#row4
btn_0=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="0",command=lambda:buttonClick(0))
btn_0.grid(row=4,column=0)
             
btn_c=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="C",command=lambda:buttonClear())
btn_c.grid(row=4,column=1)

btn_equal=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="=",command=lambda:buttonequal())
btn_equal.grid(row=4,column=2)
btn_division=Button(main,padx=16,fg="black",font=("green",20,"bold"),text="/",command=lambda:buttonClick("/"))
btn_division.grid(row=4,column=3)  




main.mainloop()