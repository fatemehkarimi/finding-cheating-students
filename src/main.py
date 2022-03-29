import pandas as pd
from answer import Answer
from person import Person
from jaccard_similarity import JaccardSimilaritiy
from person_similarity import PersonSimilarity


def get_person_list(df):
    person_list = []
    for row_idx, row in df.iterrows():
        ans_list = []
        ans_text = ''
        for col_idx, column in enumerate(df.columns):
            if col_idx % 2 == 0:
                ans_text = row[column]
            else:
                ans_status = row[column]
                ans_list.append(Answer(ans_text, ans_status))
        person = Person(ans_list)
        person_list.append(person)


def main():
    df = pd.read_excel('./dataset/Answers.xlsx')
    person_list = get_person_list(df)
    person_sim_meter = PersonSimilarity(JaccardSimilaritiy())

    for i in range(len(person_list)):
        for j in range(i + 1, len(person_list)):
            sim_matrix = person_sim_meter.build_similarity_matrix(
                person_list[i], person_list[j])


if __name__ == "__main__":
    main()
