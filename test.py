#coding=utf-8
import arcpy
import os
import shutil


shppath = "D:/DaTa/Yangtz/workflow/shape_ehi/fishnet/1km_inter.shp"
testpath = "D:/User/Desktop/Feature/2002.shp"


def split():
    own = []
    path = []
    for root,dirs,files in os.walk("E:/final/sub_/"):
        for file in files:
            if(file.split('.')[-1]=="shp"):
                if file.split('.')[0] not in own:
                    own.append(file.split('.')[0])
                    path.append("E:/final/sub_/" + file.split('.')[0])
    cursor = arcpy.UpdateCursor(shppath,"","","idj")
    arcpy.MakeFeatureLayer_management(shppath, "fine")
    for row in cursor:
            idj = row.idj
            if idj + '\n' not in own:
                if not os.path.isfile("E:/final/extra/" + row.idj + '.shp'):
                    print ('"idj"=\'' + row.idj + '\'')
                    arcpy.SelectLayerByAttribute_management("fine", "NEW_SELECTION", '"idj"=\'' + row.idj + '\'')
                    arcpy.CopyFeatures_management("fine", "E:/final/extra/" + row.idj + '.shp')
                    print (row.idj)
            try:
                cursor.updateRow(row)
            except:
                print ("update error!",row.idj)
if __name__ == '__main__':
    
    #split()
    cursor = arcpy.UpdateCursor(testpath)
    arcpy.MakeFeatureLayer_management(testpath, "fine")
    for row in cursor:
        print(row.idj)
        if row.idj == "1012":
            print(row.PAFRAC,row.CONTAG)
        else:
            cursor.updateRow(row)