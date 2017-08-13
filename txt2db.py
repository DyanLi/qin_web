#!/usr/bin/env python3

from datetime import datetime

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qin_web.settings")

import django
django.setup()

def main():
    print("main runing")
    from qinhuangdao.models import Qinhuangdao
    print('import models')
    with open("1216a.txt", 'r', encoding='utf-8') as file:
        for line in file.readlines():
            now_line = line.split(',')
            now_time = datetime.strptime(now_line[2] + ' ' + now_line[3], '%Y-%m-%d %H:%M:%S')
            Qinhuangdao.objects.create(datetime=now_time, \
                                      velocity1=int(now_line[4]), direction1=round(float(now_line[6]),1), \
                                      velocity2=int(now_line[7]), direction2=round(float(now_line[9]),1), \
                                      velocity3=int(now_line[10]), direction3=round(float(now_line[12]),1), \
                                      velocity4=int(now_line[13]), direction4=round(float(now_line[15]),1), \
                                      velocity5=int(now_line[16]), direction5=round(float(now_line[18]),1), \
                                      velocity6=int(now_line[19]), direction6=round(float(now_line[21]),1), \
                                      velocity7=int(now_line[22]), direction7=round(float(now_line[24]),1), \
                                      velocity8=int(now_line[25]), direction8=round(float(now_line[27]),1), \
                                      velocity9=int(now_line[28]), direction9=round(float(now_line[30]),1), \
                                      velocity10=int(now_line[31]), direction10=round(float(now_line[33]),1),
                                      velocity11=int(now_line[34]), direction11=round(float(now_line[36]),1), \
                                      velocity12=int(now_line[37]), direction12=round(float(now_line[39]),1), \
                                      velocity13=int(now_line[40]), direction13=round(float(now_line[42]),1), \
                                      velocity14=int(now_line[43]), direction14=round(float(now_line[45]),1), \
                                      velocity15=int(now_line[46]), direction15=round(float(now_line[48]),1),)


if __name__ == '__main__':
    main()
    print('done!')
