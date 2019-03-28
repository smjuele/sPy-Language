import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
import parser
import lexer
import sys


def main():
	try:
		file_input = sys.argv[1];
		pass
	except Exception as e:
		print("Missing file input!")
		print("Try this: python main.py <filename>")
		sys.exit()
		
	# Open the input file.
	f = open(file_input, 'r')
	data = f.read()
	f.close()

	lexer.input(data)
	print("TOKENS:")
	while True:
		tok = lexer.token()
		if not tok: 
			break
		print("\t",tok)
	print("\nEVALUATION:")
	
	parser.parse(data)

 	