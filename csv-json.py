fi = open("06-15-2020.csv","r")
delfirst = fi.readline() # skip over titles
lines = fi.readlines()
fi.close()

conflist = []
for line in lines:
    templist = line.split(",")
    pname = templist[2]
    cname = templist[3]
    date = templist[4]
    lat = templist[5]
    lon = templist[6]
    conf = int(templist[7])
    conflist.append({"pname":pname,"cname":cname,"confirmed":conf, "lat":lat, "lon": lon})

conflist.sort(key=lambda s: s['confirmed'], reverse=True)
fo = open("06-15-2020.js","w")
fo.write("data = " + str(conflist))
fo.close()
