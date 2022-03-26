class AnswerSimilarity:
    def __init__(self, vec1, vec2):
        self.vec1 = vec1
        self.vec2 = vec2

    def calc_similarity(self):
        raise NotImplementedError("calc_similarity method is not implemented")
