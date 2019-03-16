import lexer
import parser
import sys
def main():
	content = ""
	with open("test.lang", "r") as file:
		content=file.read()

#build the lexer and parser
	lex = lexer.lexer(content)
	parse = parser.parser(content)

	tokens = lex.tokenize()

main()
 	