import collections
import matplotlib.pyplot as plt

file_names = ['Laabbc', 'Laabcd','Labcde','LLaabb','LLaabc','LLabcd','LLLaab','LLLabc','LLLLaa','LLLLab']
max_value = 0
histogram = collections.defaultdict(int)

for file_name in file_names:
    with open('results/'+file_name+'.txt') as f:
        print file_name
        #possible_numbers = set([])
        line_count = 0
        num_count = 0
        for line in f.read().splitlines():
            data = line.split(';')
            key = data[0][1:-1].replace(" ","")
            value = map(int,data[1:-1])

            for i in value:
                histogram[i] += 1

            #line_count += 1
            #num_count += len(value)

            #possible_numbers.update(value)

            #max value
            #if len(value) > max_value:
            #    max_key, max_value = key,len(value)

            #12 values over 630
            #if len(value) > 630:
            #    print key, len(value)

            # ~10 values under 40
            #if len(value) < 40:
            #    print key, len(value)
        #print len(possible_numbers)
        #print line_count, num_count, num_count/float(line_count)

#print "max_values", max_key, max_value

# Plot values in histogram
vals = [histogram[k] for k in sorted(histogram)]
plt.vlines(x=range(100,1000), ymin=0, ymax=vals, color='#007acc', alpha=0.2)
plt.plot(range(100,1000), vals, "o", color='#007acc', alpha=0.6, markersize=2.)
plt.xlabel('Three-Digit Number')
plt.ylabel('Frequency')
plt.show()
