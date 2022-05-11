class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        chunks = [s[x:x+k] for x in range(0, len(s), k)]
        lastChunk = len(chunks[len(chunks)-1])

        if lastChunk == k:
            return chunks

        needToFill = k-lastChunk
        toAppend = fill*needToFill
        chunks[len(chunks)-1] = chunks[len(chunks)-1] + toAppend

        return chunks