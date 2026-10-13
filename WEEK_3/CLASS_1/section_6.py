# mean median and so on....
scores = [70,60,48,30]
mean = sum(scores)/len(scores)
median = sorted(scores)[2]
print(mean,median)

# disperrsion: variance and standard deviation
data = [4,8,6,10,12]
mean = 8
variance = sum((x - mean)**2 for x in data)/len(data) #formula
std_dev = variance**0.5
print(variance,std_dev)

# task : high and low variance find them....
# high variance = values are away from mean mean = 2 value = [2,3,4,10,20,30]
# low variace = values are near mean mean = 10 values = [10,11,12,10]

# co-efficent of variance cv
cv = (std_dev/mean)*100
print(cv)

# corelationa and coefficient
# r = +1 positive co relation
# r = 0 no corelation
# r = -1 negative co realtion
