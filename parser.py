def parse(s):
    if(('.' in s) and ('e' in s)):
        exp1 = '0'
        exp1,exp2 = s.split(".")
        if not exp1:
            exp1 = '0'
        if('0'<=exp1<='9'):
         count = 1
         if('e' in exp2):
            for s in exp2:
                if(s == 'e' and count == 1):
                    count+=1
                    return None
                else:
                    count+=1
                    a,b = exp2.split('e')
                    b = int(b)
                    break
         else:
             return None
         result = (exp1+'.'+a+'*10**'+str(b))
         print(result)
         return result
        else:
            return None