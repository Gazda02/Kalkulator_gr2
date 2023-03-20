# TEST

print('Hello')
print('Hi')
print('Hello world')
print('000000000')
print('Halo')

#Biblioteki

from tkinter import *

from symbol import *

# Karol Gazda - Tymczasowe funkcje


#TODO: Ta funkcja ma "wkładać" kolejne elementy do rówannia
def press():
    pass

#TODO: Ta funkcja ma wyczyścić bufor equasion
def clear():
    pass

#TODO: Ta funkcja ma czyścić bufor equasion i wyświetlać wynik. Powinna też (chyba) wrzucić równanie do tablicy previous
def press_equal():
    pass

#TODO: Ta funkcja powinna wczytać zapamiętane równanie z tablicy
def previous_equasion():
    pass

# Karol Gazda - Tymczasowe stałe


#TODO: to będzie w przyszłości tablica zawierająca 10 poprzednich równań
previous=['0','0','0','0','0','0','0','0','0','0']


# Jakub Gicala - Wstępne GUI


#Ustawienie okna kalkulatora
gui = Tk()
gui.title('Kalkulator')
gui.geometry('400x968')
gui.configure(bg='#ee5aa4')
gui.iconbitmap('Calculator_icon.ico')
gui.resizable(False, False)

#Stworzenie ramy na przyciski
button_frame = Frame(gui, bg='#ee5aa4')
button_frame.pack()

#Zdefiniowanie zmiennej equasion klasy StringVar przechowującej wpisywane wyrażenie
equasion = StringVar()
equasion.set('0')

#Stworzenie pól przechowujących 10 poprzednich równań i głównego pola do wpisywania wyrażenia
expression_field = Entry(button_frame, textvariable=equasion, justify='right', font=('arial', 20, 'bold',),
                         relief='ridge', borderwidth=20,bg='#f24986')

previous_expression_field_1 = Entry(button_frame, textvariable=previous[0], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5, )
previous_expression_field_2 = Entry(button_frame, textvariable=previous[1], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5,)
previous_expression_field_3 = Entry(button_frame, textvariable=previous[2], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5, )
previous_expression_field_4 = Entry(button_frame, textvariable=previous[3], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5,)
previous_expression_field_5 = Entry(button_frame, textvariable=previous[4], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5, )
previous_expression_field_6 = Entry(button_frame, textvariable=previous[5], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5,)
previous_expression_field_7 = Entry(button_frame, textvariable=previous[6], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5,)
previous_expression_field_8 = Entry(button_frame, textvariable=previous[7], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5,)
previous_expression_field_9 = Entry(button_frame, textvariable=previous[8], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5, )
previous_expression_field_10 = Entry(button_frame, textvariable=previous[9], justify='right', font=('arial', 20, 'bold'),
                         relief='ridge', borderwidth=5, )

#Stworzenie wszystkich przycisków
imaginary_unit_button = Button(button_frame, text='i', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                               width=4, height=1, command=lambda: press('i'))
decimal_point_button = Button(button_frame, text='.', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                              width=4, height=1, command=lambda: press('.'))
button_0 = Button(button_frame, text='0', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(0))
button_1 = Button(button_frame, text='1', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(1))
button_2 = Button(button_frame, text='2', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(2))
button_3 = Button(button_frame, text='3', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(3))
button_4 = Button(button_frame, text='4', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(4))
button_5 = Button(button_frame, text='5', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(5))
button_6 = Button(button_frame, text='6', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(6))
button_7 = Button(button_frame, text='7', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(7))
button_8 = Button(button_frame, text='8', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(8))
button_9 = Button(button_frame, text='9', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                  height=1, command=lambda: press(9))
addition_button = Button(button_frame, text='+', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                         width=4, height=1, command=lambda: press('+'))
substraction_button = Button(button_frame, text='-', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                             width=4, height=1, command=lambda: press('-'))
multiplication_button = Button(button_frame, text='*', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                               width=4, height=1, command=lambda: press('*'))
division_button = Button(button_frame, text='/', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                         width=4, height=1, command=lambda: press('/'))
power_button = Button(button_frame, text='^', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=lambda: press('^'))
square_root_button = Button(button_frame, text='sqrt', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC',
                            width=4, height=1, command=lambda: press('sqrt'))
clear_button = Button(button_frame, text='C', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=clear())
equal_button = Button(button_frame, text='=', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=press_equal())
previous_expression_button_1 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_2 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_3 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_4 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_5 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_6 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_7 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_8 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_9 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())
previous_expression_button_10 = Button(button_frame, text='->', font=('arial', 20), relief='ridge', borderwidth=5, bg='#0000CC', width=4,
                      height=1, command=previous_equasion())

#Tutaj rozmieszczam przyciski oraz pola
expression_field.grid(row=0, column=0, columnspan=5, ipadx=29, ipady=13,pady=0)

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
clear_button.grid(row=3, column=4)

button_0.grid(row=4, column=0)
imaginary_unit_button.grid(row=4, column=1)
decimal_point_button.grid(row=4, column=2)
division_button.grid(row=4, column=3)
equal_button.grid(row=4, column=4)

previous_expression_button_1.grid(row=5, column=0)
previous_expression_button_2.grid(row=6, column=0)
previous_expression_button_3.grid(row=7, column=0)
previous_expression_button_4.grid(row=8, column=0)
previous_expression_button_5.grid(row=9, column=0)
previous_expression_button_6.grid(row=10, column=0)
previous_expression_button_7.grid(row=11, column=0)
previous_expression_button_8.grid(row=12, column=0)
previous_expression_button_9.grid(row=13, column=0)
previous_expression_button_10.grid(row=14, column=0)

previous_expression_field_1.grid(row=5, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_2.grid(row=6, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_3.grid(row=7, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_4.grid(row=8, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_5.grid(row=9, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_6.grid(row=10, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_7.grid(row=11, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_8.grid(row=12, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_9.grid(row=13, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)
previous_expression_field_10.grid(row=14, column=1, columnspan=4, ipadx=4, ipady=9,pady=0)

#Uruchomienie kalkulatora
gui.mainloop()


