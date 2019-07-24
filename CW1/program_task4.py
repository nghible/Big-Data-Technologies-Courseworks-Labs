
from mrjob.job import MRJob

class MRmyjob(MRJob):

	def mapper(self, _, line):
		# Split data
		data = line.split(', ')
		# Get the key
		join_id = data[0].strip()
		yield join_id, (data[1],data[2])

	def reducer(self, key, values):
		# Append to a list
		a = [i for i in values]
		# yield key and the combined list of a for each key
		yield key, a


if __name__== "__main__":
	MRmyjob.run()
