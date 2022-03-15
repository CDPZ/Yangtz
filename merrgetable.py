# -*- coding: utf-8 -*-

import os

def hebing(year):
    root = "E:/final/out/out_10km/"+str(year)
    paths = []

    for j in range(100):
        path = root + "/fragout"+ str(j) +".land"
        if os.path.isfile(path):
            paths.append(path)
        else:
            break



    for land in paths:
        fr = open(land,'r').read()
        with open('E:/final/out/CSV/' + str(year) + '.csv', 'a') as f:
            f.write(fr)
    print(u'合并完毕！')


if __name__ == '__main__':
    years = [2000,2010,2020]
    for year in years:
        hebing(year)

