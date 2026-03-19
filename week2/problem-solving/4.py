class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret=1
        def rePow(x,n):
            print(n)
            if n==0:return 1
            if n > 0:
                if n==1: return x
                if n%2==1:
                    return rePow(x,int(n/2))*rePow(x,int(n/2+n%2))
                rest=rePow(x,int(n/2))
                return rest*rest

            if n<0:
                if -n==1: return 1/x
                if -n%2==1:
                    print("홀수")
                    return rePow(x,int(n/2))*rePow(x,int(n/2-n%2))
                rest=rePow(x,int(n/2))
                return rest*rest
        ret=rePow(x,n)

        return ret