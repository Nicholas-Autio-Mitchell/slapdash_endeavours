
## ================================================================================= ##
##  Plot multiple addresses or other data on top of a region taken from Google Maps  ##
## ================================================================================= ##

# import gmplot
import csv
import itertools


def addr(line):
    if line.startswith('NEXT_ADDRESS'):
        addr.count =+ 1
    return addr.count

addr.count = 0

# get the addresses of all the places, perform cleanup
with open('./test_addresses.txt', 'r') as f:
    input = csv.reader(f)

    lines_to_write = []

    for i, line in enumerate(input):

        try: # two checks to remove telephone/fax numbers
            if line[0][0:2] == 'T:' or line[0][0:2] == 'F:':
                print('skipped a T:/F: number')
                pass                       

            elif sum(char.isnumeric() for char in line[0]) > 5:
                print('skipped a telephone/fax number')
                pass

            # skip any lines containing an email address
            # assumes names and addresses do not contain the @ symbol
            elif '@' in line[0]:
                print('removed email address: {}'.format(line))

            else:
                lines_to_write.append(line)

        except IndexError: # catch the empty lines between each address
            lines_to_write.append(['NEXT_ADDRESS'])

# create a dictionary to hold all addresses, then append the lats and longs later
address_book = {}

# separate the address, using the 'NEXT_ADDRESS' lines added in the checks above
tmp = []
counter = 1
for line in lines_to_write:
    if line == ['NEXT_ADDRESS']:
        chunk_addr = ', '.join([l[0] for l in tmp])
        address_book[str(counter)] = chunk_addr
        tmp = []
        counter += 1
    
    else:
        #print('line = {}'.format(line))
        tmp.append(line)
        
for k, v in address_book.items():
    print('Address {}: {}'.format(k, v))

with open('./just_addresses.txt', 'w') as o:
    output = csv.writer(o)
    # address_book[i] = address for i, address in enumerate(lines_to_write)
    [output.writerow([address]) for i, address in address_book.items()]



    

    
# with open('./just_addresses.txt') as f:
#     for k, group in itertools.groupby(f, addr):
#         print(k, list(group))

# gmap = gmplot.GoogleMapPlotter(48.141065, 11.578710, 10)

# gmap.plot([48.141065], [11.578710], 'cornflowerblue', edge_width=10)
# gmap.draw('test.html')
    
#gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
#gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
#gmap.heatmap(heat_lats, heat_lngs)
