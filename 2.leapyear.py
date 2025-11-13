from datetime import date
current=date.today().year
final=int(input("enter final year:"));
for year in range(current,final+1):
    if(year%4==0 and year%100!=0)or(year%400==0):
        print(year);
            

