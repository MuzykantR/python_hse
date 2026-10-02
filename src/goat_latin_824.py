class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        result = []
        for i, w in enumerate(words):
            if w[0] in "aeouiAEOUI":
                new_w = w + "ma" + "a" * (i + 1)
            else:
                new_w = w[1:] + w[0] + "ma" + "a" * (i + 1)
            result.append(new_w)
            
        return ' '.join(result)