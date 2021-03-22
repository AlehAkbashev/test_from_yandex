def make_dict_schedule(my_schedule):
    my_dict = {}
    for i in range(len(my_schedule)):
        if my_schedule[i][0] not in my_dict.keys():
            my_dict[my_schedule[i][0]] = [my_schedule[i][1]]
        else:
            my_dict[my_schedule[i][0]].append(my_schedule[i][1])
    return my_dict


def make_schedule(num_pare):
    schedule_list = []
    for i in range(num_pare):
        lec2, lec1 = map(int, input().split())
        schedule_list.append((lec2, lec1))
    return schedule_list


def check(dict_schedule):
    flag = False
    for elem in dict_schedule.keys():
        for temp in dict_schedule[elem]:
            if dict_schedule.get(temp):
                if elem in dict_schedule[temp]:
                    flag = True
    if flag:
        print('NO')
    else:
        print('YES')


def main():
    n, p = map(int, input().split())
    schedule = make_schedule(p)
    dict_lecture = make_dict_schedule(schedule)
    check(dict_lecture)


main()


