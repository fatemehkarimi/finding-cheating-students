import pandas as pd
from answer import Answer
from person import Person
from tf_idf_similarity import TFIDFSimilarity
from jaccard_person_similarity import JaccardPersonSimilarity


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

    cosine_meter = TFIDFSimilarity(person_list)
    jaccard_meter = JaccardPersonSimilarity(person_list)

    # for i in range(len(person_list)):
    # for j in range(len(person_list)):

    cosine_sim_matrix = cosine_meter.calc_person_similarity(12, 5)
    jaccard_sim_matrix = jaccard_meter.calc_person_similarity(12, 5)
    print(cosine_sim_matrix)
    print(jaccard_sim_matrix)
    print("-------------------------------------")


if __name__ == "__main__":
    main()
