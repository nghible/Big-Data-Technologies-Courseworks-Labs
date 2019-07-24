from mrjob.job import MRJob

class MRmyjob(MRJob):
	def mapper(self, _, line):
		data=line.split(", ")
		if len(data)>=2:
			age=data[0].strip()
			yield None, age

	def reducer(self, _, list_of_values):
		a=[int(i) for i in list_of_values]
		avg_a = sum(a) / (len(a))
		yield "average_age:", avg_a

if __name__== "__main__":
	MRmyjob.run()
