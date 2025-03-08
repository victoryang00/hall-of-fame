import dblp
import operator
import pickle

sosp_file = open("sosp.data", 'rb')
osdi_file = open("osdi.data", 'rb')
total_file = open("total.data", 'rb')

sosp = pickle.load(sosp_file)
osdi = pickle.load(osdi_file)
total = pickle.load(total_file)

sosp_file.close()
osdi_file.close()
total_file.close()

# choose here whether sosp or osdi or both        
#sorted_x = sorted(sosp.items(), key=operator.itemgetter(1), reverse=True)
#sorted_x = sorted(osdi.items(), key=operator.itemgetter(1), reverse=True)
sorted_x = sorted(list(total.items()), key=operator.itemgetter(1), reverse=True)

print("Top 25 Authors:")
i = 1
for x,c in sorted_x:
    if i < 120:
        print(i, x, c)
    i += 1
    if x in ["Vijay Chidambaram", "Simon Peter", "Christopher J. Rossbach", "Taesoo Kim", "Xi Wang", "Marcos K. Aguilera", "Michael M. Swift", "Ding Yuan"]:
        print(i, x, c)
        

