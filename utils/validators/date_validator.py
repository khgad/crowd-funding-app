import datetime

class DateValidator:
    def __init__(self, date_format = "%Y-%m-%d"):
        self.date_format = date_format

    def is_valid(self, date_str, not_before = None, not_after = None):
        try:
            date = datetime.datetime.strptime(date_str, self.date_format)
            if not_before:
                not_before_date = datetime.datetime.strptime(not_before, self.date_format)
                if date <= not_before_date:
                    return (False, f"Invalid date, Please enter date that come after {not_before}.")
            if not_after:
                not_after_date = datetime.datetime.strptime(not_after, self.date_format)
                if date >= not_after_date:
                    return (False, f"Invalid date, Please enter date that come before {not_after}.")
                
            return (True, f"Valid date: {date.date()}.")

        except ValueError:
            return (False, "Invalid date. Please enter a valid date with format YYYY-MM-DD. ex: 2023-01-01")


    