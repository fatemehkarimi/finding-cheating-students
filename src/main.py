import pandas as pd
from answer import Answer
from person import Person
from jaccard_similarity import JaccardSimilaritiy
from person_similarity import PersonSimilarity
from tf_idf_similarity import TFIDFSimilarity


def get_person_list(df):
    person_list = []
    for row_idx, row in df.iterrows():
        ans_list = []
        for col_idx, column in enumerate(df.columns):
            ans_list.append(Answer(row[column]))
        person = Person(ans_list)
        person_list.append(person)
    return person_list


def main():
    df = pd.read_excel('./dataset/Answers.xlsx')
    person_list = get_person_list(df)

    sim_meter = TFIDFSimilarity(person_list)
    # person_sim_meter = PersonSimilarity(JaccardSimilaritiy())

    for i in range(len(person_list)):
        for j in range(len(person_list)):
            sim_matrix = sim_meter.calc_person_similarity(i, j)
            print(sim_matrix)
        print("-------------------------------------")


if __name__ == "__main__":
    main()
