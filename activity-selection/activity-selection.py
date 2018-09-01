def activity_selection(start_time, end_time):
    selected_activities = [0]
    last_selected = 0
    for i in range(1, len(end_time)):
        if (start_time[i] >= end_time[last_selected]):
            selected_activities.append(i)
            last_selected = i

    return selected_activities

if __name__=="__main__":
    start_time = [1, 3, 0, 5, 8, 5]
    end_time = [2, 4, 6, 7, 9, 9]
    print activity_selection(start_time, end_time)