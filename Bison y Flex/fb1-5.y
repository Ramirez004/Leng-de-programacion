/* simplest version of calculator */
%{
#include <stdio.h>
#include <stdlib.h>
int yylex(void);           /* declarar el lexer */
int yyerror(char *s);      /* declarar yyerror para evitar warning */
%}

/* declare tokens */
%token NUMBER
%token ADD SUB MUL DIV ABS
%token AND OR
%token EOL

%left OR
%left AND
%left ADD SUB
%left MUL DIV

%%

calclist: /* nothing */
    | calclist exp EOL { printf("= %d\n", $2); } /* EOL is end of an expression */
    | calclist EOL       /* aceptar línea vacía o comentario */
    ;

exp: factor
    { $$ = $1; }
    | exp ADD factor { $$ = $1 + $3; }
    | exp SUB factor { $$ = $1 - $3; }
    | exp AND factor { $$ = $1 & $3; }
    | exp OR factor  { $$ = $1 | $3; }
    ;

factor: term
    { $$ = $1; }  /* default $$ = $1 */
    | factor MUL term { $$ = $1 * $3; }
    | factor DIV term { $$ = $1 / $3; }
    ;

term: NUMBER { $$ = $1; }  /* default $$ = $1 */
    | ABS term { $$ = $2 >= 0 ? $2 : -$2; }
    ;

%%

int main(int argc, char **argv)
{
    return yyparse();
}

int yyerror(char *s)
{
    fprintf(stderr, "error: %s\n", s);
    return 0;
}
