#Medium
#Array / String
class Codec:
    def encode(self, strs: List[str]) -> str:

        delimiter = chr(365)
        return delimiter.join(strs)
    
    def decode(self, s: str) -> List[str]:
        delimiter = chr(365)
        return s.split(delimiter)