from typing import List


def encode(strs: List[str]) -> str:
    return "".join([f"{len(s)}|{s}" for s in strs])

def decode(str:str):
    if not str:
        return []
    
print(decode(encode([])))

print(encode([""]))