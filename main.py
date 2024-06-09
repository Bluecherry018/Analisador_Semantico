import sys
from antlr4 import *
from LAGrammarLexer import LAGrammarLexer
from LAGrammarParser import LAGrammarParser
from LAGrammarListener import LAGrammarListener
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener

class SemanticErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
        
    def add_error(self, line, msg):
        if (line, msg) not in self.errors:
            self.errors.append((line, msg))

    def has_errors(self):
        return len(self.errors) > 0

    def print_errors(self, output_file):
        self.errors.sort(key=lambda x: x[0])  # Ordena os erros pela linha
        with open(output_file, 'w') as f:
            for error in self.errors:
                f.write(f"Linha {error[0]}: {error[1]}\n")
            f.write("Fim da compilação\n")

class LAGrammarSemanticAnalyzer(LAGrammarListener):
    def __init__(self, error_listener):
        super().__init__()
        self.symbol_table = {}
        self.current_scope = "global"
        self.error_listener = error_listener

    def enterDeclaracoes_variaveis(self, ctx: LAGrammarParser.Declaracoes_variaveisContext):
        for declaracao_var in ctx.declaracao_variavel():
            self.enterDeclaracao_variavel(declaracao_var)

    def enterDeclaracao_variavel(self, ctx: LAGrammarParser.Declaracao_variavelContext):
        tipo = ctx.tipo().getText()
        identificadores = ctx.identificadores().identificador()

        for identificador in identificadores:
            nome = identificador.getText()
            if nome in self.symbol_table:
                self.error_listener.add_error(identificador.start.line, f"identificador {nome} já declarado anteriormente")
            else:
                self.symbol_table[nome] = tipo

    def enterIdentificadores(self, ctx: LAGrammarParser.IdentificadoresContext):
        for identificador in ctx.identificador():
            self.enterIdentificador(identificador)

    def enterIdentificador(self, ctx: LAGrammarParser.IdentificadorContext):
        nome = ctx.getText()
        if nome not in self.symbol_table:
            self.error_listener.add_error(ctx.start.line, f"identificador {nome} não declarado")

    def enterTipo(self, ctx: LAGrammarParser.TipoContext):
        nome = ctx.getText()
        if nome not in ['literal', 'inteiro', 'real', 'logico', 'registro', 'ponteiro']:
            tipo_formatado = nome if nome != "literal" else nome
            self.error_listener.add_error(ctx.start.line, f"tipo {tipo_formatado} não declarado")

    def exitAtribuicao_cmd(self, ctx: LAGrammarParser.Atribuicao_cmdContext):
        identificador = ctx.identificador().getText()
        tipo_variavel = self.symbol_table.get(identificador)
        tipo_expressao = self.get_tipo_expressao(ctx.expressao())

        if tipo_variavel and tipo_expressao and not self.tipo_compativel(tipo_variavel, tipo_expressao):
            self.error_listener.add_error(ctx.identificador().start.line, f"atribuição não compatível para {identificador}")

    def get_tipo_expressao(self, ctx: LAGrammarParser.ExpressaoContext):
        if ctx.literal():
            return "literal"
        elif ctx.NUM_INT():
            return "inteiro"
        elif ctx.NUM_REAL():
            return "real"
        elif ctx.identificador():
            return self.symbol_table.get(ctx.identificador().getText())
        elif ctx.getChild(1) and (ctx.getChild(1).getText() in ['+', '-', '*', '/']):
            tipo_expr1 = self.get_tipo_expressao(ctx.expressao(0))
            tipo_expr2 = self.get_tipo_expressao(ctx.expressao(1))
            if tipo_expr1 == tipo_expr2:
                return tipo_expr1
            else:
                return "tipo_indefinido"
        return "tipo_indefinido"

    def tipo_compativel(self, tipo_var, tipo_expr):
        if tipo_var == tipo_expr:
            return True
        if (tipo_var == "real" and tipo_expr == "inteiro") or (tipo_var == "inteiro" and tipo_expr == "real"):
            return True
        return False

    def print_errors(self, output_file):
        self.error_listener.print_errors(output_file)

def main(input_file, output_file):
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = LAGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LAGrammarParser(stream)
    
    # Remover o listener de erros padrão e adicionar o nosso customizado
    parser.removeErrorListeners()
    error_listener = SemanticErrorListener()
    parser.addErrorListener(error_listener)
    
    tree = parser.programa()

    analyzer = LAGrammarSemanticAnalyzer(error_listener)
    walker = ParseTreeWalker()
    walker.walk(analyzer, tree)

    analyzer.print_errors(output_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: Python3 main.py entrada.txt saida.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
