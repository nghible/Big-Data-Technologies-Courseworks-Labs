# I will answer these questions on the first 10 lines of the 'adult' dataset

from mrjob.job import MRJob

class MRmyjob(MRJob):

	def mapper(self, _, line):
		# Split data by ,
		data=line.split(", ")
		if len(data)>=2:
			# Assign the first term of the data to age
			age = data[0].strip()
			# Assign the second term of the data to work_class
			work_class = data[1]
			# Yield every age as value and each work_class as key
			yield work_class, age


	def reducer(self, work_class, list_of_values):
		# Convert the values to integer for arithmetic
		a=[int(i) for i in list_of_values]
		# Take the average
		avg_a = float(sum(a)) / len(a)
		# Yield the average, group by work_class
		yield work_class, avg_a

if __name__== "__main__":
	MRmyjob.run()
