from pyspark import SparkContext
from operator import add

sc = SparkContext('local','pyspark')

def age_group(age):
	if age < 10:
		return '0-10'
	elif age < 20:
		return '10-20'
	elif age < 30:
		return '20-30'
	elif age < 40:
		return '30-40'
	elif age < 50:
		return '40-50'
	elif age < 60:
		return '50-60'
	elif age < 70:
		return '60-70'
	elif age < 80:
		return '70-80'
	else:
		return '80+'

def parse_with_age_group(data):
	userid, age, gender, occupation, zip = data.split("|")
	return userid, age_group(int(age)), gender, occupation, zip, int(age)

# Create RDD of u.user file:

fs = sc.textFile("file:///home/cloudera/Downloads/CW2/u.user")

# Convert age into age groups:

data_with_age_group = fs.map(parse_with_age_group)

# Sorting the data as RDDs:

# First, we will filter the data by the age group, then we map each occupation to a value of 1. Then, we use ReduceByKey
# method to count all the entries the belongs to each group. Then we use the SortBy method to sort by the values in descending order.
# Finally we use the keys method to get only the occupations.

sorted_40_50 = data_with_age_group.filter(lambda x: ('40-50' in x)).map(lambda x: (x[3],1)).reduceByKey(lambda a,b: a + b).sortBy(lambda x: x[1], 0).keys()

sorted_50_60 = data_with_age_group.filter(lambda x: ('50-60' in x)).map(lambda x: (x[3],1)).reduceByKey(lambda a,b: a + b).sortBy(lambda x: x[1], 0).keys()

# Get the top 10 most frequent occupation of each age group

top_40_50 = sorted_40_50.take(10)
top_50_60 = sorted_50_60.take(10)

# Get the intersection of the lists

print list(set(top_40_50) & set(top_50_60))
