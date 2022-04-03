import numpy as np
from person_similarity import PersonSimilarity
from cosine_similarity import CosineSimilarity


class TFIDFSimilarity(PersonSimilarity):
    def __init__(self, person_list):
        self.person_list = person_list
        self.cosine_similarity = CosineSimilarity()
        self.word_list = self.get_word_list()
        self.tf_matrix = self.build_tf_matrix()
        self.idf_matrix = self.build_idf_matrix()
        self.weight_matrix = self.build_weight_matrix()

    def get_word_list(self):
        all_words = set()
        for person in self.person_list:
            for ans in person.get_ans_list():
                for word in ans.get_word_freq().keys():
                    all_words.add(word)
        return list(all_words)

    def build_tf_matrix(self):
        result = []
        for person in self.person_list:
            person_tf = []
            for ans in person.get_ans_list():
                tf_matrix = dict(
                    zip(self.word_list, [0] * len(self.word_list)))
                word_freq = ans.get_word_freq()
                for word in word_freq.keys():
                    tf_matrix[word] = word_freq[word]['count']
                person_tf.append(tf_matrix)
            result.append(person_tf)
        return result

    def build_idf_matrix(self):
        df_matrix = dict(zip(self.word_list, [0] * len(self.word_list)))
        total_ans = 0
        for person in self.person_list:
            for ans in person.get_ans_list():
                for word in ans.get_word_freq().keys():
                    df_matrix[word] += 1
                total_ans += 1

        result = dict()
        for word, ans_freq in df_matrix.items():
            result[word] = np.log(total_ans / ans_freq)
            if result[word] == 0:
                result[word] = np.log(total_ans / (total_ans - 1)) / 2
        return result

    def build_weight_matrix(self):
        result = []
        for p_idx, person in enumerate(self.person_list):
            person_weight = []
            for a_idx, ans in enumerate(person.get_ans_list()):
                ans_weight = dict()
                for word, freq in self.tf_matrix[p_idx][a_idx].items():
                    if freq == 0:
                        ans_weight[word] = 0
                    else:
                        ans_weight[word] = (np.log(freq) + 1) * \
                            self.idf_matrix[word]
                person_weight.append(ans_weight)
            result.append(person_weight)
        return result

    def calc_person_similarity(self, p1_idx, p2_idx):
        sim_matrix = []
        p1_ans_list = self.person_list[p1_idx].get_ans_list()
        for i in range(len(p1_ans_list)):
            vec1 = []
            for word in self.word_list:
                vec1.append(self.weight_matrix[p1_idx][i][word])

            vec2 = []
            for word in self.word_list:
                vec2.append(self.weight_matrix[p2_idx][i][word])

            sim_value = self.cosine_similarity.calc_similarity(vec1, vec2)
            sim_matrix.append(sim_value)
        return sim_matrix
