# Project1-Foofle-DB
# Ghazal Sadeghian-9533054


from tabulate import tabulate
import mysql.connector


def getProcedures():
    c = input('Do you want to continue? Enter y/n   ')
    if c == 'y':
        print("Select from these procedures:")
        print('SignUp')
        print('Login')
        print('Logout')
        print('deleteAccount')
        print('getNotifications')
        print('sendEmail')
        print('getInbox')
        print('getSentEmails')
        print('openEmail')
        print('deleteEmail')
        print('getAccountInfo')
        print('editProfile')
        print('getOthersProfile')
        print('blockAccount')
        print('permitAccount')
        req = input()
        return req
    else:
        return "finish"


hostname = 'localhost'
username = 'root'
password = ''
database = 'Foofle'
cnn = mysql.connector.connect(user=username, password=password, database=database, host=hostname)
cursor = cnn.cursor()
req = getProcedures()
while (req != "finish"):

    if (req == 'SignUp'):

        usern = input("username:  ")
        passw = input("password:  ")
        phone = input("phone:  ")
        addr = input("address:  ")
        fn = input("firstname:  ")
        sn = input("surname:  ")
        mob = input("mobile:  ")
        bd = input("birthDate:  ")
        alias = input("alias:  ")
        ap = input("accessPermission:  ")
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
                print(tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'Login'):
        usern = input("username:  ")
        passw = input("password:  ")
        try:
            args = (usern, passw)
            cursor.callproc('Login', args=args)
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'Logout'):

        try:
            cursor.callproc('Logout')
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'deleteAccount'):

        try:
            cursor.callproc('deleteAccount')
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()


    elif (req == 'getNotifications'):
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
            print(tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'getInbox'):
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
            print(tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        cont = input("Do you want to get older emails?[y/n]: ")
        if (cont == "y"):
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
                print(tabulate(table, headers=header))

                cnn.commit()
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))

        req = getProcedures()


    elif (req == 'getSentEmails'):
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
            print(tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        cont = input("Do you want to get older emails?[y/n]: ")
        if (cont == "y"):
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
                print(tabulate(table, headers=header))

                cnn.commit()
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))

        req = getProcedures()


    elif (req == 'openEmail'):
        date = input("Date:  ")
        subject = input("Subject:  ")
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
            print(tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'deleteEmail'):

        subject = input("Subject:  ")
        date = input("Date:  ")
        try:
            args = (subject, date)
            cursor.callproc("deleteEmail", args=args)
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'sendEmail'):

        subject = input("subject:  ")
        content = input("content:  ")
        r1 = input("receiver1:  ")
        r2 = input("receiver2:  ")
        r3 = input("receiver3:  ")
        c1 = input("cc1:  ")
        c2 = input("cc2:  ")
        c3 = input("cc3:  ")

        try:
            args = (subject, content, r1, r2, r3, c1, c2, c3)
            cursor.callproc('sendEmail', args=args)
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'editProfile'):

        field = input("Field:  ")
        newV = input("new value:  ")
        try:
            args = (field, newV)
            cursor.callproc("editProfile", args=args)
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'getAccountInfo'):
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
            print(tabulate(table, headers=header))

            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()
    elif (req == 'getOthersProfile'):
        table = []
        fu = input("Username:  ")
        try:
            args = (fu, (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'), (0, 'CHAR'))
            result_args = cursor.callproc("getOthersProfile", args=args)
            for i in range(len(result_args)):
                table.append(result_args[i])

            print(tabulate([table],
                           headers=['username', 'address', 'firstname', 'surname', 'alais', 'mobile', 'birthDate']))
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()


    elif (req == 'blockAccount'):

        bu = input("username:  ")

        try:
            args = (bu,)
            cursor.callproc("blockUser", args=args)
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()

    elif (req == 'permitAccount'):

        bu = input("username:  ")

        try:
            args = (bu,)
            cursor.callproc("permitUser", args=args)
            cnn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        req = getProcedures()






    else:
        req = getProcedures()

cursor.close()
cnn.close()
