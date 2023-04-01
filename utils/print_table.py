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

