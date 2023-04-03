from utils.colors import Colors
import math

def table_of_options(title, *options):

    TABLE_COLOR = Colors.BLUE

    title_length = len(title)
    total_white_space = 10
    side_spaces = total_white_space//2
    total_length = title_length+total_white_space
    print(f"{TABLE_COLOR}+{'-'*total_length}+{Colors.RESET}")
    print(f"{TABLE_COLOR}|{Colors.RESET}{' '*side_spaces}{Colors.CYAN}{title}{' '*side_spaces}{TABLE_COLOR}|{Colors.RESET}")
    print(f"{TABLE_COLOR}+{'-'*total_length}+{Colors.RESET}")
    for idx, option in enumerate(options):
        print(f"{TABLE_COLOR}|{Colors.RESET}{' '*side_spaces}{Colors.GREEN}{idx+1} - {Colors.RESET}{option}{' '*(title_length-len(option)-4+side_spaces)}{TABLE_COLOR}|{Colors.RESET}")
    print(f"{TABLE_COLOR}+{'-'*total_length}+{Colors.RESET}")
    choice = input(f"{TABLE_COLOR}|{Colors.RESET} Choice: ")
    print()
    return choice


# def projects_table(projects):
#     print()

#     titles = projects[0].keys()
#     padding = {
#         "id": 2,
#         "owner_id": 2,
#         "title": 5,
#         "description": 7,
#         "total_target": 2,
#         "start_date": 3,
#         "end_date": 3,
#     }
#     total_length = 1

#     for title in titles:
#         total_length += padding[title] + len(title) + padding[title] + 1

#     print(f"+{'-'*(total_length-2)}+")

#     print("|", end='')
#     for title in titles:
#         print(f"{' '*padding[title]}{title}{' '*padding[title]}|", end='')
#     print()

#     print(f"+{'-'*(total_length-2)}+")

#     for project in projects:
#         print("|", end='')

#         for key, value in project.items():
#             padding_temp = (len(key) + (padding[key]*2) - len(str(value)))/2
#             padding_left = math.floor(padding_temp)
#             padding_right = math.ceil(padding_temp)
#             print(f"{' '*padding_left}{value}{' '*padding_right}|", end='')

#         print()
#         print(f"+{'-'*(total_length-2)}+")
    
#     print()

def projects_table(projects):

    TABLE_COLOR = Colors.BLUE

    # Add space befor printing the table
    print()

    # Get the column titles from the first project dictionary and calculate the padding for each column
    titles = projects[0].keys()
    padding = {
        title: max(
        len(title), 
        max(len(str(p[title])) for p in projects)
        )
        for title in titles
    }

    # Add 4 to each padding value to create a space between columns
    padding = {title: value + 4 for title, value in padding.items()}
    
    # Calculate the total length of the table and print the top border
    total_length = sum(padding.values()) + len(titles) + 1
    print(f"{TABLE_COLOR}+{'-'*(total_length-2)}+{Colors.RESET}")

    # Print the column titles and the bottom border for the title row
    print(f"{TABLE_COLOR}|{Colors.RESET}", end='')
    for title in titles:
        if title == 'id':
            print(f"{Colors.BOLD_YELLOW}{title:^{padding[title]}}{TABLE_COLOR}|{Colors.RESET}", end='')
        else:
            print(f"{Colors.BOLD_CYAN}{title:^{padding[title]}}{TABLE_COLOR}|{Colors.RESET}", end='')
    print()
    print(f"{TABLE_COLOR}+{'-'*(total_length-2)}+{Colors.RESET}")

    # Print each project row and the bottom border for the row
    for project in projects:
        print(f"{TABLE_COLOR}|{Colors.RESET}", end='')
        for key, value in project.items():
            if key == 'id':
                print(f"{Colors.GREEN}{value:^{padding[key]}}{TABLE_COLOR}|{Colors.RESET}", end='')
            else:
                print(f"{value:^{padding[key]}}{TABLE_COLOR}|{Colors.RESET}", end='')
        print()
        print(f"{TABLE_COLOR}+{'-'*(total_length-2)}+{Colors.RESET}")


    # Add space after printing the table
    print()