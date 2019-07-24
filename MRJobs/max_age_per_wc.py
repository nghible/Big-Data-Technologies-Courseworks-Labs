from mrjob.job import MRJob
from mrjob.step import MRStep

class MRmyjob(MRJob):
	def mapper(self, _, line):
		data=line.split(", ")
		if len(data)>=2:
			age = data[0].strip()
			work_class = data[1]
			yield (work_class, age), 1

	def reducer1(self, key, list_of_values):
	# First reducer is to find the ocurrence of every age
		yield key, sum(list_of_values)

	def reducer2(self, key, list_of_values):
	# Second reducer is to find the maximum age
		age = [int(i) for i in key[1]]
		max_age = max(age)
		if key[1] == max_age:
			yield key[0], (list_of_values, key[1])

	def steps(self):
		return [MRStep(mapper=self.mapper, reducer=self.reducer1),
			MRStep(reducer=self.reducer2)]

if __name__== "__main__":
	MRmyjob.run()
