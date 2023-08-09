from class_struct import *





def is_overlapping(session1, session2):
    # Check if sessions have overlapping dates
    if session1.start_date != "" and session1.end_date != "" and session2.start_date != "" and session2.end_date != "":
        if session1.start_date > session2.end_date or session1.end_date < session2.start_date:
            return False

    # Check if sessions are on the same day
    if not set(session1.days).intersection(set(session2.days)):
        return False

    # Check if sessions overlap in time
    start1 = session1.start_time[0] * 60 + session1.start_time[1]
    end1 = session1.end_time[0] * 60 + session1.end_time[1]
    start2 = session2.start_time[0] * 60 + session2.start_time[1]
    end2 = session2.end_time[0] * 60 + session2.end_time[1]

    if start1 <= start2 < end1 or start1 < end2 <= end1:
        return True

    return False




# DEBUGGER
def print_schedule(schedule):
    print("CURRENT SCHEDULE:")
    #print("===================================================================================================")
    for session in schedule:
        print(session)
    print("===================================================================================================")
    print("\n")
    

# DEBUGGER
def print_schedule_list(schedule_list):
    for schedule in schedule_list:
        print_schedule(schedule)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< END OF SCHEDULE LIST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
    return None




# curr_schedule: list of selected sessions
# to_be_scheduled_catagories: catagories of sessions to be scheduled (e.g., ['TST', 'LEC', 'LAB', 'TUT'] => still need to schedule a TST, LEC, LAB, and TUT session)
def add_sessions_to_schedule(curr_schedule, new_schedule_list, curr_course, to_be_scheduled_sessions, courses_dict):
    # base case: all sessions have been scheduled
    if len(to_be_scheduled_sessions) == 0:
        #print_schedule(curr_schedule)
        # print("ADDED A NEW COURSE SCHEDULE: ")
        # print(curr_course)
        new_schedule_list.append(curr_schedule.copy())
        # print("PRINTING curr_schedule:")
        # print_schedule(curr_schedule)
        # print("PRINTING new_schedule_list:")
        # print_schedule(new_schedule_list)
        return None

    # recursive case: add a session to the schedule
    curr_session = to_be_scheduled_sessions[0]
    to_be_scheduled_sessions = to_be_scheduled_sessions[1:]

    # if this course does not have a session of the current category, skip it
    if len(courses_dict[curr_course][curr_session]) == 0:
        add_sessions_to_schedule(curr_schedule, new_schedule_list, curr_course, to_be_scheduled_sessions, courses_dict)
        return None

    for session in courses_dict[curr_course][curr_session]:
        # Check if session overlaps with any of the sessions in the current schedule
        overlapping = False
        for scheduled_session in curr_schedule:
            if is_overlapping(session, scheduled_session):
                # print("SESSION OVERLAPS: " + session.classCode + " " + session.section + " " + session.category)
                # print("WITH: " + scheduled_session.classCode + " " + scheduled_session.section + " " + scheduled_session.category)
                overlapping = True
                break

        # If session does not overlap with any of the sessions in the current schedule, add it to the schedule
        if not overlapping:
            curr_schedule.append(session)
            add_sessions_to_schedule(curr_schedule, new_schedule_list, curr_course, to_be_scheduled_sessions, courses_dict)
            curr_schedule.remove(session)

    return None



# use backtracking to generate all possible schedules
# schedule_list: list of schedules (Format: [list of [list of Session]])
# to_be_scheduled_course_names: list of course names to be scheduled
def add_courses_to_schedule(schedule_list, to_be_scheduled_course_names, courses_dict):
    for course in to_be_scheduled_course_names:
        new_schedule_list = []
        for curr_schedule in schedule_list:
            # print("ADDING A NEW COURSE SCHEDULE: ")
            # print(course)

            # print("CURRENT OLD SCHEDULE TO BE ADDED ON:")
            # print_schedule(curr_schedule)

            add_sessions_to_schedule(curr_schedule, new_schedule_list, course, ["TST", "LEC", "LAB", "TUT"], courses_dict)
            # print("AFTER ADDING SESSIONS: (printing new_schedule_list))")
            # print_schedule_list(new_schedule_list)

        schedule_list = new_schedule_list.copy()
        # print(f"FINISHED ADDING COURSE {course}, CURRENT SCHEDULES: ")
        # print("SCHEDULE_LIST:")
        # print_schedule_list(schedule_list)
        # print("NEW_SCHEDULE_LIST:")
        # print_schedule_list(new_schedule_list)      

        
    return schedule_list


