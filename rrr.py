import os
import subprocess
import multiprocessing as mp



def gera_pathfbt(year):

        clip = "E:/final/out/10km/" + str(year) + "/"
        clip_save = "E:/final/out/out_10km/" + str(year) + "/" 
        more = ",x,999,x,x,1,x,IDF_GeoTIFF"
        count = 0
        pathlist = os.listdir(clip)
        i = 0
        while(True):                   #This time we change to 900, for the fragstats showed overflow error when running folder 5.
            clipf = open(clip_save + "/_" + str(i) + ".fbt", 'w+')
            for line in pathlist:
                (filename, extension) = os.path.splitext(line)
                if (extension == ".tif"):
                    clipf.write(clip + '/' + line + more + '\n')
                    count += 1
                    if count/2000==1:
                        pathlist = pathlist[2000:]
                        count = 0
                        break
                else:
                    count += 1
                    if count/2000==1:
                        pathlist = pathlist[2000:]
                        count = 0
                        break
            i = i + 1
            if len(pathlist) < 2000:
                break
        clipf = open(clip_save + "/_" + str(i) + ".fbt", 'w+')
        for line in pathlist:
            (filename, extension) = os.path.splitext(line)
            if (extension == ".tif"):
                clipf.write(clip + '/' + line + more + '\n')


def run(path,j):
    FBTs = []
    for i in range(100):
        if os.path.isfile(path + "/_" + str(i) + ".fbt") is True:
            FBTs.append("_" + str(i) + ".fbt")
        else:
            break
    for fbt in FBTs:
        print (fbt)
        os.chdir(path)
        out = path +"/fragout" + fbt[1:-4]
        fca = "F:/fras/unnamed" + str(j) + ".fca"
        task = subprocess.Popen('frg -m '+ fca +' -b '+ fbt + ' -o ' + "\"" + out + "\"", stdout = subprocess.PIPE, shell = True)
        print(task.stdout.read())


def Frg(year):
    root = "E:/final/out/out_10km/"+str(year)

    path = root

    mpp = mp.Pool(processes=7)
    mpp.daemon = True

    mpp.apply_async(run, args=(path, 1)) 
    mpp.close()  
    mpp.join()
    print ("whole year finished")


    
if __name__ == '__main__':
    years = [2000,2010,2020]
    for year in years:
        print ("will be running "+str(year)+ "\n")
        print ("gepa_succ")
        Frg(year)
