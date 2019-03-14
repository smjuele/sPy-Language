import lexer
import parser
def main():
	content = ""
	with open("test.lang", "r") as file:
		content=file.read()

	#build the lexer and parser
	lex = lexer.Lexer(content)
	parse = parser.parser(content)

	tokens = lex.tokenize()
main()