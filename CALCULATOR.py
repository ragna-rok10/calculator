# CODE FOR CALCULATOR.
from tkinter import *  # USE TO IMPORT ALL THE LIBRARY.
import math     # TO USE ALL THE MATHEMATICAL FUNCTIONS.
from pygame import mixer        # TO IMPORT AND USE AUDIO FILES.
import speech_recognition

mixer.init()
def click(value):
    ex = entryField.get()
    answer=' '
    try:

        if value == 'C':
            ex = ex[0:len(ex)-1]
            entryField.delete(0,END)
            entryField.insert(0,ex)
            return

        elif value == 'CE':
            entryField.delete(0,END)

        elif value == '√':
            answer=math.sqrt(eval(ex))

        elif value == 'cosΘ':
            answer=math.cos(math.radians(eval(ex)))

        elif value == 'tanΘ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinΘ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == 'π':
            answer=math.pi

        elif value == '2π':
            answer=2*math.pi

        elif value == 'cosh':
            answer=math.cosh(eval(ex))

        elif value == 'tanh':
            answer=math.tanh(eval(ex))

        elif value == 'sinh':
            answer=math.sinh(eval(ex))

        elif value == chr(8731):
            answer=eval(ex)**(1/3)

        elif value == 'x\u02b8':
            answer=entryField.insert(END,'**')
            return

        elif value == 'x\u00B3':
            answer=eval(ex)**3

        elif value == 'x\u00B2':
            answer=eval(ex)**2

        elif value == 'ln':
            answer=math.log(eval(ex))

        elif value == 'deg':
            answer=math.degrees(eval(ex))

        elif value == 'rad':
            answer=math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log10':
            answer= math.log10(eval(ex))

        elif value == 'x!':
            answer=math.factorial(eval(ex))

        elif value == chr(247):
            entryField.insert(END,"/")
            return

        elif value == '=':
            answer=eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0,END)
        entryField.insert(0,answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b

def mod(a,b):
    return a%b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations = {'ADD':add, 'ADDITION':add, 'SUM':add, 'PLUS':add,'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
              'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,'DIVISION': div, 'DIV': div, 'DIVIDE': div,"LCM":lcm ,
              'HCF':hcf,'MOD':mod ,'REMAINDER' :mod , 'MODULUS' :mod }

def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass

    return l
def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer() #ACCESS METHODS.
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list= text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l= findNumbers(text_list)
                    print(l)
                    result = operations[word.upper()](l[0],l[1])
                    entryField.delete(0,END)
                    entryField.insert(END,result)

                else:
                    pass

        except:
            pass

root = Tk() # HELPS IN CREATING THE WONDOW FOR CALCULATOR.
root.title('SMART CALCULATOR BY RAJJO') # USED TO GIVE THE TITLE.
root.config(bg='lime green') #FOR THE BACKGROUND COLOR.
root.geometry('680x486+100+100') # FOR THE DIMENSION OF THE WINDOW.

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(root,image=logoImage,bg='lime green')
logoLabel.grid(row=0,column=0)
entryField=Entry(root,font=('arial', 20, 'bold'), bg='lime green', fg='white', bd=10, relief=SUNKEN, width=30) # FOR THE INPUTS ON THE WINDOW AND DESIGN.
entryField.grid(row=0, column=0,columnspan=8)

micImage=PhotoImage(file='microphone.png')
micButton=Button(root,image=micImage,bg='lime green',activebackground='lime green',command=audio)
micButton.grid(row=0,column=7)
button_text_List = ["C", "CE", "√", "+", "π", "cosΘ", "tanΘ", "sinΘ", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh", "4", "5", "6", "*", chr(8731),
                    "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg", "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]
rowvalue=1
columnvalue=0
for i in button_text_List:

    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='lime green',fg='white',
                  font=('arial',18,'bold'),activebackground='lime green',command=lambda button=i:click(button))
    button.grid(row=rowvalue, column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0

root.mainloop()# KEEPS WINDOW ON A LOOP.

# END OF CODE.