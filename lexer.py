#!/usr/bin/python

import ply.lex as lex
import ply.yacc as yacc
import sys

reserved = {
	'start':'comienzo',
	'if': 'si',
	'else': 'otro',
	'while': 'mientras',
	'do':'hacer',
	'return':'regresso',
	'print': 'imprimir',
	'scan': 'introducir',
	'for': 'para',
	'call':'avisar',
	'is': 'es',
	'try':'tratar',
	'end':'fin',
	'break':'romperse',
	'class':'clase',
	'def':'explicar',
	'end_def':'finexplicar'

}

tokens =[
	'VAR',
	'LT',
	'GT',
	'LEQ',
	'GEQ',
	'EQ',
	'NEQ',
	'NOT',
	'OR',
	'AND',
	'STRLIT',
	'CHRLIT',
	'INTLIT',
	'FLTLIT',
	'DBLLIT',
	'BOOLEAN',
	'PLUS',
	'MINUS',
	'MUL',
	'DIV',
	'MOD',
	'OPENPAR',
	'CLOSEPAR',
	'OPENCURLY',
	'CLOSECURLY',
	'OPENBRACE',
	'CLOSEBRACE',
	'ASSIGN',
	'COMMA',
	'TILDE'

]

tokens = list(reserved.values()) + list(tokens) 

# Regular expression rules for simple tokens
t_LT = r'\<'
t_GT = r'\>'
t_LEQ = r'\<='
t_GEQ = r'\>='
t_EQ = r'\=='
t_NEQ = r'\!='
t_NOT = r'\!'
t_OR = r'\|'
t_AND = r'\&&'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_OPENCURLY = r'\{'
t_CLOSECURLY = r'\}'
t_OPENBRACE = r'\['
t_CLOSEBRACE = r'\]'
t_ASSIGN = r'\='
t_TILDE = r'\~'

# Ignore whitespaces
t_ignore = r' '

def t_FLTLIT(t):
	r'\d\.\d+'
	t.value = float(t.value)
	return t


def t_INTLIT(t):
	r'\d+'
	t.value = int(t.value)
	return t
	
# Determining if reserved word
def t_VAR(t):
	r'[a-z][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value.lower(), 'VAR')
	return t
	
# Match the first quotes for strings
def t_STRLIT(t):
	r'[\"][^\"]+[\"]'
	t.value = str(t.value).strip('\"')
	return t
	
# Defining a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
 
# RegExp for comments: No return value. Token discarded.
def t_COMMENT(t):
	r'\*~.*'
	pass


def t_error(t):
	print("SYNTAX ERROR: Illegal character: '%s' \n\tLine number: %d" (t.value[0], t.lineno))
	t.lexer.skip(1)

 # Build the lexer
lexer = lex.lex()



