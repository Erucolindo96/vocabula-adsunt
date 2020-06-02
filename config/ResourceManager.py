from typing import List


class ResourceManager:

    @staticmethod
    def stopwords(path: str) -> str:
        with open(path, encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def authors_slugs(path: str) -> List[str]:
        with open(path, encoding='utf-8') as f:
            return f.read().split()
