%{
	#include <stdio.h>	
	#include "tree.h"
	int yylex();
	void yyerror(const char *s);
%}
%union{
	Tree pVal;
	int iVal;
	char *sVal;
}
%type <pVal> Exp Term
%token	<iVal>	NUM