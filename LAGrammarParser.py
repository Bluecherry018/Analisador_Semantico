# Generated from LAGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,257,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,5,1,65,8,1,10,1,12,1,68,
        9,1,1,2,1,2,3,2,72,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,
        5,84,8,5,10,5,12,5,87,9,5,1,5,3,5,90,8,5,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,5,7,99,8,7,10,7,12,7,102,9,7,1,8,1,8,5,8,106,8,8,10,8,12,8,109,
        9,8,1,9,1,9,5,9,113,8,9,10,9,12,9,116,9,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,125,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,12,1,12,5,12,137,8,12,10,12,12,12,140,9,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,3,14,151,8,14,1,14,1,14,1,15,1,15,1,
        15,5,15,158,8,15,10,15,12,15,161,9,15,1,16,1,16,1,16,1,16,1,16,1,
        16,3,16,169,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,187,8,18,1,18,1,18,1,18,1,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,202,8,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,211,8,19,10,19,12,19,214,9,
        19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,5,22,223,8,22,10,22,12,22,
        226,9,22,1,22,3,22,229,8,22,1,23,1,23,1,23,1,23,4,23,235,8,23,11,
        23,12,23,236,1,24,1,24,1,24,3,24,242,8,24,1,25,1,25,1,26,1,26,1,
        27,1,27,5,27,250,8,27,10,27,12,27,253,9,27,1,27,1,27,1,27,0,1,38,
        28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,0,4,1,0,24,27,1,0,42,44,2,0,28,33,42,42,1,0,38,
        39,259,0,56,1,0,0,0,2,66,1,0,0,0,4,71,1,0,0,0,6,73,1,0,0,0,8,76,
        1,0,0,0,10,79,1,0,0,0,12,91,1,0,0,0,14,95,1,0,0,0,16,107,1,0,0,0,
        18,110,1,0,0,0,20,124,1,0,0,0,22,126,1,0,0,0,24,131,1,0,0,0,26,143,
        1,0,0,0,28,147,1,0,0,0,30,154,1,0,0,0,32,162,1,0,0,0,34,172,1,0,
        0,0,36,178,1,0,0,0,38,201,1,0,0,0,40,215,1,0,0,0,42,217,1,0,0,0,
        44,219,1,0,0,0,46,234,1,0,0,0,48,241,1,0,0,0,50,243,1,0,0,0,52,245,
        1,0,0,0,54,247,1,0,0,0,56,57,3,2,1,0,57,58,5,1,0,0,58,59,3,16,8,
        0,59,60,5,2,0,0,60,1,1,0,0,0,61,62,3,4,2,0,62,63,5,3,0,0,63,65,1,
        0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,
        3,1,0,0,0,68,66,1,0,0,0,69,72,3,6,3,0,70,72,3,8,4,0,71,69,1,0,0,
        0,71,70,1,0,0,0,72,5,1,0,0,0,73,74,5,4,0,0,74,75,3,12,6,0,75,7,1,
        0,0,0,76,77,5,4,0,0,77,78,3,10,5,0,78,9,1,0,0,0,79,80,5,4,0,0,80,
        85,3,12,6,0,81,82,5,5,0,0,82,84,3,12,6,0,83,81,1,0,0,0,84,87,1,0,
        0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,88,90,
        5,6,0,0,89,88,1,0,0,0,89,90,1,0,0,0,90,11,1,0,0,0,91,92,3,14,7,0,
        92,93,5,41,0,0,93,94,3,42,21,0,94,13,1,0,0,0,95,100,3,44,22,0,96,
        97,5,5,0,0,97,99,3,44,22,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,1,
        0,0,0,100,101,1,0,0,0,101,15,1,0,0,0,102,100,1,0,0,0,103,106,3,6,
        3,0,104,106,3,18,9,0,105,103,1,0,0,0,105,104,1,0,0,0,106,109,1,0,
        0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,17,1,0,0,0,109,107,1,0,0,
        0,110,114,3,20,10,0,111,113,3,20,10,0,112,111,1,0,0,0,113,116,1,
        0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,19,1,0,0,0,116,114,1,0,
        0,0,117,125,3,22,11,0,118,125,3,24,12,0,119,125,3,26,13,0,120,125,
        3,28,14,0,121,125,3,32,16,0,122,125,3,34,17,0,123,125,3,36,18,0,
        124,117,1,0,0,0,124,118,1,0,0,0,124,119,1,0,0,0,124,120,1,0,0,0,
        124,121,1,0,0,0,124,122,1,0,0,0,124,123,1,0,0,0,125,21,1,0,0,0,126,
        127,5,7,0,0,127,128,5,8,0,0,128,129,3,14,7,0,129,130,5,9,0,0,130,
        23,1,0,0,0,131,132,5,10,0,0,132,133,5,8,0,0,133,138,3,38,19,0,134,
        135,5,5,0,0,135,137,3,38,19,0,136,134,1,0,0,0,137,140,1,0,0,0,138,
        136,1,0,0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,
        142,5,9,0,0,142,25,1,0,0,0,143,144,3,44,22,0,144,145,5,11,0,0,145,
        146,3,38,19,0,146,27,1,0,0,0,147,148,3,44,22,0,148,150,5,8,0,0,149,
        151,3,30,15,0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,
        153,5,9,0,0,153,29,1,0,0,0,154,159,3,38,19,0,155,156,5,5,0,0,156,
        158,3,38,19,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,
        160,1,0,0,0,160,31,1,0,0,0,161,159,1,0,0,0,162,163,5,12,0,0,163,
        164,3,38,19,0,164,165,5,13,0,0,165,168,3,18,9,0,166,167,5,14,0,0,
        167,169,3,18,9,0,168,166,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,
        170,171,5,15,0,0,171,33,1,0,0,0,172,173,5,16,0,0,173,174,3,38,19,
        0,174,175,5,17,0,0,175,176,3,18,9,0,176,177,5,18,0,0,177,35,1,0,
        0,0,178,179,5,19,0,0,179,180,3,44,22,0,180,181,5,20,0,0,181,182,
        3,38,19,0,182,183,5,21,0,0,183,186,3,38,19,0,184,185,5,22,0,0,185,
        187,3,38,19,0,186,184,1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,
        189,5,17,0,0,189,190,3,18,9,0,190,191,5,23,0,0,191,37,1,0,0,0,192,
        193,6,19,-1,0,193,202,3,40,20,0,194,202,5,45,0,0,195,202,5,46,0,
        0,196,202,3,44,22,0,197,198,5,8,0,0,198,199,3,38,19,0,199,200,5,
        9,0,0,200,202,1,0,0,0,201,192,1,0,0,0,201,194,1,0,0,0,201,195,1,
        0,0,0,201,196,1,0,0,0,201,197,1,0,0,0,202,212,1,0,0,0,203,204,10,
        2,0,0,204,205,7,0,0,0,205,211,3,38,19,3,206,207,10,1,0,0,207,208,
        3,52,26,0,208,209,3,38,19,2,209,211,1,0,0,0,210,203,1,0,0,0,210,
        206,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,
        39,1,0,0,0,214,212,1,0,0,0,215,216,7,1,0,0,216,41,1,0,0,0,217,218,
        7,2,0,0,218,43,1,0,0,0,219,224,5,42,0,0,220,221,5,34,0,0,221,223,
        5,42,0,0,222,220,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,
        1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,227,229,3,46,23,0,228,227,
        1,0,0,0,228,229,1,0,0,0,229,45,1,0,0,0,230,231,5,35,0,0,231,232,
        3,38,19,0,232,233,5,36,0,0,233,235,1,0,0,0,234,230,1,0,0,0,235,236,
        1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,47,1,0,0,0,238,242,5,
        45,0,0,239,242,5,46,0,0,240,242,3,40,20,0,241,238,1,0,0,0,241,239,
        1,0,0,0,241,240,1,0,0,0,242,49,1,0,0,0,243,244,5,37,0,0,244,51,1,
        0,0,0,245,246,7,3,0,0,246,53,1,0,0,0,247,251,5,32,0,0,248,250,3,
        12,6,0,249,248,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,
        0,0,0,252,254,1,0,0,0,253,251,1,0,0,0,254,255,5,40,0,0,255,55,1,
        0,0,0,22,66,71,85,89,100,105,107,114,124,138,150,159,168,186,201,
        210,212,224,228,236,241,251
    ]

class LAGrammarParser ( Parser ):

    grammarFileName = "LAGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'algoritmo'", "'fim_algoritmo'", "';'", 
                     "'declare'", "','", "'fim_declare'", "'leia'", "'('", 
                     "')'", "'escreva'", "'<-'", "'se'", "'entao'", "'senao'", 
                     "'fim_se'", "'enquanto'", "'faca'", "'fim_enquanto'", 
                     "'para'", "'de'", "'ate'", "'passo'", "'fim_para'", 
                     "'+'", "'-'", "'*'", "'/'", "'literal'", "'inteiro'", 
                     "'real'", "'logico'", "'registro'", "'ponteiro'", "'.'", 
                     "'['", "']'", "'&'", "'e'", "'ou'", "'fim_registro'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DOISPONTOS", "IDENT", "CADEIA", "LOGICO", 
                      "NUM_INT", "NUM_REAL", "WS", "COMMENTS", "ErrorChar" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_decl_local_global = 2
    RULE_declaracao_local = 3
    RULE_declaracao_global = 4
    RULE_declaracoes_variaveis = 5
    RULE_declaracao_variavel = 6
    RULE_identificadores = 7
    RULE_corpo = 8
    RULE_comandos = 9
    RULE_comando = 10
    RULE_leia_cmd = 11
    RULE_escreva_cmd = 12
    RULE_atribuicao_cmd = 13
    RULE_chamada_funcao_cmd = 14
    RULE_argumentos = 15
    RULE_cmd_condicional = 16
    RULE_cmd_enquanto = 17
    RULE_cmd_para = 18
    RULE_expressao = 19
    RULE_literal = 20
    RULE_tipo = 21
    RULE_identificador = 22
    RULE_dimensao = 23
    RULE_valor = 24
    RULE_ponteiro = 25
    RULE_logico = 26
    RULE_registro = 27

    ruleNames =  [ "programa", "declaracoes", "decl_local_global", "declaracao_local", 
                   "declaracao_global", "declaracoes_variaveis", "declaracao_variavel", 
                   "identificadores", "corpo", "comandos", "comando", "leia_cmd", 
                   "escreva_cmd", "atribuicao_cmd", "chamada_funcao_cmd", 
                   "argumentos", "cmd_condicional", "cmd_enquanto", "cmd_para", 
                   "expressao", "literal", "tipo", "identificador", "dimensao", 
                   "valor", "ponteiro", "logico", "registro" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    DOISPONTOS=41
    IDENT=42
    CADEIA=43
    LOGICO=44
    NUM_INT=45
    NUM_REAL=46
    WS=47
    COMMENTS=48
    ErrorChar=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(LAGrammarParser.DeclaracoesContext,0)


        def corpo(self):
            return self.getTypedRuleContext(LAGrammarParser.CorpoContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = LAGrammarParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.declaracoes()
            self.state = 57
            self.match(LAGrammarParser.T__0)
            self.state = 58
            self.corpo()
            self.state = 59
            self.match(LAGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_local_global(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.Decl_local_globalContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.Decl_local_globalContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)




    def declaracoes(self):

        localctx = LAGrammarParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 61
                self.decl_local_global()
                self.state = 62
                self.match(LAGrammarParser.T__2)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_local_globalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_local(self):
            return self.getTypedRuleContext(LAGrammarParser.Declaracao_localContext,0)


        def declaracao_global(self):
            return self.getTypedRuleContext(LAGrammarParser.Declaracao_globalContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_decl_local_global

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_local_global" ):
                listener.enterDecl_local_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_local_global" ):
                listener.exitDecl_local_global(self)




    def decl_local_global(self):

        localctx = LAGrammarParser.Decl_local_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_local_global)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.declaracao_local()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.declaracao_global()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_localContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_variavel(self):
            return self.getTypedRuleContext(LAGrammarParser.Declaracao_variavelContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_declaracao_local

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_local" ):
                listener.enterDeclaracao_local(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_local" ):
                listener.exitDeclaracao_local(self)




    def declaracao_local(self):

        localctx = LAGrammarParser.Declaracao_localContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao_local)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(LAGrammarParser.T__3)
            self.state = 74
            self.declaracao_variavel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_globalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes_variaveis(self):
            return self.getTypedRuleContext(LAGrammarParser.Declaracoes_variaveisContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_declaracao_global

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_global" ):
                listener.enterDeclaracao_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_global" ):
                listener.exitDeclaracao_global(self)




    def declaracao_global(self):

        localctx = LAGrammarParser.Declaracao_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracao_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(LAGrammarParser.T__3)
            self.state = 77
            self.declaracoes_variaveis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracoes_variaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_variavel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.Declaracao_variavelContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.Declaracao_variavelContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_declaracoes_variaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes_variaveis" ):
                listener.enterDeclaracoes_variaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes_variaveis" ):
                listener.exitDeclaracoes_variaveis(self)




    def declaracoes_variaveis(self):

        localctx = LAGrammarParser.Declaracoes_variaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracoes_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(LAGrammarParser.T__3)
            self.state = 80
            self.declaracao_variavel()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 81
                self.match(LAGrammarParser.T__4)
                self.state = 82
                self.declaracao_variavel()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 88
                self.match(LAGrammarParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_variavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificadores(self):
            return self.getTypedRuleContext(LAGrammarParser.IdentificadoresContext,0)


        def DOISPONTOS(self):
            return self.getToken(LAGrammarParser.DOISPONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(LAGrammarParser.TipoContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_declaracao_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_variavel" ):
                listener.enterDeclaracao_variavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_variavel" ):
                listener.exitDeclaracao_variavel(self)




    def declaracao_variavel(self):

        localctx = LAGrammarParser.Declaracao_variavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracao_variavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.identificadores()
            self.state = 92
            self.match(LAGrammarParser.DOISPONTOS)
            self.state = 93
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentificadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.IdentificadorContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.IdentificadorContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_identificadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificadores" ):
                listener.enterIdentificadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificadores" ):
                listener.exitIdentificadores(self)




    def identificadores(self):

        localctx = LAGrammarParser.IdentificadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_identificadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.identificador()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 96
                self.match(LAGrammarParser.T__4)
                self.state = 97
                self.identificador()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CorpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_local(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.Declaracao_localContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.Declaracao_localContext,i)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ComandosContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ComandosContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_corpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorpo" ):
                listener.enterCorpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorpo" ):
                listener.exitCorpo(self)




    def corpo(self):

        localctx = LAGrammarParser.CorpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_corpo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398047106192) != 0):
                self.state = 105
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 103
                    self.declaracao_local()
                    pass
                elif token in [7, 10, 12, 16, 19, 42]:
                    self.state = 104
                    self.comandos()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ComandoContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)




    def comandos(self):

        localctx = LAGrammarParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comandos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.comando()
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 111
                    self.comando() 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leia_cmd(self):
            return self.getTypedRuleContext(LAGrammarParser.Leia_cmdContext,0)


        def escreva_cmd(self):
            return self.getTypedRuleContext(LAGrammarParser.Escreva_cmdContext,0)


        def atribuicao_cmd(self):
            return self.getTypedRuleContext(LAGrammarParser.Atribuicao_cmdContext,0)


        def chamada_funcao_cmd(self):
            return self.getTypedRuleContext(LAGrammarParser.Chamada_funcao_cmdContext,0)


        def cmd_condicional(self):
            return self.getTypedRuleContext(LAGrammarParser.Cmd_condicionalContext,0)


        def cmd_enquanto(self):
            return self.getTypedRuleContext(LAGrammarParser.Cmd_enquantoContext,0)


        def cmd_para(self):
            return self.getTypedRuleContext(LAGrammarParser.Cmd_paraContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = LAGrammarParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comando)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.leia_cmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.escreva_cmd()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.atribuicao_cmd()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.chamada_funcao_cmd()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.cmd_condicional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 122
                self.cmd_enquanto()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.cmd_para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Leia_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificadores(self):
            return self.getTypedRuleContext(LAGrammarParser.IdentificadoresContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_leia_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeia_cmd" ):
                listener.enterLeia_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeia_cmd" ):
                listener.exitLeia_cmd(self)




    def leia_cmd(self):

        localctx = LAGrammarParser.Leia_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_leia_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(LAGrammarParser.T__6)
            self.state = 127
            self.match(LAGrammarParser.T__7)
            self.state = 128
            self.identificadores()
            self.state = 129
            self.match(LAGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Escreva_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_escreva_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscreva_cmd" ):
                listener.enterEscreva_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscreva_cmd" ):
                listener.exitEscreva_cmd(self)




    def escreva_cmd(self):

        localctx = LAGrammarParser.Escreva_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_escreva_cmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(LAGrammarParser.T__9)
            self.state = 132
            self.match(LAGrammarParser.T__7)
            self.state = 133
            self.expressao(0)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 134
                self.match(LAGrammarParser.T__4)
                self.state = 135
                self.expressao(0)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(LAGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atribuicao_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(LAGrammarParser.IdentificadorContext,0)


        def expressao(self):
            return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_atribuicao_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao_cmd" ):
                listener.enterAtribuicao_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao_cmd" ):
                listener.exitAtribuicao_cmd(self)




    def atribuicao_cmd(self):

        localctx = LAGrammarParser.Atribuicao_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_atribuicao_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.identificador()
            self.state = 144
            self.match(LAGrammarParser.T__10)
            self.state = 145
            self.expressao(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chamada_funcao_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(LAGrammarParser.IdentificadorContext,0)


        def argumentos(self):
            return self.getTypedRuleContext(LAGrammarParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_chamada_funcao_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamada_funcao_cmd" ):
                listener.enterChamada_funcao_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamada_funcao_cmd" ):
                listener.exitChamada_funcao_cmd(self)




    def chamada_funcao_cmd(self):

        localctx = LAGrammarParser.Chamada_funcao_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_chamada_funcao_cmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.identificador()
            self.state = 148
            self.match(LAGrammarParser.T__7)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 136339441844480) != 0):
                self.state = 149
                self.argumentos()


            self.state = 152
            self.match(LAGrammarParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)




    def argumentos(self):

        localctx = LAGrammarParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.expressao(0)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 155
                self.match(LAGrammarParser.T__4)
                self.state = 156
                self.expressao(0)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_condicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ComandosContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ComandosContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_cmd_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_condicional" ):
                listener.enterCmd_condicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_condicional" ):
                listener.exitCmd_condicional(self)




    def cmd_condicional(self):

        localctx = LAGrammarParser.Cmd_condicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cmd_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(LAGrammarParser.T__11)
            self.state = 163
            self.expressao(0)
            self.state = 164
            self.match(LAGrammarParser.T__12)
            self.state = 165
            self.comandos()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 166
                self.match(LAGrammarParser.T__13)
                self.state = 167
                self.comandos()


            self.state = 170
            self.match(LAGrammarParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_enquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,0)


        def comandos(self):
            return self.getTypedRuleContext(LAGrammarParser.ComandosContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_cmd_enquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_enquanto" ):
                listener.enterCmd_enquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_enquanto" ):
                listener.exitCmd_enquanto(self)




    def cmd_enquanto(self):

        localctx = LAGrammarParser.Cmd_enquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cmd_enquanto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(LAGrammarParser.T__15)
            self.state = 173
            self.expressao(0)
            self.state = 174
            self.match(LAGrammarParser.T__16)
            self.state = 175
            self.comandos()
            self.state = 176
            self.match(LAGrammarParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(LAGrammarParser.IdentificadorContext,0)


        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,i)


        def comandos(self):
            return self.getTypedRuleContext(LAGrammarParser.ComandosContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_cmd_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_para" ):
                listener.enterCmd_para(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_para" ):
                listener.exitCmd_para(self)




    def cmd_para(self):

        localctx = LAGrammarParser.Cmd_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cmd_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(LAGrammarParser.T__18)
            self.state = 179
            self.identificador()
            self.state = 180
            self.match(LAGrammarParser.T__19)
            self.state = 181
            self.expressao(0)
            self.state = 182
            self.match(LAGrammarParser.T__20)
            self.state = 183
            self.expressao(0)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 184
                self.match(LAGrammarParser.T__21)
                self.state = 185
                self.expressao(0)


            self.state = 188
            self.match(LAGrammarParser.T__16)
            self.state = 189
            self.comandos()
            self.state = 190
            self.match(LAGrammarParser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(LAGrammarParser.LiteralContext,0)


        def NUM_INT(self):
            return self.getToken(LAGrammarParser.NUM_INT, 0)

        def NUM_REAL(self):
            return self.getToken(LAGrammarParser.NUM_REAL, 0)

        def identificador(self):
            return self.getTypedRuleContext(LAGrammarParser.IdentificadorContext,0)


        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,i)


        def logico(self):
            return self.getTypedRuleContext(LAGrammarParser.LogicoContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LAGrammarParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expressao, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 193
                self.literal()
                pass

            elif la_ == 2:
                self.state = 194
                self.match(LAGrammarParser.NUM_INT)
                pass

            elif la_ == 3:
                self.state = 195
                self.match(LAGrammarParser.NUM_REAL)
                pass

            elif la_ == 4:
                self.state = 196
                self.identificador()
                pass

            elif la_ == 5:
                self.state = 197
                self.match(LAGrammarParser.T__7)
                self.state = 198
                self.expressao(0)
                self.state = 199
                self.match(LAGrammarParser.T__8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = LAGrammarParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 203
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 204
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 205
                        self.expressao(3)
                        pass

                    elif la_ == 2:
                        localctx = LAGrammarParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 206
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 207
                        self.logico()
                        self.state = 208
                        self.expressao(2)
                        pass

             
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self):
            return self.getToken(LAGrammarParser.CADEIA, 0)

        def LOGICO(self):
            return self.getToken(LAGrammarParser.LOGICO, 0)

        def IDENT(self):
            return self.getToken(LAGrammarParser.IDENT, 0)

        def getRuleIndex(self):
            return LAGrammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = LAGrammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577728) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAGrammarParser.IDENT, 0)

        def getRuleIndex(self):
            return LAGrammarParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = LAGrammarParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4414957944832) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentificadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(LAGrammarParser.IDENT)
            else:
                return self.getToken(LAGrammarParser.IDENT, i)

        def dimensao(self):
            return self.getTypedRuleContext(LAGrammarParser.DimensaoContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_identificador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)




    def identificador(self):

        localctx = LAGrammarParser.IdentificadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_identificador)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(LAGrammarParser.IDENT)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 220
                    self.match(LAGrammarParser.T__33)
                    self.state = 221
                    self.match(LAGrammarParser.IDENT) 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 227
                self.dimensao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_dimensao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensao" ):
                listener.enterDimensao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensao" ):
                listener.exitDimensao(self)




    def dimensao(self):

        localctx = LAGrammarParser.DimensaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_dimensao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 230
                    self.match(LAGrammarParser.T__34)
                    self.state = 231
                    self.expressao(0)
                    self.state = 232
                    self.match(LAGrammarParser.T__35)

                else:
                    raise NoViableAltException(self)
                self.state = 236 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(LAGrammarParser.NUM_INT, 0)

        def NUM_REAL(self):
            return self.getToken(LAGrammarParser.NUM_REAL, 0)

        def literal(self):
            return self.getTypedRuleContext(LAGrammarParser.LiteralContext,0)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = LAGrammarParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_valor)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(LAGrammarParser.NUM_INT)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(LAGrammarParser.NUM_REAL)
                pass
            elif token in [42, 43, 44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PonteiroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LAGrammarParser.RULE_ponteiro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPonteiro" ):
                listener.enterPonteiro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPonteiro" ):
                listener.exitPonteiro(self)




    def ponteiro(self):

        localctx = LAGrammarParser.PonteiroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ponteiro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(LAGrammarParser.T__36)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LAGrammarParser.RULE_logico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogico" ):
                listener.enterLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogico" ):
                listener.exitLogico(self)




    def logico(self):

        localctx = LAGrammarParser.LogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegistroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_variavel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAGrammarParser.Declaracao_variavelContext)
            else:
                return self.getTypedRuleContext(LAGrammarParser.Declaracao_variavelContext,i)


        def getRuleIndex(self):
            return LAGrammarParser.RULE_registro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegistro" ):
                listener.enterRegistro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegistro" ):
                listener.exitRegistro(self)




    def registro(self):

        localctx = LAGrammarParser.RegistroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_registro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(LAGrammarParser.T__31)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 248
                self.declaracao_variavel()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 254
            self.match(LAGrammarParser.T__39)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




