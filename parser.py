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
	
