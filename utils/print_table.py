import math

def table_of_options(title, *options):
    title_length = len(title)
    total_white_space = 10
    side_spaces = total_white_space//2
    total_length = title_length+total_white_space
    print(f"+{'-'*total_length}+")
    print(f"|{' '*side_spaces}{title}{' '*side_spaces}|")
    print(f"+{'-'*total_length}+")
    for idx, option in enumerate(options):
        print(f"|{' '*side_spaces}{idx+1} - {option}{' '*(title_length-len(option)-4+side_spaces)}|")
    print(f"+{'-'*total_length}+")
    choice = input("| Choice: ")
    return choice


def projects_table(projects):
    print()

    titles = projects[0].keys()
    padding = {
        "id": 2,
        "owner_id": 2,
        "title": 5,
        "description": 7,
        "total_target": 2,
        "start_date": 3,
        "end_date": 3,
    }
    total_length = 1

    for title in titles:
        total_length += padding[title] + len(title) + padding[title] + 1

    print(f"+{'-'*(total_length-2)}+")

    print("|", end='')
    for title in titles:
        print(f"{' '*padding[title]}{title}{' '*padding[title]}|", end='')
    print()

    print(f"+{'-'*(total_length-2)}+")

    for project in projects:
        print("|", end='')

        for key, value in project.items():
            padding_temp = (len(key) + (padding[key]*2) - len(str(value)))/2
            padding_left = math.floor(padding_temp)
            padding_right = math.ceil(padding_temp)
            print(f"{' '*padding_left}{value}{' '*padding_right}|", end='')

        print()
        print(f"+{'-'*(total_length-2)}+")
    
    print()

# def projects_table(projects):
#     titles = projects[0].keys()
#     padding = {title: max(len(title), max(len(str(p[title])) for p in projects))
#                for title in titles}
#     total_length = sum(padding.values()) + (len(padding)*2) + 1

#     print(f"+{'-'*(total_length-2)}+")
#     print("|", end='')
#     for title in titles:
#         print(f" {title:^{padding[title]}} |", end='')
#     print()
#     print(f"+{'-'*(total_length-2)}+")

#     for project in projects:
#         print("|", end='')
#         for key, value in project.items():
#             print(f" {value:^{padding[key]}} |", end='')
#         print()
#         print(f"+{'-'*(total_length-2)}+")

#     print()


    


projects = [
    {
        "id": 1,
        "owner_id": 0,
        "title": "project-1",
        "description": "#####",
        "total_target": "25000",
        "start_date": "2023-04-07",
        "end_date": "2023-04-08"
    },
    {
        "id": 2,
        "owner_id": 0,
        "title": "project-2",
        "description": "#####",
        "total_target": "2000",
        "start_date": "2023-4-4",
        "end_date": "2023-4-5"
    },
    {
        "id": 3,
        "owner_id": 5,
        "title": "project-3",
        "description": "######",
        "total_target": "23000",
        "start_date": "2023-6-6",
        "end_date": "2023-6-9"
    }
]

# projects_table(projects)