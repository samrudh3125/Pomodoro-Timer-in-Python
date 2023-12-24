import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timerr=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timerr)
    canvas.itemconfig(timer_text,text="00:00")
    text.config(text="TIMER")
    check_mark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec=WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%2==1:
        timer(work_sec)
        text.config(text="Work",fg=GREEN)
    elif reps==8:
        timer(long_break_sec)
        text.config(text="Long Break",fg=RED)
    else:
        timer(short_break_sec)
        text.config(text="Short Break",fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(time):
    global timerr
    count_min=math.floor(time/60)
    count_sec=f"0{time%60}" if time%60<10 else time%60
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if time>0:
        timerr=window.after(1000,timer,time-1)
    else:
        start_timer()
        mark=""
        for i in range(math.floor(reps/2)):
            mark+="✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

text=tkinter.Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))

text.grid(column=1,row=0)
canvas=tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
image=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=tkinter.Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

Reset_button=tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
Reset_button.grid(column=2,row=2)

check_mark=tkinter.Label(text="",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()