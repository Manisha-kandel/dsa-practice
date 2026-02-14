'''
271. Encode and Decode strings
'''

class Solution:
    '''
    input: ['hel#lo', 'world']
    enc = '6#hel#lo5#world'
    dec = ['hel#lo', 'world']
    '''
    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        # 6#hel#lo5#world --> ['hel#lo', 'world']
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            start = j + 1
            end = start + length
            dec.append(s[start: end])
            print(dec)
            i = end
        print(dec)
        return dec
            

         


