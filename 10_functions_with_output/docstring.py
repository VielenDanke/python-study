# Return name
def format_name(name):
    """Take a name and format it with logic:
    If char at index in argument name % 2 == 0 - upper case letter would be placed
    If char at index in argument name % 2 != 0 - lower case letter would be placed"""
    result = ""
    for idx in range(0, len(name)):
        if idx % 2 == 0:
            result += name[idx].upper()
            continue
        result += name[idx].lower()
    return result
