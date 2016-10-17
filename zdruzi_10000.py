# coding: utf-8
import os

info = range(157, 270)
range = 10000
start, end = 0, 14


for dt in range(start, end):
    nova_d = 'dtisoc/dtisoc{:04}.txt'.format(dt)
    with open(nova_d, 'w') as new:
        text = ''
        for n in range(range):
            id = dt * ran + n
            dat = origin + 'data1/{:07}'.format(id)
            if os.path.isfile(dat):
                with open(dat, 'r') as d:
                    for i, line in enumerate(d):
                        if i in info:
                            text += line
        new.write(text)
    print('{}% opravljeno ...'.format((dt - start + 1)*100/(end - start)))
