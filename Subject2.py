import csv

subjects = []


def input_year():
    years = ['2020', '2021', '2022', '2023']
    year = input("연도 선택(2020, 2021, 2022, 2023) :")
    if year in years:
        return year
    else:
        print('2020 / 2021 / 2022 / 2023 중 하나를 입력하세요.')
        return input_year()


def extract_subject():  # 과목 이름들을 리스트에 넣는 함수
    year = input_year()
    f = open(f'{year}1231.csv')
    reader = csv.reader(f)
    for row in reader:
        if row[1] not in subjects and row[1] != '유형':
            subjects.append(row[1])
    f.close()
    return year


def print_subject():  # 과목을 출력하는 함수
    year = extract_subject()
    for i in range(len(subjects)):
        print(f"{i + 1}.{subjects[i]}", end=" ")
    enter_subject = input("어떤 과목을 선택하시겠습니까?")
    while True:
        if enter_subject not in subjects:
            enter_subject = input("알맞은 과목 명을 입력하세요.")
        else:
            break

    return enter_subject, year


def extract_data_man(subject, year):
    f = open(f'{year}1231.csv')
    reader = csv.reader(f)
    man_data = {}
    for row in reader:
        if row[1] == subject:
            man_data[int(row[2].strip())] = int(row[3].strip())
    return man_data


def extract_data_woman(subject, year):
    f = open(f'{year}1231.csv')
    reader = csv.reader(f)
    woman_data = {}
    for row in reader:
        if row[1] == subject:
            woman_data[int(row[2].strip())] = int(row[4].strip())
    return woman_data
