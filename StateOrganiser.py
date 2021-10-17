from os import name
import pandas
import csv
with open('tweetdata.csv') as f:
    #lines = f.readlines()
    #print(*lines, sep="\n")
    #https://www.kite.com/python/answers/how-to-read-specific-column-from-csv-file-in-python#:~:text=Use%20pandas.,read%20from%20the%20CSV%20file.
    col_list = ["0", "1", "2"]
    df = pandas.read_csv("tweetdata.csv", usecols=col_list)
    class states: 
        def __init__(self, name, count): 
            self.name = name 
            self.count = count
        def __repr__(self): 
            return "State name:% s count:% s" % (self.name, self.count) 
    statestring = "Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming"
    statestringabrev = "AL, AK, AZ, AR, CA, CO, CT, DE, DC, FL, GA, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY"
    
    statestringlist = statestring.split(", ")
    statestringlistabrev = statestringabrev.split(", ")
    stateobjlist = []

    for i in statestringlistabrev:
        stateobjlist.append(states(i, 0))

    totalCount = 0
    for i in df["2"]:
        #for j in statestringlistabrev:
        for index, j in enumerate(statestringlistabrev):
            if j in str(i):
                stateobjlist[index].count += 1
                totalCount += 1
            
        for index, j in enumerate(statestringlist):
            if j in str(i):
                stateobjlist[index].count += 1
                totalCount += 1

    # with open('stateOccurence.csv', 'w') as q:
    #     write = csv.writer(q) 
    #     for i in stateobjlist:
    #         #write.writerow([i.name, i.count]) 
    #         write.writerow([i.count])
    #         #print(i)
    
    textfile = open("stateOccurence.txt", "w")
    for element in stateobjlist:
        textfile.write(str(element.count) + ",")
    textfile.close()
    print(totalCount)
    # print(len(statestringlist))
    # print(len(statestringlistabrev))

    #for i in df["2"]:
     #   print(i)


