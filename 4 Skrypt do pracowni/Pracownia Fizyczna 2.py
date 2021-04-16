#--------------------------------------------------------------------------------------
# Skrypt to liczenia rzeczy na pracownie krok po kroku żeby moć to potem przeklejać do worda xd
# Wyniki wywalane sa do pliku .txt, przyklady w repozytorium
# Skrypt napisałem dla siebie nie jako projekt do portfolio
# więc zwykły uzytkownik szybciej ogarnie obsługe koparki
# - zobaczyc kod, nie zabierac sie za praktykowanie xd


#########################################################################################
#                               ####### RÓWNANIE ######
#
# 1. Wpisz równanie. Np. f(x,y,z)=x+y**2+z/2 - Wszystkie zmienne musza byc podane w f(...) !
# 2. Kliknij dodaj równanie
# 3. Wczytaj dane z excel - wybierz plik z exela z danymi ( tylko same liczby, każda zmienna w innej kolumnie )
# 4. Wpisz zmienne : Np. "x,y,z" Program zczytuje z kazdej kolumny odpowiednią zmienną
# 5. Kliknij dodaj zmienną
# 6. Kliknij generuj i wybierz miejsce gdzie zapisze sie plik z danymi
##########################################################################################
#                               ###### Niepewność (17 ) ######
#
# 1. Wpisujesz wartość średnią
# 2. Kliknij dodaj
# 3. Wczytaj dane - Dane muszą być w pierwszej kolumnie w exelu!
# 4. Generuj i wybierz miejsce zapisu
###########################################################################################
#                              #### Niepewnosc z pochodna (15) ###
#
#   1. Wpisz funkcje dokladnie tak jak przy rownaniu i kliknij dodaj
#   2. Wpisz dane w takiej kolejnosci jak w funkcji f(x,y,z) -> x=2,y=5,z=12 i dodaj
#   3. UWAGA !
#   4. Tylko po wpisanych zmiennych zostanie policzona pochodna
#   5. Generuj i wybierz miejsce zapisu
##############################################################################################
#                            ######## Średnia z danych #####
#
#   1. Zaimportuj dane z exela (dane muszą byc w pierwszej kolumnie )
#
#
################################################################################
from tkinter import *
from tkinter import filedialog
import xlrd
from sympy import *
import math
from openpyxl import Workbook

# Main GUI

MainRoot = Tk()
MainRoot.title('Pracownia fizyczna')


def avclick():
    path = []

    # **Funkcje ** #
    def generate():
        final = []

        inputWorkBook = xlrd.open_workbook(path[0])
        inputWorksheet = inputWorkBook.sheet_by_index(0)

        clear_data = []
        for data in range(inputWorksheet.nrows):
            x = float(simplify(inputWorksheet.cell_value(data, 0)))
            clear_data.append(N(x, 5))

        n = len(clear_data)
        # FIRST
        first = ''
        for element in clear_data:
            if element == clear_data[-1]:
                first += str(element)
            else:
                first += str(element) + '+'
        first += '/' + str(n)
        final.append(first)
        # SCND
        scnd = str(sum(clear_data))
        scnd += '/' + str(n)
        final.append(scnd)
        # THRD
        thrd = str(sum(clear_data) / n)
        final.append(thrd)

        ectroot = Tk()
        ectroot.filename = filedialog.askdirectory(title='Wybierz folder zapisu')
        file_path = ectroot.filename + '/srednia z danych.txt'
        ectroot.destroy()

        file = open(file_path, 'w+')
        for element in final:
            file.write('Następny krok: \n')
            file.write('\n')
            file.write(element + '\n')
            file.write('\n')
        file.close()

    def data():
        dataroot = Tk()
        dataroot.filename = filedialog.askopenfile(initialdir='/Pulpit', title='Wybierz Exela z danymi')
        path.append(dataroot.filename.name)
        dataroot.destroy()

    ################
    # Main
    avroot = Tk()
    avroot.title('Średnia z danych')

    # Buttons
    data = Button(avroot, text='Wczytaj dane', padx=40, pady=20, command=data)
    gen = Button(avroot, text='Generuj', padx=40, pady=20, command=generate)
    close = Button(avroot, text='Zamknij', padx=40, pady=20, command=avroot.destroy)
    # Pos Buttons
    data.grid(row=0, column=0)
    gen.grid(row=1, column=0)
    close.grid(row=3, column=0)


def np1click():
    global averageValue
    averageValue = 0

    path = []

    def data():
        dataroot = Tk()
        dataroot.filename = filedialog.askopenfile(initialdir='/Pulpit', title='Wybierz Exela z danymi')
        path.append(dataroot.filename.name)
        dataroot.destroy()

    def generate():
        final = []

        inputWorkBook = xlrd.open_workbook(path[0])
        inputWorksheet = inputWorkBook.sheet_by_index(0)

        clear_data = []
        for data in range(inputWorksheet.nrows):
            x = float(simplify(inputWorksheet.cell_value(data, 0)))
            clear_data.append(N(x, 5))

        n = len(clear_data)

        #### First ####

        first = ''

        su = []
        su2 = []
        for element in clear_data:
            el = str(element)
            av = str(averageValue)
            re = '({} - {})^2'.format(el, av)
            su.append(re)
            re2 = math.pow(element - averageValue, 2)
            su2.append(re2)

        ns = str(n)

        first += 'sqrt(('
        for element in su:
            if element == su[-1]:
                first += element
                first += ')'
            else:
                first += element
                first += '+'
        first += '/'
        first += '{} ( {} -1))'.format(ns, ns)

        final.append(first)
        # SCND

        scnd = 'sqrt('
        su3 = sum(su2)
        for element in su2:
            if element == su2[-1]:
                scnd += str(element)
            else:
                scnd += str(element)
                scnd += '+'
        ns2 = n - 1
        scnd += '/'
        scnd += '{}({}))'.format(ns, ns2)

        final.append(scnd)
        # Thrd
        ne = n * ns2
        trd = 'sqrt('
        trd += str(su3) + '/' + str(ne) + ')'

        final.append(trd)
        # four
        end = su3 / ne
        four = 'sqrt(' + str(end) + ')'

        final.append(four)

        # five

        end2 = sqrt(end)
        five = str(end2)
        final.append(five)

        # To file

        ectroot = Tk()
        ectroot.filename = filedialog.askdirectory(title='Wybierz folder zapisu')
        file_path = ectroot.filename + '/Niepewność standardowa (17).txt'
        ectroot.destroy()

        file = open(file_path, 'w+')
        for element in final:
            file.write('Następny krok: \n')
            file.write('\n')
            file.write(element + '\n')
            file.write('\n')
        file.close()

    def add():
        res = e.get()
        global averageValue
        averageValue += float(simplify(res))

    # Main

    np1root = Tk()
    np1root.title('Niepewność standardowa (17)')

    # Buttons
    labe = Label(np1root, text='Wpisz wartość średnią ')
    e = Entry(np1root, width=35, borderwidth=5)
    add = Button(np1root, text='Dodaj', padx=40, pady=20, command=add)
    data = Button(np1root, text='Wczytaj dane', padx=40, pady=20, command=data)
    gen = Button(np1root, text='Generuj', padx=40, pady=20, command=generate)
    close = Button(np1root, text='Zamknij', padx=40, pady=20, command=np1root.destroy)

    # Buttons pos
    labe.grid(row=0, column=0)
    e.grid(row=1, column=0, columnspan=1, padx=10, pady=10)
    data.grid(row=2, column=0)
    gen.grid(row=3, column=0)
    close.grid(row=4, column=0)
    add.grid(row=1, column=2)


def np2click():
    functio = []

    values = []

    uncers = []

    def addfunc():

        functio1 = fun.get()
        functio.append(functio1)

    def addval():

        ad = valen.get()
        values.append(ad)

    def adduncer():

        er = unent.get()
        uncers.append(er)

    #########################

    def generate():
        final_lines = []
        ###
        lst = []

        def genform():  # to jest to
            formula1 = functio[0]
            # symbo,equ,equsim,var,bef=
            last = []
            t = formula1
            t2 = t.split('=')
            t3 = t2[0].split('(')
            t4 = t3[1].split(')')
            t5 = t4[0].split(',')
            t6 = t4[0].replace(',', ' ')
            symbo = '''{}=symbols('{}')'''.format(t4[0], t6)
            last.append(symbo)
            equ = '''{}={}'''.format(t3[0], t2[1])
            last.append(equ)
            # exec (last[0])
            # exec (last[1])
            code = '''
                                    {}
                                    {}
                                    x=simplify({})
                                    a=str(t3[0])+'='+str(x)
                                    last.append(a)
                                    '''.format(last[0], last[1], t3[0])
            exec(code)
            w = [x for x in t5]
            last.append(w)
            last.append(t3[0])

            for e in last:
                lst.append(e)

        genform()

        ###

        def intro():
            t = 'Wzór ogólny : ''\n'
            formula = functio[0]
            t += str(formula)
            final_lines.append(t)
            # final_lines.append(formula)
            # 2
            t2 = formula + '='
            a1 = lst[2].split('=')
            t2 += a1[1]
            final_lines.append(t2)

        intro()

        def sum_pure_deriv():
            t = functio[0]
            t2 = t.split('=')
            fx = t2[0]
            # poprawka
            pop = []

            u = uncers
            u1 = u[0].split(',')
            u2 = [x.split('=') for x in u1]
            for element in u2:
                pop.append(element[0])

            todiv = []
            for element in pop:
                if element in lst[3]:
                    todiv.append(element)

            #
            # 1
            text = 'sqrt('
            for element in todiv:
                if element == todiv[-1]:
                    t2 = '(d{}/d{})^2 * u^2({}))'.format(fx, element, element)
                    text += t2
                else:
                    t2 = '(d{}/d{})^2 * u^2({}) + '.format(fx, element, element)
                    text += t2

            final_lines.append(text)
            # posredni
            tp = lst[2].split('=')
            textpos = 'sqrt('
            for element in todiv:
                if element == todiv[-1]:
                    t2 = '(d ({}) /d{})^2 * u^2({}))'.format(str(tp[1]), element, element)
                    textpos += t2
                else:
                    t2 = '(d ({}) /d{})^2 * u^2({}) + '.format(str(tp[1]), element, element)
                    textpos += t2
            final_lines.append(textpos)

            # 2
            dif1 = []
            text2 = 'sqrt('
            dif1a = []
            for element in todiv:
                code = '''
                                    {}
                                    {}
                                    r=diff({},{})
                                    dif1a.append(r)
                                    r='('+str(r)+')^2' +' * '+ '('+str(element)+')^2'
                                    dif1.append(r)                      
                                    '''.format(lst[0], lst[2], lst[-1], element)
                exec(code)

            dif1b = dif1a.copy()

            for element in dif1:
                if element == dif1[-1]:
                    t = '(' + str(element) + '))'
                    text2 += t
                else:
                    t = '(' + str(element) + ') + '
                    text2 += t

            final_lines.append(text2)

            # 3 dictionaries
            t = values
            t1 = t[0].split(',')
            t2 = [x.split('=') for x in t1]
            dictionarval = {}
            for x in t2:
                dictionarval[x[0]] = x[1]

            tu = uncers
            t1 = tu[0].split(',')
            t2 = [x.split('=') for x in t1]
            dictionaruncer = {}
            for x in t2:
                dictionaruncer[x[0]] = x[1]

            dif2 = []
            dif3s = []
            for element in dif1a:
                dif2.append(str(element))
            for element in dif2:
                el2 = element
                for letter in el2:
                    if letter in dictionarval.keys():
                        el2 = el2.replace(letter, dictionarval[letter])
                dif3s.append(el2)

            difs4 = []
            for e in dif3s:
                difs4.append(parse_expr(e))

            text3 = 'sqrt('
            n = 0
            for element1 in dif3s:
                if element1 == dif3s[-1]:
                    tt = '({})^2 * ({})^2)'.format(element1, dictionaruncer[lst[3][n]])
                    text3 += tt
                else:
                    tt = ' ({})^2 * ({})^2 +'.format(element1, dictionaruncer[lst[3][n]])
                    text3 += tt
                n += 1
            final_lines.append(text3)

            text4 = 'sqrt('
            n = 0
            for element1 in difs4:
                if element1 == difs4[-1]:
                    tt = '({})^2 * ({})^2)'.format(str(element1), dictionaruncer[lst[3][n]])
                    text4 += tt
                else:
                    tt = ' ({})^2 * ({})^2 +'.format(str(element1), dictionaruncer[lst[3][n]])
                    text4 += tt
                n += 1
            final_lines.append(text4)

            # 5
            disf5 = []
            for element in difs4:
                x = '(' + str(element) + ')' + '**2'
                disf5.append(parse_expr(x))
            u51 = []
            for e in dictionaruncer.values():
                u51.append(e)
            u5 = []
            for element in u51:
                elemen = '(' + str(element) + ')' + '**2'
                u5.append(parse_expr(elemen))

            mno = []
            text5 = 'sqrt( '
            n = 0
            for element in disf5:
                if element == disf5[-1]:
                    tx = '{}*{} )'.format(str(element), str(u5[n]))
                    text5 += tx
                    tx2 = '{}*{}'.format(str(element), str(u5[n]))
                    mno.append(tx2)
                else:
                    tx = '{}*{} +'.format(str(element), str(u5[n]))
                    text5 += tx
                    tx2 = '{}*{}'.format(str(element), str(u5[n]))
                    mno.append(tx2)
                n = 0
            final_lines.append(text5)

            # 6
            mnoe = []
            for ele in mno:
                mnoe.append(parse_expr(ele))
            t7 = ''
            text6 = 'sqrt( '
            for ele in mnoe:
                tx = str(ele) + '+'
                text6 += tx
                t7 += tx
            text6 += ')'
            final_lines.append(text6)

            # 7
            t7 = t7[:-1]
            suma = parse_expr(t7)
            text7 = 'sqrt(' + str(suma) + ')'
            final_lines.append(text7)

            # 8
            end = sqrt(suma)
            text8 = str(end)
            final_lines.append(text8)

        sum_pure_deriv()

        # To file

        ectroot = Tk()
        ectroot.filename = filedialog.askdirectory(title='Wybierz folder zapisu')
        file_path = ectroot.filename + '/Niepewność standardowa (to z pochodną) (15).txt'
        ectroot.destroy()

        file = open(file_path, 'w+')
        for element in final_lines:
            file.write('Następny krok: \n')
            file.write('\n')
            file.write(element + '\n')
            file.write('\n')
        file.close()

    # Main
    np2root = Tk()
    np2root.title('Niepewność standardowa (to z pochodną) (15)')
    # Entries
    fun = Entry(np2root, width=35, borderwidth=5)
    valen = Entry(np2root, width=35, borderwidth=5)
    unent = Entry(np2root, width=35, borderwidth=5)

    # Buttons
    func = Button(np2root, text='Dodaj funkcję', padx=40, pady=20, command=addfunc)
    val = Button(np2root, text='Dodaj dane', padx=40, pady=20, command=addval)
    uncerf = Button(np2root, text='Dodaj niepewności', padx=40, pady=20, command=adduncer)
    gen = Button(np2root, text='Generuj', padx=40, pady=20, command=generate)
    close = Button(np2root, text='Zamknij', padx=40, pady=20, command=np2root.destroy)

    # Labels
    funl = Label(np2root, text='Wpisz funkcję')
    vall = Label(np2root, text='Wpisz dane')
    uncel = Label(np2root, text='Wpisz niepewnosci')
    funl2 = Label(np2root, text='Np:f(x,y,z)=x**2+(16*z)/y')
    vall2 = Label(np2root, text='Np:x=1,y=2,z=5 ')
    uncel2 = Label(np2root, text='Np:x=0.5,y=0.1 ')
    warrior = Label(np2root, text='Zachowaj kolejność przy danych i niepewnosciach')

    # Grid
    funl.grid(row=0, column=0)
    warrior.grid(row=0, column=1)
    fun.grid(row=1, column=0, columnspan=1, padx=10, pady=10)
    func.grid(row=1, column=1)
    funl2.grid(row=1, column=2)
    vall.grid(row=2, column=0)
    valen.grid(row=3, column=0, columnspan=1, padx=10, pady=10)
    val.grid(row=3, column=1)
    vall2.grid(row=3, column=2)
    uncel.grid(row=4, column=0)
    unent.grid(row=5, column=0, columnspan=1, padx=10, pady=10)
    uncerf.grid(row=5, column=1)
    uncel2.grid(row=5, column=2)
    gen.grid(row=6, column=0)
    close.grid(row=6, column=1)


def eqclick():
    path = []

    variable = []

    equation = []

    def data():
        dataroot = Tk()
        dataroot.filename = filedialog.askopenfile(initialdir='/Pulpit', title='Wybierz Exela z danymi')
        path.append(dataroot.filename.name)
        dataroot.destroy()

    def varadd():
        variable.append(varia.get())

    def eqadd():
        equation.append(equ.get())

    def generate():

        # Equation
        lst = []

        def genform():  # to jest to
            formula1 = equation[0]

            # symbo,equ,equsim,var,bef=
            last = []
            t = formula1
            t2 = t.split('=')
            t3 = t2[0].split('(')
            t4 = t3[1].split(')')
            t5 = t4[0].split(',')
            t6 = t4[0].replace(',', ' ')
            symbo = '''{}=symbols('{}')'''.format(t4[0], t6)
            last.append(symbo)
            equ = '''{}={}'''.format(t3[0], t2[1])
            last.append(equ)
            # exec (last[0])
            # exec (last[1])
            code = '''
                                    {}
                                    {}
                                    x=simplify({})
                                    a=str(t3[0])+'='+str(x)
                                    last.append(a)
                                    '''.format(last[0], last[1], t3[0])
            exec(code)
            w = [x for x in t5]
            last.append(w)
            last.append(t3[0])

            for e in last:
                lst.append(e)

        genform()
        #######

        # Data Exel

        inputWorkBook = xlrd.open_workbook(path[0])
        inputWorksheet = inputWorkBook.sheet_by_index(0)
        clear_data = []

        for elementr in range(1, inputWorksheet.nrows):
            curr = []
            for elementc in range(inputWorksheet.ncols):
                y = simplify(inputWorksheet.cell_value(elementr, elementc))
                x = float(y)
                curr.append(x)
            clear_data.append(curr)

        # QuickSolve

        variable2 = variable[0]
        vars3 = variable2.split(',')

        solved = []
        for element in clear_data:
            code = '''

                                    structure=[]
                                    i=0
                                    for letter in vars3:
                                        tupsl=(letter,element[i])
                                        i+=1
                                        structure.append(tupsl)


                                    {}
                                    {}
                                    result={}.subs(structure)
                                    solved.append(result) 
                                    '''.format(lst[0], lst[2], lst[-1])
            exec(code)

        solvedtoexl1 = solved.copy()  # to wrzucimy do exela

        warring = lst[2].split('=')

        solvetotxt = []
        n = 0
        for data in clear_data:

            final_file1 = ''

            t1 = str(lst[1]) + '= ' + str(warring[1]) + ' = '
            final_file1 += t1

            elements_values = data
            elements_keys = vars3
            # dictionary
            nd = 0
            diction = {}
            for d in elements_values:
                diction[elements_keys[nd]] = d
                nd += 1

            # 2
            txt2 = str(warring[1])

            for letter in txt2:
                if letter in diction.keys():
                    txt2 = txt2.replace(letter, str(diction[letter]))

            final_file1 += txt2
            final_file1 += ' = '
            final_file1 += str(solved[n])
            n += 1
            solvetotxt.append(final_file1)
            ####

        # To txt file

        ectroot = Tk()
        ectroot.filename = filedialog.askdirectory(title='Wybierz folder zapisu')
        file_path = ectroot.filename + '/Równania(rozpisane).txt'
        filepa = ectroot.filename + '/Wyniki.xlsx'
        ectroot.destroy()

        file = open(file_path, 'w+')
        for element in solvetotxt:
            file.write('Następny pomiar: \n')
            file.write('\n')
            file.write(element + '\n')
            file.write('\n')
        file.close()

        # To exel file
        solvedtoexl2 = solved.copy()

        wb = Workbook()
        ws = wb.active

        stexl = []
        for element in solvedtoexl2:
            alv = []
            alv.append(float(element))
            stexl.append(alv)

        for e in stexl:
            ws.append(e)

        wb.save(filepa)

    # Main
    eqroot = Tk()
    eqroot.title('Równanie')

    # Entries
    equ = Entry(eqroot, width=35, borderwidth=5)
    varia = Entry(eqroot, width=35, borderwidth=5)

    # Buttons
    data = Button(eqroot, text='Wczytaj dane', padx=40, pady=20, command=data)
    varb = Button(eqroot, text='Dodaj zmienne', padx=40, pady=20, command=varadd)
    eqb = Button(eqroot, text='Dodaj równanie', padx=40, pady=20, command=eqadd)
    gener = Button(eqroot, text='Generuj', padx=40, pady=20, command=generate)
    cl = Button(eqroot, text='Zamknij', padx=40, pady=20, command=eqroot.destroy)

    # Labels
    eql = Label(eqroot, text='Wpisz równanie')
    varl = Label(eqroot, text='Wpisz zmienne (kolejność jak w exelu)')
    supeq = Label(eqroot, text='Np. f(x,y,z)=x+y**2+z/2')
    supvar = Label(eqroot, text='Np. x,y,z')

    # Grid
    eql.grid(row=0, column=0)
    equ.grid(row=1, column=0, columnspan=1, padx=10, pady=10)
    eqb.grid(row=1, column=1)
    supeq.grid(row=0, column=1)
    data.grid(row=2, column=0)
    varl.grid(row=3, column=0)
    varia.grid(row=4, column=0, columnspan=1, padx=10, pady=10)
    varb.grid(row=4, column=1)
    supvar.grid(row=3, column=1)
    gener.grid(row=5, column=0)
    cl.grid(row=6, column=1)


# Main Buttons

equation = Button(MainRoot, text='Równanie', padx=40, pady=20, command=eqclick)
np1 = Button(MainRoot, text='Niepewność standardowa (17)', padx=40, pady=20, command=np1click)
np2 = Button(MainRoot, text='Niepewność standardowa (to z pochodną) (15)', padx=40, pady=20, command=np2click)
average = Button(MainRoot, text='Średnia z danych', padx=40, pady=20, command=avclick)
ext = Button(MainRoot, text='Zamknij', padx=40, pady=20, command=MainRoot.destroy)

# Pos buttons
equation.grid(row=0, column=0)
np1.grid(row=0, column=1)
np2.grid(row=0, column=2)
average.grid(row=0, column=3)
ext.grid(row=1, column=3)

MainRoot.mainloop()
