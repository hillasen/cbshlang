class Tokenizer:
    def __init__(self, parsed_code):
        self.parsed_code = parsed_code
        self.tokenized = []

    def __doCalculate(self, code):
        nums = {"북" : "+1", "남" : "-1"}
        opers = {"물":"*", "수":"/", "정":"%", "화":"+", "생":"-"}
        calc = "("
        is_var = False
        name_var = ""
        for i in code:
            if (i in opers):
                calc += ")"
                calc += opers[i]
                calc += "("
            if (i in nums):
                calc += nums[i]
            if (is_var and i == '웅'):
                calc += "self.getVariable(\"" + (name_var + "웅") + "\")"
                name_var = ""
                is_var = False
                continue
            if(i == "우"):
                name_var += "우"
                continue
            if (i == "충"):
                calc += "self.getVariable(\"충\")"
                is_var = False
                continue
            if( i == "추"):
                is_var = True
                name_var += "추"

            pass
        calc += ")"
        return calc
    def doTokenize(self):
        now_code = ""
        is_var = False
        is_calc = False
        for i in range(len(self.parsed_code)):
            t = self.parsed_code[i]
            now_code = now_code + t
            if (t == 'f'):
                if(is_calc):
                    self.tokenized.append(["calc", self.__doCalculate(now_code)])
                self.tokenized.append(["f", "f"])
                now_code = ""
                is_calc = False
            if (is_var and t == '웅' and is_calc == False):
                self.tokenized.append(["var", now_code])
                now_var = False
                is_calc = True
                now_code = ""
                continue
            if (t == "충" and is_calc == False):
                self.tokenized.append(["var", now_code])
                now_code = ""
                is_calc = True
                continue
            if( t == "추" and is_calc == False):
                is_var = True
            if(t == "곽"):
                is_calc = False
                self.tokenized.append(["print", "num"])
                now_code = ""
            if (t == "꽉"):
                is_calc = False
                self.tokenized.append(["print", "chr"])
                now_code = ""
            if (t == "학" and self.parsed_code[i-1] != "화" and  self.parsed_code[i-1] != "수"):
                is_calc = False
                self.tokenized.append(["input", "input"])
                now_code = ""


