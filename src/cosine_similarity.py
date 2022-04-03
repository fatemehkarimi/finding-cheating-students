import numpy as np
from answer_similarity import AnswerSimilarity


class CosineSimilarity(AnswerSimilarity):
    def calc_similarity(self, ans1, ans2):
        if len(ans1) != len(ans2):
            raise Exception("vectors should have equal size")
        dot_product = np.dot(ans1, ans2)
        norm_vec1 = np.linalg.norm(ans1)
        norm_vec2 = np.linalg.norm(ans2)

        return dot_product / (norm_vec1 * norm_vec2)
