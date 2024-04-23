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
CHECKMARK = ""
TIMER = None
REPS = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, CHECKMARK
    window.after_cancel(TIMER)
    REPS = 0
    CHECKMARK = ""
    canvas.itemconfig(time_text, text="Pomodoro")
    ticks.config(text=CHECKMARK)
    label.config(text="TIMER", fg=YELLOW)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS, CHECKMARK
    REPS += 1
    work_secs = WORK_MIN * 60
    small_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        label.config(text="LONG BREAK", fg=RED)
        CHECKMARK += "✔"
        ticks.config(text=CHECKMARK)
        CHECKMARK = "COMPLETED"
        count(long_break_secs)

    elif REPS % 2 == 0:
        label.config(text="SHORT BREAK", fg="PINK")
        CHECKMARK += "✔"
        ticks.config(text=CHECKMARK)
        count(small_break_secs)

    else:
        label.config(text="WORK", fg=GREEN)
        count(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count(minutes):
    global TIMER
    if minutes > 0:
        if minutes % 60 < 10:
            canvas.itemconfig(time_text, text=f"{int(minutes / 60)}:0{int(minutes % 60)}")

        else:
            canvas.itemconfig(time_text, text=f"{int(minutes / 60)}:{int(minutes % 60)}")

        TIMER = window.after(1000, count, minutes-1)
    else:
        if CHECKMARK == "COMPLETED":
            reset_timer()
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=PINK)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=YELLOW, bg=PINK)
label.grid(column=1, row=0)

canvas = Canvas(width=250, height=300, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 150, image=tomato_img)
time_text = canvas.create_text(125, 172, text="Pomodoro", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

ticks = Label(text=CHECKMARK, font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=PINK)
ticks.grid(column=1, row=3)

window.mainloop()
