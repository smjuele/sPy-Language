#!/usr/bin/python

import ply.yacc as yacc

precedence = (
	('left','PLUS','MINUS'),
	('left','MUL','DIV', 'MOD'),
)

def p_main_program(p):
	#!/usr/bin/python

import ply.yacc as yacc

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV', 'MOD'),
)

def p_main_program(p):
    
    '''
        main_program : comienzo OPENCURLY statement CLOSECURLY fin
                     | comienzo classes fin
                     | comienzo function_heading fin                    
    '''
def p_statement(p):
    '''
        statement  : identifier_list EQ expression
                    | introducir type
                    | imprimir OPENPAR identifier_list CLOSEPAR
                    | imprimir QUOTATION identifier_list QUOTATION
                    | regresso OPENPAR expression_list CLOSEPAR
                    | optional_statements
                    | while
                    | si OPENPAR expression_list CLOSEPAR statement
                    | si OPENPAR expression_list CLOSEPAR statement else_if
                    | comment
    '''

def p_identifier_list(p):
    '''
        identifier_list : CHRLIT identifier_list
                        | STRLIT identifier_list
                        | INTLIT identifier_list
                        | UNDERSCORE
                        | empty
    '''
def p_empty(p):
    '''
        empty: 
    '''
    #p[0] = None

def p_expression(p):
    '''
        expression  : expression
                    | expression_list COMMA expression
                    | identifier_list
    '''
def p_expression_list(p):
    '''
        expression_list : logical_expression
                        |  arithmetic_expression
    '''
def p_logical_expression(p):
    '''
        logical_expression  : expression LT expression
                            | expression GT expression
                            | expression LEQ expression
                            | expression GEQ expression
                            | expression EQ expression
                            | expression NEQ expression
                            | expression EQ expression
                            | expression NOT expression
                            | expression OR expression
                            | expression AND expression
    '''

def p_arithmetic_expression(p):
    '''
        airthmetic_expression : expression PLUS expression
                              |  expression MINUS expression
                              |  expression MUL expression
                              |  expression DIV expression
                              |  expression MOD expression
    '''

def p_type(p):
    '''
        type : int identifier_list TILDE
             | float identifier_list TILDE 
             | double identifier_list TILDE 
             | char identifier_list TILDE 
             | string identifier_list TILDE 
    '''
def p_optional_statements(p):
    '''
        optional_statements: statement_list
                           | empty 
    '''

def p_statement_list(p):
    '''
        statement_list : statement
                       | statement_list statement 

    '''
def p_else_if(p):
    '''
        else_if : otro OPENPAR expression CLOSEPAR statement else_if
                | empty
    '''

def p_while(p):
    '''
        while : mientras OPENPAR expression_list CLOSEPAR TILDE optional_statements TILDE
              | mientras OPENPAR expression_list CLOSEPAR TILDE optional_statements TILDE romperse
    '''

def p_comment(p):
    '''
    '''

def p_classes(p): 
    '''
        classes : clase OPENCURLY identifier_list optional_statements CLOSECURLY
    '''

def p_function_heading(p):
    '''
        function_heading: explicar OPENPAR parameters TILDE CLOSEPAR
    '''
def p_parameters(p):
    '''
        parameters: type
                  | type COMMA parameters
                  | empty
    '''

# def p_statement_assign(t):
#           "statement : IDNAME ASSIGN expression"
        
# def p_statement_expr(p):
#       "statement : expression"

# def p_statement_if_stmt(p):
#     "if_statement : si OPENPAR  boolean_expression CLOSEPAR statement"
#     si (p[3]):
#         p[0] = p[5]

# def p_statement_if_else(p):
#     'if_statement : si OPENPAR boolean_expression CLOSEPAR statement otro statement'
#     si (p[3]):
#         p[5]
#     otro:
#         p[7]

# def p_statement_print(t):
#     'statement : imprimir OPENPAR expression CLOSEPAR'
#     imprimir(t[3])

# def p_statement_print_string(t):
#     'statement : imprimir OPENPAR STRING CLOSEPAR'
#     imprimir(t[3])

# def p_statement_print_var(t):
#     'statement : VAR ASSIGN expression imprimir OPENPAR VAR CLOSEPAR'
#     imprimir("Result: ", t[3])

# def p_statement_print_var_string(t):
#     'statement : VAR ASSIGN STRING imprimir OPENPAR VAR CLOSEPAR'
#    imprimir("Result: ", t[3])

# def p_expression_plus(p):
#     'expression : expression PLUS expression'
#     p[0] = p[1] + p[3]

# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]
    

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
	
