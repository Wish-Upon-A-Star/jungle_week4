class Solution:
    def letterCombinations(self,digits: str):
        outputs=[]
        def back(str,output):
            for i in range(len(str)):
                strs =[]
                if str[i] == "2":
                    strs="abc"
                elif str[i]=="3":
                    strs="def"
                elif str[i]=="4":
                    strs="ghi"
                elif str[i]=="5":
                    strs="jkl"
                elif str[i]=="6":
                    strs="mno"
                elif str[i]=="7":
                    strs="pqrs"
                elif str[i]=="8":
                    strs="tuv"
                elif str[i]=="9":
                    strs="wxyz"

                for j in range(len(strs)):
                    output.append(strs[j])
                    back(str[i+1:],output)
                    if len(output)==len(digits):
                            add=''.join(output)


                            outputs.append(add)
                    output.pop()

        back(digits,[])
        return outputs