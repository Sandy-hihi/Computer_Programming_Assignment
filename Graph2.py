import numpy as np
import matplotlib.pyplot as plt
import Subject2 as Sb


def plot_bar_graph():
    # 과목 선택
    subject = Sb.print_subject()

    # 남성 및 여성 데이터 추출
    mandata = Sb.extract_data_man(subject)
    womandata = Sb.extract_data_woman(subject)

    # 점수와 인원수를 numpy 배열로 변환
    scores = sorted(set(mandata.keys()).union(set(womandata.keys())))
    mcounts = [mandata.get(score, 0) for score in scores]
    wcounts = [womandata.get(score, 0) for score in scores]

    # 막대 그래프 생성
    x = np.arange(len(scores))
    bar_width = 0.4

    plt.figure(figsize=(12, 6))
    plt.bar(x - bar_width / 2, mcounts, width=bar_width, label="Male", color="blue")
    plt.bar(x + bar_width / 2, wcounts, width=bar_width, label="Female", color="orange")

    plt.title(f"Score Distribution for {subject}", fontsize=14)
    plt.xlabel("Score", fontsize=12)
    plt.ylabel("Number of People", fontsize=12)
    plt.xticks(x, scores, rotation=45)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3, axis="y")

    # 그래프 출력
    plt.tight_layout()
    plt.show()
