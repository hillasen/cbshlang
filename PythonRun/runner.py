class Runner:
    def __init__(self, tokenized):
        self.tokenized = tokenized;
        self.variables = {}
        self.line = 1;
    def getVariable(self, var):
        if( var in self.variables):
            return self.variables[var]
        else:
            raise Exception("" + str(self.line) + "째 줄에 오류 발생! 변수 " + var + " 은 선언되지 않았습니다!")

        return self.variables[var]

    def __setVariable(self, var, value):
        self.variables[var] = value
    def __doNumPrint(self, var):
        print(self.getVariable(var), end='')
    def __doChrPrint(self, var):
        print(chr(self.getVariable(var)), end='')

    def __doInput(self, var):
        self.variables[var] = int(input())


    def run(self):
        for i in range(len(self.tokenized)):

            cmd = self.tokenized[i][0]
            inf = self.tokenized[i][1]
            if(cmd == "var"):
                if(self.tokenized[i+1][0] == "calc"):
                    self.__setVariable(inf, eval(self.tokenized[i+1][1]))
                    pass

                if (self.tokenized[i + 1][0] == "print"):
                    if(self.tokenized[i + 1][1] == "num"):
                        self.__doNumPrint(inf)
                        pass
                    if (self.tokenized[i + 1][1] == "chr"):
                        self.__doChrPrint(inf)
                        pass
                    pass

                if (self.tokenized[i + 1][0] == "input"):
                    self.__doInput(inf)
                    pass
                pass

            if(cmd == "f"):
                self.line += 1;

