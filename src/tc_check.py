
keys = ['in', 'out', 'break-start', 'break-end', 'total', 'over_midnight',
        'paid-holiday', 'sick-leave', 'business-trip',
        'season-holiday', 'replacement-off', 'compensatory-off', 'holiday']


def tc_to_dict(string):
    local_keys = [word.strip() for word in string.split('\n')[0].split('|')[1:]]
    dict_dates = dict()
    for line in string.split('\n')[1:]:
        if line.split('|')[0].strip() == '':
            # last line for total, break
            break
        line_dict = dict()
        for i, item in enumerate(line.split('|')[1:]):
            line_dict[local_keys[i]] = item.strip()
        dict_dates[line.split('|')[0].strip()] = line_dict
    return dict_dates


def oclock_to_minutes(string):
    hour, minute = string.split(':')
    return int(hour) * 60 + int(minute)


def minutes_to_oclock(minutes):
    if minutes < 0:
        return '-' + minutes_to_oclock(-minutes)
    else:
        return str(minutes // 60) + ':' + str(minutes % 60)


def had_to_work(date, dico_day):
    if date.find('Sun') != -1:
        return False
    elif date.find('Sat') != -1:
        return False
    elif 'paid-holiday' in dico_day.keys() and dico_day['paid-holiday'] == 'yes':
        return False
    elif 'sick-leave' in dico_day.keys() and dico_day['sick-leave'] == 'yes':
        return False
    elif 'season-holiday' in dico_day.keys() and dico_day['season-holiday'] == 'yes':
        return False
    elif 'business-trip' in dico_day.keys() and dico_day['business-trip'] == 'yes':
        return True  # business-trip sets total to '8:00'
    elif 'replacement-off' in dico_day.keys() and dico_day['replacement-off'] == 'yes':
        return False
    elif 'compensatory-off' in dico_day.keys() and dico_day['compensatory-off'] == 'yes':
        return False
    elif 'holiday' in dico_day.keys() and dico_day['holiday'].strip() != '':
        return False
    else:
        return True


def check_valid(dico):
    due_dates = 0
    due_time = 0
    for date in sorted(list(dico.keys())):
        if dico[date]['total'] == '':
            # check if had to work
            if had_to_work(date, dico[date]):
                print('input error for {}'.format(date))
        else:
            if not had_to_work(date, dico[date]):
                # overtime, not counted in due date
                print('worked during holiday on {}'.format(date))
            else:
                due_dates += 1
                due_time += 8*60 - oclock_to_minutes(dico[date]['total'])
    print('due_time {} (if negative or zero: OK!)'.format(minutes_to_oclock(due_time)))


if __name__ == '__main__':
    import sys
    check_valid(tc_to_dict(sys.argv[1]))
