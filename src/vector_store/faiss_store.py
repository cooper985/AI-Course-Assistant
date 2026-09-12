 import faiss
 import numpy as np


 class FAISS_Store:

     def __init__(self,dimension):
         self.dimension = dimension
         self.index = faiss.IndexFlatL2(dimension)
         self.documents = []