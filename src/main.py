import pandas as pd
from Answer import Answer


def main():
    df = pd.read_excel('./dataset/Answers.xlsx')
    for idx, row in df.iterrows():
        ans_text = row['Question 1']
        ans_status = row['Status 1']
        answer = Answer(ans_text, ans_status)
        print(answer.get_word_freq())


if __name__ == "__main__":
    main()
