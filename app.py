from tkinter import *
from chatbot import get_response

# Colors
BG_APP = "#ffffff"
BG_TOP = "#ffffff"
BG_CHAT = "#ffffff"
BG_ENTRY = "#D9DDDC"
ACCENT = "#0095f6"
TEXT_DARK = "#262626"
TEXT_LIGHT = "#8e8e8e"

PLACEHOLDER = "Type your message here..."


def add_message(text, is_user=False):
    row = Frame(messages_frame, bg=BG_CHAT)
    row.pack(fill=X, pady=4)

    if is_user:
        bubble_bg = ACCENT
        bubble_fg = "white"
        Label(
            row,
            text=text,
            bg=bubble_bg,
            fg=bubble_fg,
            font=("times new roman", 11),
            padx=10,
            pady=6,
            wraplength=260,
            justify=LEFT
        ).pack(side=RIGHT, padx=(80, 10))
    else:
        Label(
            row,
            text=text,
            bg="#efefef",
            fg=TEXT_DARK,
            font=("times new roman", 11),
            padx=10,
            pady=6,
            wraplength=260,
            justify=LEFT
        ).pack(side=LEFT, padx=(10, 80))

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)


def send(event=None):
    user_input = entry.get().strip()

    if not user_input:
        return

    add_message(user_input, is_user=True)
    add_message(get_response(user_input), is_user=False)

    entry.delete(0, END)


# Enable entry when user clicks
def enable_entry(event):
    if entry["state"] == "disabled":
        entry.config(state="normal", fg=TEXT_DARK)
        entry.delete(0, END)
        entry.focus()


# Main window
root = Tk()
root.title("Akshay's Chatmate")
root.geometry("500x400")
root.configure(bg=BG_APP)

# Top bar
Frame(root, bg=BG_TOP, height=50).pack(fill=X)

Label(
    root,
    text="🙏 How may I help you!",
    bg=BG_TOP,
    fg=TEXT_DARK,
    font=("times new roman", 14, "bold")
).place(x=15, y=10)

# Chat area
chat_frame = Frame(root, bg=BG_CHAT)
chat_frame.pack(fill=BOTH, expand=True)

canvas = Canvas(chat_frame, bg=BG_CHAT, bd=0, highlightthickness=0)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(chat_frame, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)

messages_frame = Frame(canvas, bg=BG_CHAT)
canvas.create_window((0, 0), window=messages_frame, anchor="nw")

messages_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Bottom input area
bottom = Frame(root, bg=BG_APP)
bottom.pack(fill=X, pady=8)

entry_bg = Frame(bottom, bg=BG_ENTRY)
entry_bg.pack(side=LEFT, padx=(10, 5), fill=X, expand=True)

entry = Entry(
    entry_bg,
    bg=BG_ENTRY,
    fg=TEXT_LIGHT,
    bd=0,
    font=("times new roman", 11),
    state="disabled"
)
entry.pack(fill=X, padx=8, pady=6)
entry.insert(0, PLACEHOLDER)

# Click to enable
entry.bind("<Button-1>", enable_entry)
entry.bind("<Return>", send)

Button(
    bottom,
    text="Send",
    command=send,
    bg=ACCENT,
    fg="white",
    bd=0,
    padx=14,
    pady=6,
    font=("times new roman", 10, "bold"),
    cursor="hand2"
).pack(side=RIGHT, padx=(0, 10))

root.mainloop()
