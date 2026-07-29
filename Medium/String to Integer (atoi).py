class Solution:
    def myAtoi(self, s: str) -> int:
        st=s.strip()
        sign= -1 if st.startswith("-") else 1
        l=[]
        if st.startswith(("-","+")):
            st=st[1:]
        for ch in st:
            if not ch.isdigit():
                break
            l.append(ch)
        if not l:
            return 0
        num=int("".join(map(str,l)))
        num*=sign
        if num>2**31-1:
            num=2**31-1
        elif num<(-2**31):
            num=(-2**31)
        return num
        

        
