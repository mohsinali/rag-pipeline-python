from typing import List
import re

class Chunker:
    def __init__(self, chunk_size: int = 300, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap


    def chunk_by_paragraph(self, text: str) -> List[str]:
        paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
        return paragraphs
    
    def chunk_by_sentence(self, text: str) -> List[str]:
        sentences = re.split(r'(?<=[.!?]) +', text)
        return sentences
    
    def chunk_fixed(self, text: str) -> List[str]:
        words = text.split()
        chunks = []

        i = 0
        while i < len(words):
            chunk = words[i:i + self.chunk_size]
            chunks.append(" ".join(chunk))
            i += self.chunk_size - self.overlap

        return chunks