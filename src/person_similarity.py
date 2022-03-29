class PersonSimilarity:
    def __init__(self, ans_sim_meter):
        self.ans_sim_meter = ans_sim_meter

    def build_similarity_matrix(self, person1, person2):
        sim_matrix = []
        for ans1 in person1.get_ans_list():
            for ans2 in person2.get_ans_list():
                sim_value = self.ans_sim_meter.calc_similarity(
                    ans1.get_word_freq(),
                    ans2.get_word_freq())
            sim_matrix.append(sim_value)
        return sim_matrix
