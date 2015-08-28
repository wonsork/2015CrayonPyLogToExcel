#!/usr/bin/python
import sys, getopt
import xlwt
import os.path


#python setup.py py2app

def main(argv):
    inputfile = ''
    outputfile = 'result.xls'
    filter=False
    try:
        opts, args = getopt.getopt(argv,"hi:o:f",["ifile=","ofile=","filter"])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile> -f <filter same tag by second> '
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-f", "--filter"):
	    filter=True

    
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile
    print 'Filter ', filter

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
        if not line: break
        data = line[0:8]
        print "len data ", len(line)
        if len(line) > 20:
	    sheet1.write(count+1,cols,len(items))
            cols=cols+1
            count=1
            data=line
	    items={}

	
	if filter:
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
   main(sys.argv[1:])
