grammar LAGrammar;

programa: declaracoes 'algoritmo' corpo 'fim_algoritmo';

declaracoes: (decl_local_global ';')*;

decl_local_global: declaracao_local | declaracao_global;

declaracao_local: 'declare' declaracao_variavel;
declaracao_global: 'declare' declaracoes_variaveis;

declaracoes_variaveis: 'declare' declaracao_variavel (',' declaracao_variavel)* 'fim_declare'?;

declaracao_variavel: identificadores DOISPONTOS tipo;

identificadores: identificador (',' identificador)*;

corpo: (declaracao_local | comandos)*;

comandos: comando (comando)*;

comando: leia_cmd
       | escreva_cmd
       | atribuicao_cmd
       | chamada_funcao_cmd
       | cmd_condicional
       | cmd_enquanto
       | cmd_para;

leia_cmd: 'leia' '(' identificadores ')';

escreva_cmd: 'escreva' '(' expressao (',' expressao)* ')';

atribuicao_cmd: identificador '<-' expressao;

chamada_funcao_cmd: identificador '(' argumentos? ')';

argumentos: expressao (',' expressao)*;

cmd_condicional: 'se' expressao 'entao' comandos ('senao' comandos)? 'fim_se';

cmd_enquanto: 'enquanto' expressao 'faca' comandos 'fim_enquanto';

cmd_para: 'para' identificador 'de' expressao 'ate' expressao ('passo' expressao)? 'faca' comandos 'fim_para';

expressao: literal
         | NUM_INT
         | NUM_REAL
         | identificador
         | '(' expressao ')'
         | expressao ('+'|'-'|'*'|'/') expressao
         | expressao logico expressao;

literal: CADEIA | LOGICO | IDENT;

tipo: 'literal' | 'inteiro' | 'real' | 'logico' | 'registro' | 'ponteiro' | IDENT;

identificador: IDENT ('.' IDENT)* dimensao?;

dimensao: ('[' expressao ']')+;

valor: NUM_INT | NUM_REAL | literal;

ponteiro: '&';

logico: 'e' | 'ou';

registro: 'registro' (declaracao_variavel)* 'fim_registro';

DOISPONTOS: ':';

IDENT: [a-zA-Z] [a-zA-Z0-9_]*;

CADEIA: '"' (~('\n'|'"'))* '"';

LOGICO: 'verdadeiro' | 'falso';

NUM_INT: [0-9]+;

NUM_REAL: [0-9]+'.'[0-9]+;

WS: [ \t\r\n]+ -> skip;

COMMENTS: '{' ~('}')* '}' -> skip;

ErrorChar: .;
