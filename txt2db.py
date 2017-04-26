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
            Qinhuangdao.objects.create(datetime=now_time, \
                                      velocity1=int(now_line[4]), direction1=float(now_line[6]), \
                                      velocity2=int(now_line[7]), direction2=float(now_line[9]), \
                                      velocity3=int(now_line[10]), direction3=float(now_line[12]), \
                                      velocity4=int(now_line[13]), direction4=float(now_line[15]), \
                                      velocity5=int(now_line[16]), direction5=float(now_line[18]), \
                                      velocity6=int(now_line[19]), direction6=float(now_line[21]), \
                                      velocity7=int(now_line[22]), direction7=float(now_line[24]), \
                                      velocity8=int(now_line[25]), direction8=float(now_line[27]), \
                                      velocity9=int(now_line[28]), direction9=float(now_line[30]), \
                                      velocity10=int(now_line[31]), direction10=float(now_line[33]),
                                      velocity11=int(now_line[34]), direction11=float(now_line[36]), \
                                      velocity12=int(now_line[37]), direction12=float(now_line[39]), \
                                      velocity13=int(now_line[40]), direction13=float(now_line[42]), \
                                      velocity14=int(now_line[43]), direction14=float(now_line[45]), \
                                      velocity15=int(now_line[46]), direction15=float(now_line[48]),)


if __name__ == '__main__':
    main()
    print('done!')
