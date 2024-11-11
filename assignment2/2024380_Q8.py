def minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def mark_busy_slots(schedule, timeline):
    for slot in schedule:
        start, end = slot.split('-')
        start_minutes = minutes(start)
        end_minutes = minutes(end)
        for i in range(start_minutes, end_minutes):
            timeline[i] = True

def find_common_free_slot(alice_schedule, bob_schedule, cameron_schedule):
    timeline = [False] * 1440  
    mark_busy_slots(alice_schedule, timeline)
    mark_busy_slots(bob_schedule, timeline)
    mark_busy_slots(cameron_schedule, timeline)

    free_slots = []
    start_free = None
    for i in range(540, 1020):  
        if timeline[i] == False:
            if start_free is None:
                start_free = i
            if i - start_free >= 30:
                free_slots.append((start_free, i))
                start_free = None
        else:
            start_free = None

    if free_slots:
        for start, end in free_slots:
            start_time = f"{start // 60:02}:{start % 60:02}"
            end_time = f"{end // 60:02}:{end % 60:02}"
            print(f"Common free slot: {start_time}-{end_time}")
        return

    conflicts = []
    for i in range(540, 1020):
        if not timeline[i]:
            if i + 30 <= 1020 and all(timeline[j] for j in range(i, i + 30)):
                start_time = f"{i // 60:02}:{i % 60:02}"
                end_time = f"{(i + 30) // 60:02}:{(i + 30) % 60:02}"
                conflicts.append((start_time, end_time))
                break

    if conflicts:
        for start_time, end_time in conflicts:
            print(f"Conflict slot: {start_time}-{end_time}")
        return

    print("No available time for all participants")

alice_schedule = list(map(str, input('Enter Alice\'s schedule: ').split()))
bob_schedule = list(map(str, input('Enter Bob\'s schedule: ').split()))
cameron_schedule = list(map(str, input('Enter Cameron\'s schedule: ').split()))

find_common_free_slot(alice_schedule, bob_schedule, cameron_schedule)

def unique_free_timeslots(alice_schedule, bob_schedule, cameron_schedule):
    out = [i for i in alice_schedule if i not in bob_schedule and i not in cameron_schedule]    
    return out

def get_free_slot(free_slot):
    out = []
    for i in free_slot:
        if i+30 in free_slot:
            out.append({'start': f"{i // 60:02}:{i % 60:02}", 'end': f"{(i + 30) // 60:02}:{(i + 30) % 60:02}"})
    return out

def bonus_free_timeslots(alice_schedule, bob_schedule, cameron_schedule):
    t1 = [False] * 1440
    t2 = [False] * 1440
    t3 = [False] * 1440
    mark_busy_slots(alice_schedule, t1)
    mark_busy_slots(bob_schedule, t2)
    mark_busy_slots(cameron_schedule, t3)

    alice_free_slot = set(i for i in range(540, 1020) if not t1[i])
    bob_free_slot = set(i for i in range(540, 1020) if not t2[i])
    cameron_free_slot = set(i for i in range(540, 1020) if not t3[i])

    f1 = get_free_slot(alice_free_slot)
    f2 = get_free_slot(bob_free_slot)
    f3 = get_free_slot(cameron_free_slot)

    out1 = unique_free_timeslots(f1, f2, f3)
    out2 = unique_free_timeslots(f2, f1, f3)
    out3 = unique_free_timeslots(f3, f1, f2)
    
    if len(out1) >= 3 and len(out2) >= 3 and len(out3) >= 3:
        print(f'Unique free slots for Alice: {out1[:3]}')
        print(f'Unique free slots for Bob: {out2[:3]}')
        print(f'Unique free slots for Cameron: {out3[:3]}')
    else:
        alice_bob_common = alice_free_slot & bob_free_slot
    alice_cameron_common = alice_free_slot & cameron_free_slot
    bob_cameron_common = bob_free_slot & cameron_free_slot

    if alice_bob_common and not alice_cameron_common and not bob_cameron_common and len(alice_bob_common)==1:
        for start in sorted(alice_bob_common):
            if start + 30 in alice_bob_common:
                start_time = f"{start // 60:02}:{start % 60:02}"
                end_time = f"{(start + 30) // 60:02}:{(start + 30) % 60:02}"
                print(f"Conflict slot: {start_time}-{end_time} (Alice and Bob)")
                return

    if alice_cameron_common and not alice_bob_common and not bob_cameron_common and len(alice_cameron_common)==1:
        for start in sorted(alice_cameron_common):
            if start + 30 in alice_cameron_common:
                start_time = f"{start // 60:02}:{start % 60:02}"
                end_time = f"{(start + 30) // 60:02}:{(start + 30) % 60:02}"
                print(f"Conflict slot: {start_time}-{end_time} (Alice and Cameron)")
                return

    if bob_cameron_common and not alice_bob_common and not alice_cameron_common and len(bob_cameron_common)==1:
        for start in sorted(bob_cameron_common):
            if start + 30 in bob_cameron_common:
                start_time = f"{start // 60:02}:{start % 60:02}"
                end_time = f"{(start + 30) // 60:02}:{(start + 30) % 60:02}"
                print(f"Conflict slot: {start_time}-{end_time} (Bob and Cameron)")
                return

    print("No available time for all participants")

bonus_free_timeslots(alice_schedule, bob_schedule, cameron_schedule)

def test():
    assert minutes('09:30') == 570
    assert minutes('10:00') == 600

test()