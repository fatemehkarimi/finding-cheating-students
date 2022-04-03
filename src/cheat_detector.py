from person_similarity import PersonSimilarity
from settings import Settings


class CheatDetector:
    def __init__(self, person_list, person_sim_meter: PersonSimilarity):
        self.person_list = person_list
        self.person_sim_meter = person_sim_meter
        self.sim_matrix = self.get_all_person_sim_matrix()

    def get_all_person_sim_matrix(self):
        result = []
        for i in range(len(self.person_list)):
            person_sim = []
            for j in range(len(self.person_list)):
                sim_measure = self.person_sim_meter.calc_person_similarity(
                    i, j)
                person_sim.append(sim_measure)
            result.append(person_sim)
        return result

    def calc_max_sim_for_answer(self, person_idx, ans_idx):
        max_sim_value = 0
        sim_person_idx = person_idx
        for i in range(len(self.person_list)):
            if i == person_idx:
                continue
            sim_value = self.sim_matrix[person_idx][i][ans_idx]
            if sim_value > max_sim_value:
                max_sim_value = sim_value
                sim_person_idx = i
        return (sim_person_idx, max_sim_value)

    def find_cheated(self):
        result = {}
        for i in range(len(self.person_list)):
            person_cheat = {}
            person_cheat_with_set = set()
            for j in range(len(self.person_list[i].get_ans_list())):
                sim_person, sim_value = self.calc_max_sim_for_answer(i, j)
                if sim_value >= Settings.MIN_CHEAT_BOUNDRY:
                    person_cheat[str(j)] = {
                        'similarity': sim_value,
                        'with who': sim_person}
                    person_cheat_with_set.add(sim_person)
            suspects = []
            for who in person_cheat_with_set:
                suspects.append({
                    'id': who,
                    'name': self.person_list[who].name
                })
            report = {
                'suspects': suspects,
                'details': person_cheat
            }
            result[str(i)] = report
        return result
