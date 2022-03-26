import pandas as pd
from answer import Answer
from jaccard_similarity import JaccardSimilaritiy


def main():
    df = pd.read_excel('./dataset/Answers.xlsx')

    answer_list = []
    for idx, row in df.iterrows():
        ans_text = row['Question 1']
        ans_status = row['Status 1']
        answer = Answer(ans_text, ans_status)
        answer_list.append(answer)

    sim_measure = JaccardSimilaritiy(
        answer_list[0].get_word_freq(),
        answer_list[1].get_word_freq()
    )

    print(sim_measure.calc_similarity())


if __name__ == "__main__":
    main()
