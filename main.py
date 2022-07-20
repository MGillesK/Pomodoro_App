from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    window.after_cancel(timer)
    canvas_center.itemconfig(timer_text, text="25:00")

    label_timer.config(text="Timer")
    label_tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        #count_sec = "0"+str(count_sec)
        count_sec = f"0{count_sec}"

    canvas_center.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        label_tick.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
#window.after()

label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

canvas_center = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0 )
tomato_img = PhotoImage(file="tomato.png")
def_image = canvas_center.create_image(103, 112, image=tomato_img)
timer_text = canvas_center.create_text(103, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas_center.grid(column=1, row=1)

button_start = Button(text="Start", bg=YELLOW, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", bg=YELLOW, command=reset_timer)
button_reset.grid(column=2, row=2)

label_tick = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
label_tick.grid(column=1, row=3)

window.mainloop()