import math
import tkinter
from tkinter import Tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check= ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lb.config(text="Timer", fg=GREEN)
    check1.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    global check
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_br_sec = LONG_BREAK_MIN*60
    if reps % 2 == 1:
        count_down(work_sec)
        timer_lb.config(text="Work", fg=GREEN)
    if reps == 8:
        count_down(long_br_sec)
        check += "✔"
        check1.config(text=check)
        timer_lb.config(text="Long break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        check += "✔"
        check1.config(text=check)
        timer_lb.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_minute = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_lb = tkinter.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_lb.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(column=1, row=1)

check1 = tkinter.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
check1.grid(row=3, column=1)

start_btn = tkinter.Button(text="start", font=(FONT_NAME, 15, "bold"), fg=RED, width=5,
                           border=0, highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = tkinter.Button(text="reset", font=(FONT_NAME, 15, "bold"), fg=RED, width=5,
                           border=0, highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=5, row=2)


window.mainloop()



