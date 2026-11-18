class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for _str in strs:
            temp = "".join(sorted(list(_str)))
            str_dict[temp].append(_str)
        return list(str_dict.values())
        

            
