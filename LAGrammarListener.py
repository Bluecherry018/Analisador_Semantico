# Generated from LAGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LAGrammarParser import LAGrammarParser
else:
    from LAGrammarParser import LAGrammarParser

# This class defines a complete listener for a parse tree produced by LAGrammarParser.
class LAGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by LAGrammarParser#programa.
    def enterPrograma(self, ctx:LAGrammarParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#programa.
    def exitPrograma(self, ctx:LAGrammarParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracoes.
    def enterDeclaracoes(self, ctx:LAGrammarParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracoes.
    def exitDeclaracoes(self, ctx:LAGrammarParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#decl_local_global.
    def enterDecl_local_global(self, ctx:LAGrammarParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#decl_local_global.
    def exitDecl_local_global(self, ctx:LAGrammarParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:LAGrammarParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:LAGrammarParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:LAGrammarParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:LAGrammarParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracoes_variaveis.
    def enterDeclaracoes_variaveis(self, ctx:LAGrammarParser.Declaracoes_variaveisContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracoes_variaveis.
    def exitDeclaracoes_variaveis(self, ctx:LAGrammarParser.Declaracoes_variaveisContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#declaracao_variavel.
    def enterDeclaracao_variavel(self, ctx:LAGrammarParser.Declaracao_variavelContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#declaracao_variavel.
    def exitDeclaracao_variavel(self, ctx:LAGrammarParser.Declaracao_variavelContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#identificadores.
    def enterIdentificadores(self, ctx:LAGrammarParser.IdentificadoresContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#identificadores.
    def exitIdentificadores(self, ctx:LAGrammarParser.IdentificadoresContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#corpo.
    def enterCorpo(self, ctx:LAGrammarParser.CorpoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#corpo.
    def exitCorpo(self, ctx:LAGrammarParser.CorpoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#comandos.
    def enterComandos(self, ctx:LAGrammarParser.ComandosContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#comandos.
    def exitComandos(self, ctx:LAGrammarParser.ComandosContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#comando.
    def enterComando(self, ctx:LAGrammarParser.ComandoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#comando.
    def exitComando(self, ctx:LAGrammarParser.ComandoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#leia_cmd.
    def enterLeia_cmd(self, ctx:LAGrammarParser.Leia_cmdContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#leia_cmd.
    def exitLeia_cmd(self, ctx:LAGrammarParser.Leia_cmdContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#escreva_cmd.
    def enterEscreva_cmd(self, ctx:LAGrammarParser.Escreva_cmdContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#escreva_cmd.
    def exitEscreva_cmd(self, ctx:LAGrammarParser.Escreva_cmdContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#atribuicao_cmd.
    def enterAtribuicao_cmd(self, ctx:LAGrammarParser.Atribuicao_cmdContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#atribuicao_cmd.
    def exitAtribuicao_cmd(self, ctx:LAGrammarParser.Atribuicao_cmdContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#chamada_funcao_cmd.
    def enterChamada_funcao_cmd(self, ctx:LAGrammarParser.Chamada_funcao_cmdContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#chamada_funcao_cmd.
    def exitChamada_funcao_cmd(self, ctx:LAGrammarParser.Chamada_funcao_cmdContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#argumentos.
    def enterArgumentos(self, ctx:LAGrammarParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#argumentos.
    def exitArgumentos(self, ctx:LAGrammarParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmd_condicional.
    def enterCmd_condicional(self, ctx:LAGrammarParser.Cmd_condicionalContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmd_condicional.
    def exitCmd_condicional(self, ctx:LAGrammarParser.Cmd_condicionalContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmd_enquanto.
    def enterCmd_enquanto(self, ctx:LAGrammarParser.Cmd_enquantoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmd_enquanto.
    def exitCmd_enquanto(self, ctx:LAGrammarParser.Cmd_enquantoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#cmd_para.
    def enterCmd_para(self, ctx:LAGrammarParser.Cmd_paraContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#cmd_para.
    def exitCmd_para(self, ctx:LAGrammarParser.Cmd_paraContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#expressao.
    def enterExpressao(self, ctx:LAGrammarParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#expressao.
    def exitExpressao(self, ctx:LAGrammarParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#literal.
    def enterLiteral(self, ctx:LAGrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#literal.
    def exitLiteral(self, ctx:LAGrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#tipo.
    def enterTipo(self, ctx:LAGrammarParser.TipoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#tipo.
    def exitTipo(self, ctx:LAGrammarParser.TipoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#identificador.
    def enterIdentificador(self, ctx:LAGrammarParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#identificador.
    def exitIdentificador(self, ctx:LAGrammarParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#dimensao.
    def enterDimensao(self, ctx:LAGrammarParser.DimensaoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#dimensao.
    def exitDimensao(self, ctx:LAGrammarParser.DimensaoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#valor.
    def enterValor(self, ctx:LAGrammarParser.ValorContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#valor.
    def exitValor(self, ctx:LAGrammarParser.ValorContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#ponteiro.
    def enterPonteiro(self, ctx:LAGrammarParser.PonteiroContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#ponteiro.
    def exitPonteiro(self, ctx:LAGrammarParser.PonteiroContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#logico.
    def enterLogico(self, ctx:LAGrammarParser.LogicoContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#logico.
    def exitLogico(self, ctx:LAGrammarParser.LogicoContext):
        pass


    # Enter a parse tree produced by LAGrammarParser#registro.
    def enterRegistro(self, ctx:LAGrammarParser.RegistroContext):
        pass

    # Exit a parse tree produced by LAGrammarParser#registro.
    def exitRegistro(self, ctx:LAGrammarParser.RegistroContext):
        pass



del LAGrammarParser