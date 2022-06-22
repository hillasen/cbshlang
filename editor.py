import sys

from PythonRun import parser
from PythonRun import tokenizer
from PythonRun import runner

code = ""

while(True):
    text = input()
    if(text == "실행"):
        break
    else:
        code += text
        code += '\n'

pa = parser.Parser(code)
to = tokenizer.Tokenizer(pa.getParsed())
to.doTokenize()
ru = runner.Runner(to.tokenized)
ru.run()