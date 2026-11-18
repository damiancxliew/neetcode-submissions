class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for _str in strs:
            temp = [ord(char) for char in _str]
            res.append(str(temp))
        return ";".join(res)

    def decode(self, s: str) -> List[str]:
        lst = s.split(';')
        if not lst or lst[0] == "":
            return []
        for i in range(len(lst)):
            temp = lst[i].split(", ")
            temp_res = ""
            for value in temp:
                # print(value)
                value = value.strip("[")
                value = value.strip("]")
                # print(value)
                if value:
                    temp_res += chr(int(value))
            lst[i] = temp_res
        return lst
