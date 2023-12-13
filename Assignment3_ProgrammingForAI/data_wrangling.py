def prepare_data(input_data):
    study_hours = []
    exam_scores = []
    for i in input_data:
        study_hours.append(i[0])
        exam_scores.append(i[1])
    return study_hours, exam_scores

input_data = [(5,65),(12,82),(100,87),(0,23)]
study_hours, exam_scores = prepare_data(input_data)
print(f'study_hours = {study_hours}')
print(f'exam_scores = {exam_scores}')