from mrjob.job import MRJob

import re
WORD_RE = re.compile(r"[\w']+")

class wordcount(MRJob):

	def mapper(self, _, line):
		age = WORD_RE.findall(line)[0]
		yield(age,1)

	def reducer(self, age, counts):
		yield (age, sum(counts))

if __name__ == '__main__':
	wordcount.run()
