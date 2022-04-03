from answer_similarity import AnswerSimilarity


class JaccardSimilaritiy(AnswerSimilarity):
    def calc_similarity(self, ans1, ans2):
        count_common = 0
        for w in ans1.keys():
            if w in ans2.keys():
                count_common += 1
        count_union = len(ans1.keys()) + len(ans2.keys()) - count_common

        if count_union == 0:
            return 1
        return count_common / count_union
