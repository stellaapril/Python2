import csv


#dictionaries
yearsDic = {}
datesDic = {}
areasDic = {}
typesDic = {}
statusDic={}

#open csv file

file = open('capitalprojects.csv',newline='')
reader = csv.DictReader(file)


info = int(input('choose 1=fiscal_years,2=start_date,3=area,4=asser_type,5=planning_status: '))

for row in reader:
    #fiscal year
    if info == 1:
        i=row['fiscal_year']
        if i not in yearsDic:
            yearsDic[i]=1
        else:
            yearsDic[i]+=1

    #start date
    if info == 2:
        i=row['start_date']
        if i not in datesDic:
            datesDic[i]=1
        else:
            datesDic[i]+=1

    #area
    if info == 3:
        i=row['area']
        if i not in areasDic:
            areasDic[i]=1
        else:
            areasDic[i]+=1

    #assert type
    if info == 4:
        i=row['asset_type']
        if i not in typesDic:
            typesDic[i]=1
        else:
            typesDic[i]+=1

    #planning status
    if info == 5:
        i=row['planning_status']
        if i not in statusDic:
            statusDic[i]=1
        else:
            statusDic[i]+=1


#close file
file.close()


#print
def main():
    if info ==1:
        print(yearsDic)
    elif info ==2:
        print(datesDic)
    elif info ==3:
        print(areasDic)
    elif info ==4:
        print(typesDic)
    elif info ==5:
        print(statusDic)

main()