from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_text = ""
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps, check_text, timer
    window.after_cancel(timer)
    check_text = ""
    reps = 0
    checkmark.config(text=check_text)
    text_top.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN*60)
        text_top.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        text_top.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN+60)
        text_top.config(text="Long break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps, check_text, timer
    if count//60 < 10:
        minutes = "0"+str(count//60)
    else:
        minutes = count // 60
    if count % 60 < 10:
        seconds = "0"+str(count % 60)
    else:
        seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_text += "✔"
            checkmark.config(text=check_text)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000,)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="D:\\python\\pomodoro\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
text_top = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
text_top.grid(row=0, column=1)
checkmark = Label(text=check_text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark.grid(row=3, column=1)
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
