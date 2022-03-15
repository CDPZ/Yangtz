#coding=utf-8
import arcpy
import os
import shutil

shppath = "D:/DaTa/Yangtz/workflow/shape_ehi/fishnet/"

if __name__ == '__main__':
    own = []
    path = []
    # for root,dirs,files in os.walk("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/1/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    #                 path.append("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/1/" + file.split('.')[0])
    # for root,dirs,files in os.walk("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/2/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    #                 path.append("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/2/" + file.split('.')[0])
    # for root,dirs,files in os.walk("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/3/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    #                 path.append("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/3/" + file.split('.')[0])
    # for root,dirs,files in os.walk("E:/final/1/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    #                 path.append("E:/final/1/" + file.split('.')[0])
    # # for root,dirs,files in os.walk("E:/final/sub_/"):
    # #     for file in files:
    # #         if(file.split('.')[-1]=="shp"):
    # #             if file.split('.')[0] not in own:
    # #                 own.append(file.split('.')[0])
    # #                 path.append("E:/final/sub_/" + file.split('.')[0])  


    # for root,dirs,files in os.walk("E:/final/3/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    #                 path.append("E:/final/3/" + file.split('.')[0])
    # for root,dirs,files in os.walk("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/split/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    #                 path.append("D:/DaTa/Yangtz/workflow/shape_ehi/sp_/split/" + file.split('.')[0])
    # for root,dirs,files in os.walk("E:/final/2/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    #                 path.append("E:/final/2/" + file.split('.')[0])
    
    # with open("D:/DaTa/Yangtz/workflow/shape_ehi/record_pa.txt", 'w') as f:
    #     for rec in path:
    #         f.write(rec)
    #         f.write("\n")
    # with open("D:/DaTa/Yangtz/workflow/shape_ehi/record_OW.txt", 'w') as f:
    #     for rec in own:
    #         f.write(rec)
    #         f.write("\n")

    own_2 = []
    path_2 = []

    own = []
    with open("D:/DaTa/Yangtz/workflow/shape_ehi/record_pa.txt") as f:
        for line in f:
            own.append(line[0:-1]) #delete \n
    count = 0
    num = 1
    for line in own:
        if num < 10:
            header = 'E:/final/sub_/Folder 0'
        else:
            header = 'E:/final/sub_/Folder '
        if count == 0:
            if not os.path.isdir(header + str(num)):
                os.mkdir(header +str(num))
        if not os.path.isfile(header + str(num) + "/" + line[line.rfind("/"):] + '.shp'):
            shutil.copy(line + '.shp', header + str(num) + "/" + line[line.rfind("/"):] + ".shp")
        try:
            if not os.path.isfile(header + str(num) + "/" + line[line.rfind("/"):] + '.shx'):
                shutil.copy(line + '.shx', header + str(num) + "/" + line[line.rfind("/"):] + ".shx")
        except IOError:
            print('no such file as ' + line + ".shx")
        try:
            if not os.path.isfile(header + str(num) + "/" + line[line.rfind("/"):] + '.dbf'):
                shutil.copy(line + '.dbf', header + str(num) + "/" + line[line.rfind("/"):] + ".dbf")
        except IOError:
            print('no such file as ' + line + ".dbf")
        try:   
            if not os.path.isfile(header + str(num) + "/" + line[line.rfind("/"):] + '.cpg'):
                shutil.copy(line + '.cpg', header + str(num) + "/" + line[line.rfind("/"):] + ".cpg")
        except IOError:
            print('no such file as ' + line + ".cpg")
        try:
            if not os.path.isfile(header + str(num) + "/" + line[line.rfind("/"):] + '.prj'):
                shutil.copy(line + '.prj', header + str(num) + "/" + line[line.rfind("/"):] + ".prj")
        except IOError:
            print('no such file as ' + line + ".prj")
        try:
            if not os.path.isfile(header + str(num) + "/" + line[line.rfind("/"):] + '.shp.xml'):
                shutil.copy(line + '.shp.xml', header + str(num) + "/" + line[line.rfind("/"):] + ".shp.xml")
        except IOError:
            print('no such file as ' + line + ".shp.xml")
        
        count += 1
        if count == 5000:
            count = 0
            num += 1