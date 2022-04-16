import tkinter
window = tkinter.Tk()
window.title('PWD GEN')
window.geometry("300x200+10+20")
window.hi_there = tkinter.Button(window)
#Create a tkinter window and making it look good
import random
chars = "'1234567890`~!@#$%^&*()_-=+{}|:><?.,/;[]\"\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
l = []
for i in chars:
  l.append(i)

pwd=''
for i in range(10):
  pwd = pwd + random.choice(l)
print(pwd)  

