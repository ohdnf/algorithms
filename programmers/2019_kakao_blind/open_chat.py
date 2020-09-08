def best_solution(record):
    answer = []
    users = {}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for r in record:
        r = r.split()
        if r[0] in ['Enter', 'Change']:
            users[r[1]] = r[2]
    
    for r in record:
        r = r.split()
        if r[0] in printer:
            answer.append('{}'.format(users[r[1]]) + printer[r[0]])
    
    return answer



def solution(records):
    users = dict()
    messages = []
    for record in records:
        status, *profile = record.split()   # profile[0] == uid / profile[1] == nickname
        if status == 'Enter':
            users[profile[0]] = profile[1]
            messages.append([status, profile[0]])
        elif status == 'Leave':
            messages.append([status, profile[0]])
        elif status == 'Change':
            users.update({profile[0]: profile[1]})
    answer = []
    for message in messages:
        status, uid = message
        if status == 'Enter':
            answer.append(f'{users.get(uid)}님이 들어왔습니다')
        elif status == 'Leave':
            answer.append(f'{users.get(uid)}님이 나갔습니다.')
        else:
            pass
    return answer

if __name__ == "__main__":
    records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    print(solution(records))