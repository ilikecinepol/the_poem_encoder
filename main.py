import time as tm
import poem as p
import random

import os

def file_settings():
    # Получение unix-времени и времени в формате гггг-мм-дд чч:мм:сс
    unix_time = int(tm.time())
    #print(unix_time)
    str_date = tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(unix_time))
    # print(type(unix_time))
    #print(str_date)
    # Получение времени в формате гггг-мм-дд чч:мм:сс из unix
    t = tm.strptime(str_date, '%Y-%m-%d %H:%M:%S')
    # print(int(tm.mktime(t)))
    key_list = []
    key = "".join(str(unix_time))
    key = key * 10

    # Удалит существующую информацию в result.txt и запишет "Hello".
    my_file = open("result.txt", 'w')
    my_file.write('\n')
    my_file.write(f''' Сообщение отправлено: {str_date}''')
    my_file.close()

if __name__ == '__main__':
    os.remove('result.txt')
    file_settings()

    from interface import *
    app = QtWidgets.QApplication(sys.argv)
    Coding = QtWidgets.QMainWindow()
    ui = Ui_Coding()
    ui.setupUi(Coding)
    print(fname, reference_name)
    Coding.show()
    sys.exit(app.exec_())


