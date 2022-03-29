from answer_similarity import AnswerSimilarity


class JaccardSimilaritiy(AnswerSimilarity):
    def calc_similarity(self, vec1, vec2):
        count_common = 0
        for w in vec1.keys():
            if w in vec2.keys():
                count_common += 1
        count_union = len(vec1.keys()) + len(vec2.keys()) - count_common

        if count_union == 0:
            return 1
        return count_common / count_union
