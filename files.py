


import sys, argparse

class DoTheThing:

	
	def __init__(self, args):
		self.thefile = args.thefile
		
		
	def count_lines(self):
		'''return the number of lines in the file'''
		
		pass
		
	def count_word(self, theword):
		''' return the number of times 'theword' appears in the file
		
		'''
		pass
		
	def most_common_word(self):
	''' return the most common word'''
	
		pass
	

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Read a file and do things')
	parser.add_argument("thefile", help="the file to pass in"
	
	thing = DoTheThing(parser.parse_args())
	
	# uncomment lines here on what thing you want to test
	
	thing.count_lines()
	
