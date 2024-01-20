def solution(name, yearning, photo):
    answer = []
    temp_dict = dict()
    for i, person in enumerate(name):
        temp_dict[person] = yearning[i]
    for step in photo: 
        step_res = 0
        for step_person in step:
            if step_person in temp_dict:
                step_res += temp_dict[step_person]
        answer.append(step_res)
    return answer