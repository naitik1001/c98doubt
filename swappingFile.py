from fileinput import filename


def swapFileData():
    filename1=input("enter the filename1")
    filename2=input("enter the filename2")
    numberOfWords=0
    data_a=open(filename1,'r')
    data_b=open(filename2,'r')


    data_b=open(filename1,'r+')
    data_a=open(filename2,'r+') 
swapFileData()