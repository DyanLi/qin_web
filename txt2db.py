#!/usr/bin/env python3

from datetime import datetime

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WYXweb.settings")

import django
django.setup()

def main():
    from qinhuangdao.models import Qinhuangdao
    with open("1216a.txt", 'r') as file:
        for line in file.readlines():
            now_line = line.split(',')
            now_time = datetime.strptime(now_line[2] + ' ' + now_line[3], '%Y-%m-%d %H:%M:%S')
            Qinhuangdao.objects.create(datetime=now_time, direction1=int(now_line[4]), velocity1=float(now_line[6]), \
                                      direction2=int(now_line[7]), velocity2=float(now_line[9]), \
                                      direction3=int(now_line[10]), velocity3=float(now_line[12]), \
                                      direction4=int(now_line[13]), velocity4=float(now_line[15]), \
                                      direction5=int(now_line[16]), velocity5=float(now_line[18]), \
                                      direction6=int(now_line[19]), velocity6=float(now_line[21]), \
                                      direction7=int(now_line[22]), velocity7=float(now_line[24]), \
                                      direction8=int(now_line[25]), velocity8=float(now_line[27]), \
                                      direction9=int(now_line[28]), velocity9=float(now_line[30]), \
                                      direction10=int(now_line[31]), velocity10=float(now_line[33]),
                                      direction11=int(now_line[34]), velocity11=float(now_line[36]), \
                                      direction12=int(now_line[37]), velocity12=float(now_line[39]), \
                                      direction13=int(now_line[40]), velocity13=float(now_line[42]), \
                                      direction14=int(now_line[43]), velocity14=float(now_line[45]), \
                                      direction15=int(now_line[46]), velocity15=float(now_line[48]),)


if __name__ == '__main__':
    main()
    print('done!')
