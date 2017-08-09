import os
import Foxboro_data_tools
import shutil

#foxboro2isco_041013

sriver_sourcedir = r'\\10.96.10.1\Export\data\MI'           #South River
sriver_destdir = 'M:\Foxboro South River Converted Data'




print("sriver_sourcedir: " + sriver_sourcedir)
print("sriver_destdir: " + sriver_destdir + '\n')

for dirs in os.listdir(sriver_sourcedir):                  #list all subdirs in root directory
    eachDir= os.path.join(sriver_sourcedir,dirs)           #create path for subdirs
    for files in os.listdir(eachDir):               #list all files in each subdir
        filepath=os.path.join(eachDir,files)        #create path for each file
        oldSiteName= os.path.splitext(files)[0].strip()
        newSiteName = Foxboro_data_tools.convertSiteName(oldSiteName)

        input_file = open(filepath)  #open exported data file

        sriver_destpath = sriver_destdir + "/" + dirs + '_' + newSiteName + '=' + oldSiteName + '.csv' #write converted header to new file
        output = open(sriver_destpath, 'w')     
        output.write("Site name," + newSiteName + '=' + oldSiteName + '\n')    #create header for exported file
        output.write("Isco Quantity,Flow Rate\n")
        output.write("Label,Flow Rate\n")
        output.write("Units,mgd\n")
        output.write("Resolution,0.1\n")
        output.write("Significant Digits,0\n")
        output.write("\n")

        for read_data in input_file:                     #read all data lines
            dataline = read_data.split()
            numcols = len(dataline)

            ymd=dataline[0].split('/')
            year=ymd[0]
            month=ymd[1]
            date=ymd[2]
        
        
            hms=time=dataline[1].split(':')
            hours=hms[0]
            minutes=hms[1]
            seconds=hms[2]
            reading=str(round(float(dataline[2]),4))
            #print date + '/' + month + '/' + year + ',' + hours + ':' + minutes + ',' + reading + '\n'
            output.write(month + '/' + date + '/' + year + ' ' + hours + ':' + minutes + ',' + reading + '\n')
        
        output.flush()
        output.close()
        print(sriver_destpath)
        
print("Conversion Complete\n")
