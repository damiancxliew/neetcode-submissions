class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for _str in strs:
            temp = "".join(sorted(list(_str)))
            str_dict[temp].append(_str)
        result = []
        for lst in str_dict.values():
            result.append(lst)
        return result
        

            
