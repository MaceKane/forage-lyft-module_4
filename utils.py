# Defining a function called "add_years_to_date".
def add_years_to_date(original_date, years_to_add):
    # Creating a new datetime object called "result" that is equal to the original date plus the specified number of years.
    result = original_date.replace(year=original_date.year + years_to_add)
    # Returning the "result" datetime object.
    return result
