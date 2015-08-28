#!/usr/bin/python
import sys, getopt
import xlwt
import os.path
from Tkinter import *
from tkFileDialog   import askopenfilename      



def callback():
	inputfile= askopenfilename()
	outputfile='result.xml'

	book = xlwt.Workbook(encoding="utf-8")
	sheet1 = book.add_sheet("Sheet 1")

	filename=inputfile
	file = open(filename,'r')
	file.seek(0)
	count=1
	cols=2
	items={}
	while True:
		line = file.readline()
		if not line:
			break
		
		data = line[0:8]
		print "len data ", len(line)
		if len(line) > 20:
			sheet1.write(count+1,cols,len(items))
			cols=cols+1
			count=1
			data=line
			items={}

		if data in items:
			print "data is contain", data
		else:
			sheet1.write(count,cols,data)
			count=count+1
			items[data]=data

		print count ,"-data\t",data,"\t",line
	#end while

	file.close()
	book.save(outputfile)


def main(argv):
    inputfile = ''
    outputfile = 'result.xml'
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print 'Input file is "', inputfile
    print 'Output file is "', outputfile
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    #filename ='/home/yellow/Projects/PyWorkSpace/PyLogToExcel/smartap_3822.log'
    #    filename ='/home/yellow/Projects/PyWorkSpace/smartap_3822.log'
    filename=inputfile
    print filename
    #print filename
    print os.path.isfile(filename)

    file = open(filename,'r')
    file.seek(0)
    print "file",file
    count=1
    #lines=file.readlines()
    #for line in lines:
    #    count=count+1
    ##    print line ,"-", count
    #    print count ,"-", line
    #    sheet1.write(count,0,line)

    ##lines = file.readline(100)
    ##for line in lines:
    ##    print line ,"-",count
    ##    count=count+1
    ##    sheet1.write(count,0,line)
    count=1    
    cols=2
    items={}
    while True: 
    #    if count > 100 :break    
        line = file.readline()
        if not line:
			break
        data = line[0:8]
        print "len data ", len(line)
        if len(line) > 20:
	    sheet1.write(count+1,cols,len(items))
            cols=cols+1
            count=1
            data=line
	    items={}
        

	if data in items:
	    print "data is contain", data
        else:
	    items[data]=data
            sheet1.write(count,cols,data)
            count=count+1

        print count ,"-data\t",data,"\t",line
    #end while

    file.close()
    book.save(outputfile)


if __name__ == "__main__":
#   main(sys.argv[1:])
	errmsg = 'Error!'
	Button(text='Log File Open', command=callback).pack(fill=X)
	mainloop()