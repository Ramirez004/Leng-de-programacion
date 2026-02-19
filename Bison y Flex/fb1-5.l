%{
#include "fb1-5.tab.h"
#include <stdlib.h>
%}

%%
0[xX][a-fA-F0-9]+ {
    yylval = strtol(yytext, NULL, 16);
    return NUMBER;
}


[0-9]+        { yylval = atoi(yytext); return NUMBER; }

"+"           { return ADD; }
"-"           { return SUB; }
"*"           { return MUL; }
"/"           { return DIV; }
"|"           { return ABS; }

"AND"         { return AND; }
"OR"          { return OR; }

\n            { return EOL; }

[ \t]+        { }

\/\/.*\n      { return EOL; }

.             { }

%%

int yywrap(void) { return 1; }
