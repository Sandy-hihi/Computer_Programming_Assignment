import Subject as Sb
import Graph as Gp

subjects = Sb.extract_subject()     # 과목 리스트 생성 및 과목 등록
selected_sub = Sb.print_subject()   # 과목을 선택하라고 출력한 후, 사용자의 답을 저장
Gp.draw_graph(selected_sub)     # 사용자의 답을 바탕으로 그래프 출력
