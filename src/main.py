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
        name = ''
        ans_list = []
        for col_idx, column in enumerate(df.columns):
            if column == 'name':
                name = str(row[column])
                continue
            ans_list.append(Answer(row[column]))
        person = Person(name, ans_list)
        person_list.append(person)
    return person_list


def write_result_to_json(result, filename):
    with open(filename, 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


def main():
    df = pd.read_excel('./dataset/persian-dataset.xlsx')
    df = df.fillna(' ')
    person_list = get_person_list(df)

    cosine_meter = TFIDFSimilarity(person_list)
    jaccard_meter = JaccardPersonSimilarity(person_list)

    jaccard_cheat_detector = CheatDetector(person_list, jaccard_meter)
    cosine_cheat_detector = CheatDetector(person_list, cosine_meter)

    result1 = jaccard_cheat_detector.find_cheated()
    result2 = cosine_cheat_detector.find_cheated()

    write_result_to_json(result1, "jaccard_result.json")
    write_result_to_json(result2, "cosine_result.json")


if __name__ == "__main__":
    main()
