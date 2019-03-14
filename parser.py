#!/usr/bin/python

import ply.yacc as yacc

precedence = (
	('left','PLUS','MINUS'),
	('left','MUL','DIV', 'MOD'),
)

def p_main_program(p):
	
	'''
		main_program : comienzo OPENCURLY statement CLOSECURLY fin
					 | comienzo clase fin
					 | comienzo function_heading fin					
	'''
def p_statement_assign(t):
    		"statement : IDNAME ASSIGN expression"
		

def p_statement_expr(p):
		"statement : expression"

def p_statement_if_stmt(p):
    "if_statement : si OPENPAR  boolean_expression CLOSEPAR statement"
    si (p[3]):
        p[0] = p[5]

def p_statement_if_else(p):
    'if_statement : si OPENPAR boolean_expression CLOSEPAR statement otro statement'
    si (p[3]):
        p[5]
    otro:
        p[7]

def p_statement_print(t):
    'statement : imprimir OPENPAR expression CLOSEPAR'
    imprimir(t[3])

def p_statement_print_string(t):
    'statement : imprimir OPENPAR STRING CLOSEPAR'
    imprimir(t[3])

def p_statement_print_var(t):
    'statement : VAR ASSIGN expression imprimir OPENPAR VAR CLOSEPAR'
    imprimir("Result: ", t[3])

def p_statement_print_var_string(t):
    'statement : VAR ASSIGN STRING imprimir OPENPAR VAR CLOSEPAR'
   imprimir("Result: ", t[3])

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
	
