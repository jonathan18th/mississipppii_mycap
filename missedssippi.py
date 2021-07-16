most_frequent = input("Please enter  a string")


all_freq ={}
  
for x in most_frequent:
    if x in all_freq:
        all_freq[x] += 1
    else:
        all_freq[x] = 1
sorted_dict = dict( sorted(all_freq.items(),
                           key=lambda item: item[1],
                           reverse=True))        

print("output is :\n " +  str(sorted_dict))                                        
