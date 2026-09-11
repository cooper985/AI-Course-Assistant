from src.embedding.embedder import Embedder


embedder = Embedder()


text = "原码是一种表示有符号数的方法"


vector = embedder.embed(text)


print(vector)

print("向量长度:", len(vector))