import datetime
import dblp
import operator
import pickle

# Dicts to store conference data. I'm focussing on SOSP and OSDI for
# these scripts.
sosp = {}
osdi = {}
total = {}
total5 = {}
author_meta = {}

cur_year = datetime.datetime.now().year

last5 = datetime.datetime.now().year - 5
next_year = datetime.datetime.now().year + 1
print(last5)

# Get publication data from DBLP for each version of the
# conference. You might have to poke around DBLP XML entries for your
# conference to identify the "crossref" (conf/sosp) and "booktitle"
# (SOSP) for the conference you are interested in
for y in range(1969, 2023, 2):
    print("SOSP", y)
    try:
        a = dblp.getvenueauthors("/conf/sosp/" + str(y), "SOSP")
        for x in a:
            sosp[x] = sosp.get(x, 0) + 1
            total[x] = total.get(x, 0) + 1
            if y >= last5:
                total5[x] = total5.get(x, 0) + 1
    except Exception as e:
        print(e)

for y in range(2023, next_year, 1):
    print("SOSP", y)
    try:
        a = dblp.getvenueauthors("/conf/sosp/" + str(y), "SOSP")
        for x in a:
            sosp[x] = sosp.get(x, 0) + 1
            total[x] = total.get(x, 0) + 1
            if y >= last5:
                total5[x] = total5.get(x, 0) + 1
    except Exception as e:
        print(e)
for y in range(1994, 2020, 2):
    print("OSDI", y)
    try:
        a = dblp.getvenueauthors("/conf/osdi/" + str(y), "OSDI")
        for x in a:
            osdi[x] = osdi.get(x, 0) + 1
        total[x] = total.get(x, 0) + 1
        if y >= last5:
            total5[x] = total5.get(x, 0) + 1
    except Exception as e:
        print(e)

# OSDI becomes annual
for y in range(2020, next_year, 1):
    print("OSDI", y)
    try:
        a = dblp.getvenueauthors("/conf/osdi/" + str(y), "OSDI")
        for x in a:
            osdi[x] = osdi.get(x, 0) + 1
        total[x] = total.get(x, 0) + 1
        if y >= last5:
            total5[x] = total5.get(x, 0) + 1
    except Exception as e:
        print(e)
            
sosp_file = open("sosp.data", 'wb')
osdi_file = open("osdi.data", 'wb')
total_file = open("total.data", 'wb')
total_5_file = open("total5.data", 'wb')

pickle.dump(sosp, sosp_file)
pickle.dump(osdi, osdi_file)
pickle.dump(total, total_file)
pickle.dump(total5, total_5_file)

sosp_file.close()
osdi_file.close()
total_file.close()
total_5_file.close()
