class Solution(object):
    def groupAnagrams(self, strs):
        # mapping charCount to list of Anagrams
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

# Time Complexity: O(N × K)
# Space Complexity: O(N × K)