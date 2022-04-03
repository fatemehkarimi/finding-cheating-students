import json
import pandas as pd
from answer import Answer
from person import Person
from cheat_detector import CheatDetector
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

    jaccard_cheat_detector = CheatDetector(person_list, jaccard_meter)
    cosine_cheat_detector = CheatDetector(person_list, cosine_meter)

    result1 = jaccard_cheat_detector.find_cheated()
    result2 = cosine_cheat_detector.find_cheated()

    with open('jaccard_result.json', 'w') as f:
        json.dump(result1, f, indent=4)

    with open('cosine_result.json', 'w') as f:
        json.dump(result2, f, indent=4)


if __name__ == "__main__":
    main()
