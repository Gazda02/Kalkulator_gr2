# Biblioteki

from tkinter import *
from math import *


# Karol Gazda - Tymczasowe funkcje

# Weronika Juszczyk:
expression = ""  # zmienna przechowująca równanie


# funkcja wypisująca równania na wyświetlacz kalkulatora
def press(number):
    global expression
    expression = expression + str(number)
    equasion.set(expression)


# funkcja czyszcząca wyświetlacz kalkulatora
def clear():
    global expression
    expression = ""
    equasion.set('0')


# Jakub Gicala
# funkcja czyszcząca pamięć
def clear_previous():
    global previous
    prev1.set('')
    prev2.set('')
    prev3.set('')
    prev4.set('')
    prev5.set('')
    prev6.set('')
    prev7.set('')
    prev8.set('')
    prev9.set('')
    prev10.set('')
    previous = ['', '', '', '', '', '', '', '', '', '']


previous = ['', '', '', '', '', '', '', '', '', '']



# Weronika Juszczyk:
# lista przechowująca równania
# wyświetlanie poprzenich równań po kolei

def press_equal():
    global expression, previous
    try:
        prev = str(expression)
        names = {'ln': log, 'sqrt': sqrt, }
        total = eval(expression, names)  # wynik równania
        equasion.set(total)  # wypisanie wyniku na wyświetlacz kalkulatora
        expression = str(total)
        previous.insert(0, prev)
        if len(previous) > 11:
            previous.pop()
        print(previous)
        prev1.set(previous[0])
        prev2.set(previous[1])
        prev3.set(previous[2])
        prev4.set(previous[3])
        prev5.set(previous[4])
        prev6.set(previous[5])
        prev7.set(previous[6])
        prev8.set(previous[7])
        prev9.set(previous[8])
        prev10.set(previous[9])
    except:
        equasion.set("Błąd")
        expression = ""

# wywoływanie wyników z historii Piotr Grzyb

def previous_equasion(number):
    global expression, previous
    try:
        names = {'ln': log, 'sqrt': sqrt, }
        prev = str(previous[number-1])
        total = eval(prev, names)
        expression = expression + str(total)
        equasion.set(expression)
    except:
        pass



# Karol Gazda- Tymczasowe stałe

# Ustawienie okna kalkulatora
gui = Tk()
gui.title('Kalkulator')

gui.minsize(width=480, height=309)
gui.maxsize(width=1280, height=309)
gui.geometry('1280x309')
gui.configure(bg='#0000CC')
# gui.iconbitmap('Calculator_icon.ico')
gui.resizable(True, False)
# Stworzenie ramy na przyciski
button_frame = Frame(gui, bg='#0000CC')
button_frame.pack()
# Zdefiniowanie zmiennej equasion klasy StringVar przechowującej wpisywane wyrażenie
equasion = StringVar()

# Piotr Grzyb- zdefiniowanie zmiennych klasy StringVar
# prev1-prev10 przechowyjących wpisywane, poprzednie wyrażenia)
prev1 = StringVar()
prev2 = StringVar()
prev3 = StringVar()
prev4 = StringVar()
prev5 = StringVar()
prev6 = StringVar()
prev7 = StringVar()
prev8 = StringVar()
prev9 = StringVar()
prev10 = StringVar()
equasion.set('0')
# Stworzenie pól przechowujących 10 poprzednich równań i głównego pola do wpisywania wyrażenia
expression_field = Entry(button_frame, textvariable=equasion, justify='right', font=('calibri', 20, 'bold',),
                         relief='ridge', borderwidth=5, bg='#0000CC')
previous_expression_field_1 = Entry(button_frame, textvariable=prev1, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_2 = Entry(button_frame, textvariable=prev2, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_3 = Entry(button_frame, textvariable=prev3, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_4 = Entry(button_frame, textvariable=prev4, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_5 = Entry(button_frame, textvariable=prev5, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_6 = Entry(button_frame, textvariable=prev6, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_7 = Entry(button_frame, textvariable=prev7, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_8 = Entry(button_frame, textvariable=prev8, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_9 = Entry(button_frame, textvariable=prev9, justify='right', font=('calibri', 20, 'bold'),
                                    relief='ridge', borderwidth=5, )
previous_expression_field_10 = Entry(button_frame, textvariable=prev10, justify='right', font=('calibri', 20, 'bold'),
                                     relief='ridge', borderwidth=5, )
# Stworzenie wszystkich przycisków- Weronika Juszczyk
# Poprawienie funkcji ln oraz sqrt- Piotr Grzyb
# Przypianie funkcjonalności przyciską previous- Piotr Grzyb
imaginary_unit_button = Button(button_frame, text='i', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                               width=4, height=1, command=lambda: press('j'))
decimal_point_button = Button(button_frame, text='.', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                              width=4, height=1, command=lambda: press('.'))
button_0 = Button(button_frame, text='0', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(0))
button_1 = Button(button_frame, text='1', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(1))
button_2 = Button(button_frame, text='2', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(2))
button_3 = Button(button_frame, text='3', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(3))
button_4 = Button(button_frame, text='4', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(4))
button_5 = Button(button_frame, text='5', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(5))
button_6 = Button(button_frame, text='6', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(6))
button_7 = Button(button_frame, text='7', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(7))
button_8 = Button(button_frame, text='8', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(8))
button_9 = Button(button_frame, text='9', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(9))
addition_button = Button(button_frame, text='+', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                         width=4, height=1, command=lambda: press('+'))
substraction_button = Button(button_frame, text='-', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                             width=4, height=1, command=lambda: press('-'))
multiplication_button = Button(button_frame, text='*', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                               width=4, height=1, command=lambda: press('*'))
division_button = Button(button_frame, text='/', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                         width=4, height=1, command=lambda: press('/'))
power_button = Button(button_frame, text='^', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=lambda: press('**'))
button_r_bracket = Button(button_frame, text='(', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                          width=4,
                          height=1, command=lambda: press('('))
button_l_bracket = Button(button_frame, text=')', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                          width=4,
                          height=1, command=lambda: press(')'))
button_ln = Button(button_frame, text='ln', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                   height=1, command=lambda: press('ln('))
square_root_button = Button(button_frame, text='sqrt', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                            width=4, height=1, command=lambda: press('sqrt('))
clear_button = Button(button_frame, text='C', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=clear)
equal_button = Button(button_frame, text='=', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=press_equal)
clear_previous_button = Button(button_frame, text='P', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                               width=4,
                               height=1, command=clear_previous)
#ten przycisk do 5 potęgi Karol Gazda
pow5 = Button(button_frame, text='x^5', font=('calibri', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
              height=1, command=lambda: press('**5'))
previous_expression_button_1 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(1))
previous_expression_button_2 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(2))
previous_expression_button_3 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(3))
previous_expression_button_4 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(4))
previous_expression_button_5 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(5))
previous_expression_button_6 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(6))
previous_expression_button_7 = Button(button_frame, text='->',font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(7))
previous_expression_button_8 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(8))
previous_expression_button_9 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                      bg='#0000CC', width=4,
                                      height=1, command=lambda: previous_equasion(9))
previous_expression_button_10 = Button(button_frame, text='->', font=('calibri', 20), relief='ridge', borderwidth=5,
                                       bg='#0000CC', width=4,
                                       height=1, command=lambda: previous_equasion(10))
# Tutaj rozmieszczam przyciski oraz pola- Jakub Gicala
# Zmiana pozycji previous_expression_button oraz previous_expression_field w celu zwiekszenia czytelności kalkulatora- Weronika Juszczyk

expression_field.grid(row=0, column=0, columnspan=5, ipadx=84, ipady=9, pady=0)

#umieszczenie przycisku Karol Gazda
pow5.grid(row=3, column=4)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
addition_button.grid(row=1, column=3)
power_button.grid(row=1, column=4)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
substraction_button.grid(row=2, column=3)
square_root_button.grid(row=2, column=4)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
multiplication_button.grid(row=3, column=3)
clear_button.grid(row=0, column=5)
button_0.grid(row=4, column=0)
imaginary_unit_button.grid(row=4, column=1)
decimal_point_button.grid(row=4, column=2)
division_button.grid(row=4, column=3)
equal_button.grid(row=4, column=4)
clear_previous_button.grid(row=4, column=5)
clear_previous_button.grid(row=4, column=5)
button_r_bracket.grid(row=1, column=5)
button_l_bracket.grid(row=2, column=5)
button_ln.grid(row=3, column=5)
previous_expression_button_1.grid(row=0, column=6)
previous_expression_button_2.grid(row=1, column=6)
previous_expression_button_3.grid(row=2, column=6)
previous_expression_button_4.grid(row=3, column=6)
previous_expression_button_5.grid(row=4, column=6)
previous_expression_button_6.grid(row=0, column=13)
previous_expression_button_7.grid(row=1, column=13)
previous_expression_button_8.grid(row=2, column=13)
previous_expression_button_9.grid(row=3, column=13)
previous_expression_button_10.grid(row=4, column=13)
previous_expression_field_1.grid(row=0, column=7, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_2.grid(row=1, column=7, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_3.grid(row=2, column=7, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_4.grid(row=3, column=7, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_5.grid(row=4, column=7, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_6.grid(row=0, column=14, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_7.grid(row=1, column=14, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_8.grid(row=2, column=14, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_9.grid(row=3, column=14, columnspan=5, ipadx=4, ipady=9, pady=0)
previous_expression_field_10.grid(row=4, column=14, columnspan=5, ipadx=4, ipady=9, pady=0)

# Uruchomienie kalkulatora
gui.mainloop()

