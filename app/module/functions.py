# The following function returns the tuition cost for a given state and time period
# This data will provide the in-state and out of state tuition metric for the given State University


def find_tution_cost(state, timing, university_data):
    college_dict = {}
    for i in range(len(university_data)):
        if university_data[i]['STATE_NAME'] == state:
            if timing == 1:
                college_dict.update({"State": state, "University": university_data[i]['University'],
                                     "InState": university_data[i]['2020-21'], "OutState": university_data[i]['Out_2020_2021']})

            elif timing == 2:
                college_dict.update({"State": state, "University": university_data[i]['University'],
                                     "InState": university_data[i]['2021-22'], "OutState": university_data[i]['Out_2021_2022']})

            else:
                college_dict.update({"State": state, "University": university_data[i]['University'],
                                     "InState": university_data[i]['2021-22'], "OutState": university_data[i]['Out_2021_2022']})

    return college_dict


# The following function will return data and labels to be used for our charts using the Chart js library.
# It take one parameter of subject - which helps to map which mongo collection and data structure we are working
# with to provide the data
def prepare_chart_data(subject, university_data):
    labels = []
    in_state_labels = []
    out_state_labels = []
    data_values = []
    in_state_values = []
    out_state_values = []

    chart_data = {}
    count_for_in_state = 0

    if subject == 'university':
        for key in university_data[0].keys():

            if not (key == '_id' or key == 'University' or key == 'STATE'):
                labels.append(key)

        labels.pop(len(labels) - 1)

        # get a count for half of the list (i.e. in-state)
        count_for_in_state = len(labels) / 2

        # break the list into two separate lists (i.e. one for in_state and one for out of state)
        for i in range(int(count_for_in_state)):
            in_state_labels.append(labels[i])

        for i in range(int(count_for_in_state)-1, (int(count_for_in_state) * 2)-1, 1):
            out_state_labels.append(labels[i])

        for value in university_data[0].values():

            if not (type(value) == str):
                data_values.append(value)

        data_values.pop(0)

        # break the list into two separate lists (i.e. one for in_state and one for out of state)
        for i in range(int(count_for_in_state)):
            in_state_values.append(data_values[i])

        for i in range(int(count_for_in_state)-1, (int(count_for_in_state) * 2)-1, 1):
            out_state_values.append(data_values[i])

        chart_data.update({'in_state_labels': in_state_labels, 'in_state_values': in_state_values,
                           'out_state_labels': out_state_labels, 'out_state_values': out_state_values})

    return chart_data

def get_state_wage(state, state_wages):
    state_wage_list = []
    state_wage_list = list(state_wages.find())
    result_values = [i[state] for i in state_wage_list if state in i]
    result =result_values[0]
    return result


# The following function returns the average tuition change by year across all 50 states.
def avg_tuition_cost_by_year(University):
    # generate a list of dictionaries from 
    # the university data
    university_data = list(University.find())

    # generate a list of distinct states
    state_list = []
    for i in range(len(university_data) -1):
        state_list.append(university_data[i]['STATE'])

    # get a
    university_keys = []
    for key in university_data[0].keys():
        university_keys.append(key)
    
    # remove the keys not needed 
    # for the averages calculation
    del university_keys[0]
    del university_keys[0]
    del university_keys[0]
    del university_keys[-1]
    
    # break university_keys into in_state and out_state keys
    no_of_keys = int(len(university_keys) / 2)

    in_state_keys = []
    for i in range(no_of_keys):
        in_state_keys.append(university_keys[i])

    out_state_keys = []
    for i in range(no_of_keys, 29, 1):
        out_state_keys.append(university_keys[i])
    
    # declare variables for yearly_averages dictionary, 
    # total, counter and in/out state averages
    yearly_averages_dict = {}
    total = 0
    cnt = 0
    in_state_avg = 0
    out_state_avg = 0
    yr_key = 'yyyy-yy'

    #loop through list of in_state year keys
    for yr in in_state_keys:
        yr_key = yr
        cnt = 0
        total = 0

        # then for each year key recursively loop through the university collection 
        # and add the value for the matching key from the state data to the total
        for i in range(len(university_data)-1):
            total += university_data[i][yr_key]
            cnt += 1

        #calculate the in_state_average for the yr_key
        in_state_avg = int(total / cnt)
            
        yearly_averages_dict.update({yr_key: in_state_avg})

    # repeat the process / techniques using the out_state year keys
    for yr in out_state_keys:
        yr_key = yr
        cnt = 0
        total = 0
        
        for i in range(len(university_data)-1):
            total += university_data[i][yr_key]
            cnt += 1
        
        #calculate the out_state_average for the yr_key
        out_state_avg = int(total / cnt)
        
        yearly_averages_dict.update({yr_key: out_state_avg})
    
    return yearly_averages_dict