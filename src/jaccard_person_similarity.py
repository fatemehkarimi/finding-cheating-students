from person_similarity import PersonSimilarity
from jaccard_similarity import JaccardSimilaritiy


class JaccardPersonSimilarity(PersonSimilarity):
    def __init__(self, person_list):
        self.person_list = person_list
        self.jaccard_sim_meter = JaccardSimilaritiy()

    def calc_person_similarity(self, p1_idx, p2_idx):
        sim_matrix = []
        p1_ans_list = self.person_list[p1_idx].get_ans_list()
        p2_ans_list = self.person_list[p2_idx].get_ans_list()

        for i in range(len(p1_ans_list)):
            sim_value = self.jaccard_sim_meter.calc_similarity(
                p1_ans_list[i].get_word_freq(),
                p2_ans_list[i].get_word_freq())
            sim_matrix.append(sim_value)
        return sim_matrix
