class Lexer(object):

		def __init__(self, source_code):
			self.source_code=source_code

		def tokenize(self):
			tokens=[] #where tokens will be stored

			source_code = self.source_code.split()

			source_index = 0
			#print('test')
			while source_index < len(source_code):

				print (source_code[source_index])

				source_index +=1
			return tokens