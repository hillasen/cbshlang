#CBSH LANG
#v1.0.0

import sys

from PythonRun import parser
from PythonRun import tokenizer
from PythonRun import runner

if(len(sys.argv) != 2):
    raise Exception("파일 이름을 입력해 주세요!")
f = open(sys.argv[1])
k = f.read()
f.close()
pa = parser.Parser(k)
to = tokenizer.Tokenizer(pa.getParsed())
to.doTokenize()
ru = runner.Runner(to.tokenized)
ru.run()
