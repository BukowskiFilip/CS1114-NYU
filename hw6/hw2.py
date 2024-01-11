
def get_decimal_time(hr, min, sec):
    user_hour_in_seconds = (hr) * (60) * (60)
    user_minutes_in_seconds = (min) * (60)
    user_total = (user_hour_in_seconds) + (user_minutes_in_seconds) + (sec)
    hours_in_french = (100 * 100)
    french_time = user_total // hours_in_french
    user_total = user_total % hours_in_french
    french_time_2 = user_total // (100)
    user_total = user_total % (100)
    return(f"{french_time}:{french_time_2}:{user_total}")

def get_decimal_date(month, day, year):
    french_revolutionary_year = 1792
    if month == 1:
        french_revolutionary_month = "NivÃ´se"
    elif month == 2:
        french_revolutionary_month = "PluviÃ´se"
    elif month == 3:
        french_revolutionary_month = "VentÃ´se"
    elif month == 4:
        french_revolutionary_month = "Germinal"
    elif month == 5:
        french_revolutionary_month = "FlorÃ©al"
    elif month == 6:
        french_revolutionary_month = "Prairial"
    elif month == 7:
        french_revolutionary_month = "Messidor"
    elif month == 8:
        french_revolutionary_month = "Thermidor"
    elif month == 9:
        french_revolutionary_month = "Fructidor"
    elif month == 10:
        french_revolutionary_month = "VendÃ©miaire"
    elif month == 11:
        french_revolutionary_month = "Brumaire"
    else:
        french_revolutionary_month = "Frimaire"
    if  0 < day <= 10:
        french_dÃ©cade = 1
    if  10 < day <= 20:
        french_dÃ©cade = 2
    else:
        french_dÃ©cade = 3
    return (f"{day} {french_revolutionary_month} Year {year - french_revolutionary_year}, DÃ©cade {french_dÃ©cade}")

def get_french_datetime(gregorian_datetime):

    first_colon = gregorian_datetime.find(":")
    second_colon = gregorian_datetime.find(":", first_colon + 1)

    hr = int(gregorian_datetime[0:first_colon])

    min = int(gregorian_datetime[first_colon + 1:second_colon])
    find_space = gregorian_datetime.find(" ", second_colon + 1)
    sec = int(gregorian_datetime[second_colon + 1: find_space])

    first_slash = gregorian_datetime.find('/')
    second_slash = gregorian_datetime.find("/", first_slash + 1)

    month = int(gregorian_datetime[find_space: first_slash])
    day = int(gregorian_datetime[first_slash + 1:second_slash])
    year = int(gregorian_datetime[second_slash + 1:])

    time_variable = get_decimal_time(hr, min, sec)
    date_variable = get_decimal_date(month, day, year)

    return (f"{time_variable}\n{date_variable}")

