# Streamlit version
import streamlit as st
from textblob import TextBlob
      


def correct_spelling(get_data):
    corr = TextBlob(get_data)
    data = corr.correct()
    return data

def main():
    st.set_page_config(page_title="Spelling Checker", page_icon="✨")
    
    st.title("Spelling Checker")

    incorrect_spelling = st.text_input("Enter Incorrect Spelling:")
    
    if st.button("Correct Spelling"):
        corrected_spelling = correct_spelling(incorrect_spelling)
        st.success(f"Correct Spelling: {corrected_spelling}")

if __name__ == "__main__":
    main()


# Tkinter version
from textblob import TextBlob
from tkinter import *

def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0, END)
    enter2.insert(0, data)

def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("900x670+120+120")
    win.resizable(False, False)
    win.config(bg="gray")
    win.title("Spelling Checker")

    label1 = Label(win, text="Incorrect Spelling", font=("Time New Roman", 25, "bold"), bg="sky blue", fg="Navy blue")
    label1.place(x=300, y=50, height=60, width=350)

    enter1 = Entry(win, font=("Time New Roman", 20),bg="lavender", bd=5)
    enter1.place(x=250, y=150, height=60, width=450)

    label2 = Label(win, text="Correct Spelling", font=("Time New Roman", 25, "bold"), bg="sky blue", fg="Navy blue")
    label2.place(x=300, y=250, height=60, width=350)

    enter2 = Entry(win, font=("Time New Roman", 20), bg="lavender", bd=5)
    enter2.place(x=250, y=350, height=60, width=450)

    button = Button(win, text="Check", font=("Time New Roman", 25, "bold"), bg="MediumSeaGreen", bd=6, command=correct_spelling)
    button.place(x=350, y=450, height=60, width=250)

    win.mainloop()

if __name__ == "__main__":
    main_window()
