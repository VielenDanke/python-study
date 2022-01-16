def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No first name or last name"
    return f"{format_text(f_name)} {format_text(l_name)}"


def format_name_title(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


def format_text(text):
    result_text = ""
    for idx in range(0, len(text)):
        if idx == 0:
            result_text += text[idx].upper()
            continue
        result_text += text[idx].lower()
    return result_text


print(f"Name formatted: {format_name('vLAd', 'dAnKeviCH')}")
