# Project1-Foofle-DB- GUI Version
# Ghazal Sadeghian-9533054


from tabulate import tabulate
import mysql.connector
import tkinter

########################################################################################################################
# Settings

hostname = 'localhost'
username = 'root'
password = ''
database = 'Foofle'
cnn = mysql.connector.connect(user=username, password=password, database=database, host=hostname)
cursor = cnn.cursor()

HEIGHT = 900
WIDTH = 1500


########################################################################################################################
# Calling Proper Procedure

def getQuery(req):
    if (req == 'SignUp'):
        label.delete('1.0', tkinter.END)

        mframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        mframe.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.4, anchor='n')

        frame1 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='username:  ', font=5, bg=frame1.cget('bg'))
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)

        label2 = tkinter.Label(frame1, text='       password:  ', font=5, bg=frame1.cget('bg'))
        label2.grid(row=1, column=3)

        entry2 = tkinter.Entry(frame1, font=10)
        entry2.grid(row=1, column=4)

        frame3 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame3.grid(row=2, column=1)

        label3 = tkinter.Label(frame3, text='phone: ', font=5, bg=frame3.cget('bg'))
        label3.grid(row=1, column=1)

        entry3 = tkinter.Entry(frame3, font=10)
        entry3.grid(row=1, column=2)

        label4 = tkinter.Label(frame3, text='       address:  ', font=5, bg=frame3.cget('bg'))
        label4.grid(row=1, column=3)

        entry4 = tkinter.Entry(frame3, font=10)
        entry4.grid(row=1, column=4)

        frame5 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame5.grid(row=3, column=1)

        label5 = tkinter.Label(frame5, text='firstname:  ', font=5, bg=frame5.cget('bg'))
        label5.grid(row=1, column=1)

        entry5 = tkinter.Entry(frame5, font=10)
        entry5.grid(row=1, column=2)

        label6 = tkinter.Label(frame5, text='       surname:  ', font=5, bg=frame5.cget('bg'))
        label6.grid(row=1, column=3)

        entry6 = tkinter.Entry(frame5, font=10)
        entry6.grid(row=1, column=4)

        frame7 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame7.grid(row=4, column=1)

        label7 = tkinter.Label(frame7, text='mobile:  ', font=5, bg=frame7.cget('bg'))
        label7.grid(row=1, column=1)

        entry7 = tkinter.Entry(frame7, font=10)
        entry7.grid(row=1, column=2)

        label8 = tkinter.Label(frame7, text='       birthDate:  ', font=5, bg=frame7.cget('bg'))
        label8.grid(row=1, column=3)

        entry8 = tkinter.Entry(frame7, font=10)
        entry8.grid(row=1, column=4)

        frame9 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame9.grid(row=5, column=1)

        label9 = tkinter.Label(frame9, text='alias: ', font=5, bg=frame9.cget('bg'))
        label9.grid(row=1, column=1)

        entry9 = tkinter.Entry(frame9, font=10)
        entry9.grid(row=1, column=2)

        label10 = tkinter.Label(frame9, text='      accessPermission:  ', font=5, bg=frame9.cget('bg'))
        label10.grid(row=1, column=3)

        entry10 = tkinter.Entry(frame9, font=10)
        entry10.grid(row=1, column=4)

        frame11 = tkinter.Frame(mframe, bg='#464545', bd=5)
        frame11.grid(row=6, column=1)
        b = tkinter.Button(frame11, text="Enter", font=5, highlightbackground='#464545',
                           command=lambda: signup(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(),
                                                  entry6.get(), entry7.get(), entry8.get(), entry9.get(),
                                                  entry10.get()))
        b.grid(row=1, column=1)

        def signup(usern, passw, phone, addr, fn, sn, mob, bd, alias, ap):
            try:
                args = (usern, passw, phone, addr, fn, sn, mob, bd, alias, ap)
                cursor.callproc('SignUp', args=args)
                if any(cursor.stored_results()):
                    for result in cursor.stored_results():
                        table = []
                        columnsProperties = (result.description)
                        header = ([column[0] for column in columnsProperties])
                        row = result.fetchone()
                        while row is not None:
                            rowL = list(row)
                            table.append(rowL)
                            row = result.fetchone()
                    label['text'] = tabulate(table, headers=header)

                cnn.commit()

            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            mframe.destroy()




    elif (req == 'Login'):
        label.delete('1.0', tkinter.END)

        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='username:  ', font=10)
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)
        frame2 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame2.grid(row=2, column=1)

        label2 = tkinter.Label(frame2, text='password:  ', font=10)
        label2.grid(row=1, column=1)

        entry2 = tkinter.Entry(frame2, font=10)
        entry2.grid(row=1, column=2)
        frame3 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame3.grid(row=3, column=1)
        b = tkinter.Button(frame3, text="Enter", font=40, highlightbackground='#464545',
                           command=lambda: login(entry1.get(), entry2.get()))
        b.grid(row=1, column=1)

        def login(usern, passw):
            try:
                args = (usern, passw)
                cursor.callproc('Login', args=args)
                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()



    elif (req == 'Logout'):
        label.delete('1.0', tkinter.END)

        try:
            cursor.callproc('Logout')
            cnn.commit()
        except mysql.connector.Error as err:
            label.insert(1.0, "Something went wrong: {}".format(err))


    elif (req == 'deleteAccount'):

        try:
            cursor.callproc('deleteAccount')
            cnn.commit()
        except mysql.connector.Error as err:
            label.insert(1.0, "Something went wrong: {}".format(err))



    elif (req == 'getNotifications'):
        label.delete('1.0', tkinter.END)
        label.delete('1.0', tkinter.END)

        try:
            cursor.callproc("getNotifications")

            for result in cursor.stored_results():
                table = []
                columnsProperties = (result.description)
                header = ([column[0] for column in columnsProperties])
                # print(header)
                row = result.fetchone()
                while row is not None:
                    rowL = list(row)
                    table.append(rowL)
                    row = result.fetchone()
            # print(table)
            label.insert(1.0, tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            label.insert(1.0, "Something went wrong: {}".format(err))


    elif (req == 'getInbox'):
        label.delete('1.0', tkinter.END)
        try:
            cursor.callproc("getInbox")

            for result in cursor.stored_results():
                table = []
                columnsProperties = (result.description)
                header = ([column[0] for column in columnsProperties])
                # print(header)
                row = result.fetchone()
                while row is not None:
                    rowL = list(row)
                    table.append(rowL)
                    row = result.fetchone()
            # print(table)
            label.insert(1.0, tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            label.insert(1.0, "Something went wrong: {}".format(err))

        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)
        b = tkinter.Button(frame1, text="Next Page", font=40, highlightbackground='#464545',
                           command=lambda: inboxNext())
        b.grid(row=1, column=1)

        def inboxNext():
            label.delete('1.0', tkinter.END)
            try:
                cursor.callproc("getInboxPage2")

                for result in cursor.stored_results():
                    table = []
                    columnsProperties = (result.description)
                    header = ([column[0] for column in columnsProperties])
                    # print(header)
                    row = result.fetchone()
                    while row is not None:
                        rowL = list(row)
                        table.append(rowL)
                        row = result.fetchone()
                # print(table)
                label.insert(1.0, tabulate(table, headers=header))

                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()




    elif (req == 'getSentEmails'):
        label.delete('1.0', tkinter.END)
        try:
            cursor.callproc("getSentEmails")

            for result in cursor.stored_results():
                table = []
                columnsProperties = (result.description)
                header = ([column[0] for column in columnsProperties])
                # print(header)
                row = result.fetchone()
                while row is not None:
                    rowL = list(row)
                    table.append(rowL)
                    row = result.fetchone()
            # print(table)
            label.insert(1.0, tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            label.insert(1.0, "Something went wrong: {}".format(err))
        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)
        b = tkinter.Button(frame1, text="Next Page", font=40, highlightbackground='#464545',
                           command=lambda: sentNext())
        b.grid(row=1, column=1)

        def sentNext():
            label.delete('1.0', tkinter.END)
            try:
                cursor.callproc("getSentEmailsPage2")

                for result in cursor.stored_results():
                    table = []
                    columnsProperties = (result.description)
                    header = ([column[0] for column in columnsProperties])
                    # print(header)
                    row = result.fetchone()
                    while row is not None:
                        rowL = list(row)
                        table.append(rowL)
                        row = result.fetchone()
                # print(table)
                label.insert(1.0, tabulate(table, headers=header))

                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()




    elif (req == 'openEmail'):
        label.delete('1.0', tkinter.END)

        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='Date:  ', font=10)
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)
        frame2 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame2.grid(row=2, column=1)

        label2 = tkinter.Label(frame2, text='Subject:   ', font=10)
        label2.grid(row=1, column=1)

        entry2 = tkinter.Entry(frame2, font=10)
        entry2.grid(row=1, column=2)
        frame3 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame3.grid(row=3, column=1)
        b = tkinter.Button(frame3, text="Enter", font=40, highlightbackground='#464545',
                           command=lambda: open(entry1.get(), entry2.get()))
        b.grid(row=1, column=1)

        def open(date, subject):
            try:
                args = (date, subject)
                cursor.callproc("openEmail", args=args)

                for result in cursor.stored_results():
                    table = []
                    columnsProperties = (result.description)
                    header = ([column[0] for column in columnsProperties])
                    # print(header)
                    row = result.fetchone()
                    while row is not None:
                        rowL = list(row)
                        table.append(rowL)
                        row = result.fetchone()
                # print(table)
                label.insert(1.0, tabulate(table, headers=header))

                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()



    elif (req == 'deleteEmail'):
        label.delete('1.0', tkinter.END)

        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='Date:  ', font=10)
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)
        frame2 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame2.grid(row=2, column=1)

        label2 = tkinter.Label(frame2, text='Subject:   ', font=10)
        label2.grid(row=1, column=1)

        entry2 = tkinter.Entry(frame2, font=10)
        entry2.grid(row=1, column=2)
        frame3 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame3.grid(row=3, column=1)
        b = tkinter.Button(frame3, text="Enter", font=40, highlightbackground='#464545',
                           command=lambda: deleteE(entry2.get(), entry1.get()))
        b.grid(row=1, column=1)

        def deleteE(subject, date):
            try:
                args = (subject, date)
                cursor.callproc("deleteEmail", args=args)
                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()


    elif (req == 'sendEmail'):
        label.delete('1.0', tkinter.END)

        mframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        mframe.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.4, anchor='n')

        frame1 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='subject:  ', font=5, bg=frame1.cget('bg'))
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)

        frame3 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame3.grid(row=2, column=1)

        label3 = tkinter.Label(frame3, text='content: ', font=5, bg=frame3.cget('bg'))
        label3.grid(row=1, column=1)

        entry3 = tkinter.Entry(frame3, font=10)
        entry3.grid(row=1, column=2)

        frame5 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame5.grid(row=3, column=1)

        label5 = tkinter.Label(frame5, text='receiver1:  ', font=5, bg=frame5.cget('bg'))
        label5.grid(row=1, column=1)

        entry5 = tkinter.Entry(frame5, font=10)
        entry5.grid(row=1, column=2)

        label6 = tkinter.Label(frame5, text='       receiver2:  ', font=5, bg=frame5.cget('bg'))
        label6.grid(row=1, column=3)

        entry6 = tkinter.Entry(frame5, font=10)
        entry6.grid(row=1, column=4)

        frame7 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame7.grid(row=4, column=1)

        label7 = tkinter.Label(frame7, text='receiver3:  ', font=5, bg=frame7.cget('bg'))
        label7.grid(row=1, column=1)

        entry7 = tkinter.Entry(frame7, font=10)
        entry7.grid(row=1, column=2)

        label8 = tkinter.Label(frame7, text='       cc1:  ', font=5, bg=frame7.cget('bg'))
        label8.grid(row=1, column=3)

        entry8 = tkinter.Entry(frame7, font=10)
        entry8.grid(row=1, column=4)

        frame9 = tkinter.Frame(mframe, bg='#eeffe6', bd=5)
        frame9.grid(row=5, column=1)

        label9 = tkinter.Label(frame9, text='cc2: ', font=5, bg=frame9.cget('bg'))
        label9.grid(row=1, column=1)

        entry9 = tkinter.Entry(frame9, font=10)
        entry9.grid(row=1, column=2)

        label10 = tkinter.Label(frame9, text='      cc3:  ', font=5, bg=frame9.cget('bg'))
        label10.grid(row=1, column=3)

        entry10 = tkinter.Entry(frame9, font=10)
        entry10.grid(row=1, column=4)

        frame11 = tkinter.Frame(mframe, bg='#464545', bd=5)
        frame11.grid(row=6, column=1)
        b = tkinter.Button(frame11, text="Enter", font=5, highlightbackground='#464545',
                           command=lambda: sendE(entry1.get(), entry3.get(), entry5.get(),
                                                 entry6.get(), entry7.get(), entry8.get(), entry9.get(),
                                                 entry10.get()))
        b.grid(row=1, column=1)

        def sendE(subject, content, r1, r2, r3, c1, c2, c3):

            try:
                args = (subject, content, r1, r2, r3, c1, c2, c3)
                cursor.callproc('sendEmail', args=args)
                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            mframe.destroy()

    elif (req == 'editProfile'):
        label.delete('1.0', tkinter.END)

        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='Field:  ', font=10)
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)
        frame2 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame2.grid(row=2, column=1)

        label2 = tkinter.Label(frame2, text='new value:   ', font=10)
        label2.grid(row=1, column=1)

        entry2 = tkinter.Entry(frame2, font=10)
        entry2.grid(row=1, column=2)
        frame3 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame3.grid(row=3, column=1)
        b = tkinter.Button(frame3, text="Enter", font=40, highlightbackground='#464545',
                           command=lambda: edit(entry1.get(), entry2.get()))
        b.grid(row=1, column=1)

        def edit(field, newV):
            try:
                args = (field, newV)
                cursor.callproc("editProfile", args=args)
                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()


    elif (req == 'getAccountInfo'):
        label.delete('1.0', tkinter.END)
        try:
            cursor.callproc("getAccountInfo")

            for result in cursor.stored_results():
                table = []
                columnsProperties = (result.description)
                header = ([column[0] for column in columnsProperties])
                # print(header)
                row = result.fetchone()
                while row is not None:
                    rowL = list(row)
                    table.append(rowL)
                    row = result.fetchone()
            # print(table)
            label.insert(1.0, tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            label.insert(1.0, "Something went wrong: {}".format(err))

    elif (req == 'getOthersProfile'):
        label.delete('1.0', tkinter.END)
        table = []

        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='Username:  ', font=10)
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)

        frame3 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame3.grid(row=2, column=1)
        b = tkinter.Button(frame3, text="Enter", font=40, highlightbackground='#464545',
                           command=lambda: getfu(entry1.get()))
        b.grid(row=1, column=1)

        def getfu(fu):
            try:
                args = (fu, (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'))
                result_args = cursor.callproc("getOthersProfile", args=args)
                for i in range(len(result_args)):
                    table.append(result_args[i])

                label.insert(1.0, tabulate([table],
                                           headers=['username', 'address', 'firstname', 'surname', 'alais', 'mobile',
                                                    'birthDate']))
                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()



    elif (req == 'blockAccount'):
        label.delete('1.0', tkinter.END)
        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='Username:  ', font=10)
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)

        frame3 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame3.grid(row=2, column=1)
        b = tkinter.Button(frame3, text="Enter", font=40, highlightbackground='#464545',
                           command=lambda: blockU(entry1.get()))
        b.grid(row=1, column=1)

        def blockU(bu):
            try:
                args = (bu,)
                cursor.callproc("blockUser", args=args)
                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()


    elif (req == 'permitAccount'):
        label.delete('1.0', tkinter.END)

        nframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
        nframe.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.2, anchor='n')

        frame1 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame1.grid(row=1, column=1)

        label1 = tkinter.Label(frame1, text='Username:  ', font=10)
        label1.grid(row=1, column=1)

        entry1 = tkinter.Entry(frame1, font=10)
        entry1.grid(row=1, column=2)

        frame3 = tkinter.Frame(nframe, bg='#464545', bd=5)
        frame3.grid(row=2, column=1)
        b = tkinter.Button(frame3, text="Enter", font=40, highlightbackground='#464545',
                           command=lambda: permitU(entry1.get()))
        b.grid(row=1, column=1)

        def permitU(bu):
            try:
                args = (bu,)
                cursor.callproc("permitUser", args=args)
                cnn.commit()
            except mysql.connector.Error as err:
                label.insert(1.0, "Something went wrong: {}".format(err))
            nframe.destroy()

    else:
        label.delete('1.0', tkinter.END)


########################################################################################################################
# Creating GUI

root = tkinter.Tk()
root.title('Foofle(Ghazal Sadeghian-9533054)')
canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH, bg='#eeffe6')
canvas.pack()

# background_image = tkinter.PhotoImage(file='landscape.png')
# background_label = tkinter.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame = tkinter.Frame(root, bg='#464545', bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.05, anchor='n')

entry = tkinter.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tkinter.Button(frame, text="Get Query", font=40, highlightbackground='#464545',
                        command=lambda: getQuery(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

mframe = tkinter.Frame(root, bg='#eeffe6', bd=5)
mframe.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.4, anchor='n')
orglabel1 = tkinter.Label(mframe, bg='#eeffe6', text='Select from these procedures:  ', fg='#373c3d',
                          font=('Helvetica', 20, 'bold'))
orglabel1.grid(row=1, column=1)
orglabel2 = tkinter.Text(mframe, bg='#eeffe6', height=1, borderwidth=0, fg='#373c3d', font=('Helvetica', 20, 'bold'))
orglabel2.insert(1.0, 'SignUp, Login, Logout, deleteAccount, getNotifications, sendEmail, getInbox, getSentEmails')
orglabel2.configure(state="disabled")


def focusText(event):
    orglabel2.config(state='normal')
    orglabel2.focus()
    orglabel2.config(state='disabled')


orglabel2.bind('<Button-1>', focusText)
orglabel2.grid(row=2, column=1)
orglabel3 = tkinter.Text(mframe, bg='#eeffe6', height=1, borderwidth=0, fg='#373c3d', font=('Helvetica', 20, 'bold'))
orglabel3.insert(1.0,
                 'openEmail, deleteEmail, getAccountInfo, editProfile, getOthersProfile, blockAccount, permitAccount')
orglabel3.configure(state="disabled")


def focusText2(event):
    orglabel3.config(state='normal')
    orglabel3.focus()
    orglabel3.config(state='disabled')


orglabel3.bind('<Button-1>', focusText2)
orglabel3.grid(row=3, column=1)

lower_frame = tkinter.Frame(root, bg='#464545', bd=10)
lower_frame.place(relx=0.5, rely=0.55, relwidth=0.95, relheight=0.4, anchor='n')

label = tkinter.Text(lower_frame, height=1, borderwidth=0)


def focusText3(event):
    label.config(state='disabled')


label.bind('<Button-1>', focusText3)
label.place(relwidth=1, relheight=1)

root.mainloop()
