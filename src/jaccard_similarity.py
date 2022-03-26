from answer_similarity import AnswerSimilarity


class JaccardSimilaritiy(AnswerSimilarity):
    def calc_similarity(self):
        count_common = 0
        for w in self.vec1.keys():
            if w in self.vec2.keys():
                count_common += 1
        count_union = len(self.vec1.keys()) + \
            len(self.vec2.keys()) - count_common

        if count_union == 0:
            return 1
        return count_common / count_union
