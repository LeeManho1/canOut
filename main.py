import os
import datetime

class Date:
    def __init__(self):
        self.date=datetime.datetime.now()

    def creat_date(self, y, m, d):
        self.date=datetime.datetime(y ,m, d, 0, 0, 0)
    def creat_time(self, y,m,d,h,mi,s):
        self.date=datetime.datetime(y,m,d,h,mi,s)

    def back(self):
        y=self.date.year
        m=self.date.month
        d=self.date.day
        wk=self.date.weekday()
        return [y,m,d,wk]

    def can(self):
        y=self.date.year
        m=self.date.month
        #d=self.date.day
        #wk=self.date.weekday()

        if y%100==0:
            if y%400==0 :
                rn=1
            else:
                rn=0
        elif y%4==0:
            rn=1
        else:
            rn=0

        dim=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        dim[2]+=rn
        mo=[0,"January","February","March","April","May","June","July","August","September","October","November","December"]
        
        #datetime.datetime(y,m,1,0,0,0)

        wk=datetime.datetime(y,m,1,0,0,0).strftime("%w")
        wk=int(wk)+1
        print()
        print(mo[m])
        print("Sun  Mon  Tue  Wed  Thu  Fri  Sat")
        print("     "*(wk-1),end="")
        #print("  ",end="")
        for i in range(1,dim[m]+1):
            if i==self.date.day:
                print(f"[{i:2d}]",end=" ")
            else:
                print(f" {i:2d} ",end=" ")
            
            if wk==7:
                print()
                wk=0
            wk+=1
        print()



        
        
        

            
        




if __name__ =="__main__":
    a=Date()
    #a.creat_date(2026,12,25)
    print("can()")
    a.can()



    pass
