#coding=utf-8
import arcpy
import os

shppath = "D:/DaTa/Yangtz/workflow/shape_ehi/fishnet/"

if __name__ == '__main__':
    own = []
    # for root,dirs,files in os.walk("D:\\DaTa\\Yangtz\\workflow\\shape_ehi\\sp_\\1\\"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    # for root,dirs,files in os.walk("D:\\DaTa\\Yangtz\\workflow\\shape_ehi\\sp_\\2\\"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    # for root,dirs,files in os.walk("D:\\DaTa\\Yangtz\\workflow\\shape_ehi\\sp_\\3\\"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    # for root,dirs,files in os.walk("E:/final/1/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    for root,dirs,files in os.walk("E:/final/2/"):
        for file in files:
            if(file.split('.')[-1]=="shp"):
                if file.split('.')[0] not in own:
                    own.append(file.split('.')[0])
    for root,dirs,files in os.walk("E:/final/sub/"):
        for file in files:
            if(file.split('.')[-1]=="shp"):
                if file.split('.')[0] not in own:
                    own.append(file.split('.')[0])
    # for root,dirs,files in os.walk("E:/final/3/"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    # for root,dirs,files in os.walk("D:\\DaTa\\Yangtz\\workflow\\shape_ehi\\sp_\\split\\"):
    #     for file in files:
    #         if(file.split('.')[-1]=="shp"):
    #             if file.split('.')[0] not in own:
    #                 own.append(file.split('.')[0])
    with open("D:\\DaTa\\Yangtz\\workflow\\shape_ehi\\record.txt", 'w') as f:
        for rec in own:
            f.write(rec)
            f.write("\n")
    own = []
    count = 0
    with open("D:\\DaTa\\Yangtz\\workflow\\shape_ehi\\record.txt") as f:
        for line in f:
            own.append(line[0:-1])
            count += 1
    
    for num in '2':
        print (num)
        print (count)
        print ("\n")
        print ("\n")
        print ("\n")
        cursor = arcpy.UpdateCursor(shppath + num + ".shp","","","idj")
        arcpy.MakeFeatureLayer_management(shppath + num + ".shp", "fine")
        # arcpy.env.overwriteOutput = True
        for row in cursor:
            idj = row.idj 
            if idj + '\n' not in own:
                if not os.path.isfile("E:/final/"+ num + "/" + row.idj + '.shp'):
                    print ('"idj"=\'' + row.idj + '\'')
                    arcpy.SelectLayerByAttribute_management("fine", "NEW_SELECTION", '"idj"=\'' + row.idj + '\'')
                    arcpy.CopyFeatures_management("fine", "E:/final/"+ num + "/" + row.idj + '.shp')
                    print (row.idj)
            try:
                cursor.updateRow(row)
            except:
                print ("update error!",row.idj)

