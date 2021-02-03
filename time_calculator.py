def add_time(start, duration, weekday=None):
  ### If you want to find what day of the week you want you have to pass in what day to start with. ###
    day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if weekday is not None:
        weekday = weekday.lower().capitalize()
        for day_o_week in day_of_week:
            if weekday == day_o_week:
                weekday = day_of_week.index(weekday)

    # breaking down the start time for ease of use later.
    for t in start:
        if t == ":":
            break_time = start.split(':')
            start_hour = break_time[0]
            for minutes in break_time[1]:
                if minutes == ' ':
                    minute = break_time[1].split(' ')
                    start_minutes = minute[0]
                if minutes == 'P':
                    period_of_day = 'PM'
                    start_hour = (int(start_hour) + 12)
                if minutes == 'A':
                    period_of_day = 'AM'

    # Break down the duration
    for hours in duration:
        if hours == ':':
            add_hours = duration.split(':')
            amount_hours = add_hours[0]
            amount_minutes = add_hours[1]
            amount_days = 0

    if int(amount_minutes) >= 60:
        amount_hours = (int(amount_hours) + (int(amount_minutes) // 60))
        amount_minutes = (int(amount_minutes % 60))
    elif int(amount_hours) >= 24:
        amount_days = (int(amount_hours) // 24)
        amount_hours = (int(amount_hours) % 24)

    total_hours = (int(start_hour) + int(amount_hours))
    total_minutes = (int(start_minutes) + int(amount_minutes))
    days = amount_days

    # Calculating and formatting minutes.
    if int(total_minutes) >= 60:
        total_hours = (int(total_hours) + (int(total_minutes) // 60))
        sixty_min_format = (int(total_minutes) % 60)
        if int(sixty_min_format) < 10:
            sixty_min_format = str('0' + str(sixty_min_format))
    else:
        sixty_min_format = total_minutes
        if int(sixty_min_format) < 10:
            sixty_min_format = ('0' + str(sixty_min_format))

    # Calculating and formatting hours.
    if int(total_hours) >= 24:
        days = (int(amount_days) + (int(total_hours) // 24))
        twentyfour_hr_format = (int(total_hours) % 24)
        if int(twentyfour_hr_format) > 12:
            twelve_hr_format = (int(twentyfour_hr_format) - 12)
        if int(twentyfour_hr_format) <= 12:
            twelve_hr_format = (twentyfour_hr_format)
    if int(total_hours) <= 24:
        twentyfour_hr_format = total_hours
        if int(twentyfour_hr_format) > 12:
            twelve_hr_format = (int(twentyfour_hr_format) - 12)
        if int(twentyfour_hr_format) <= 12:
            twelve_hr_format = (twentyfour_hr_format)

    # Determining AM or PM.
    period_of_day = 0
    if int(twentyfour_hr_format) == 24:
        period_of_day = ' AM'
    elif int(twentyfour_hr_format) >= 12:
        period_of_day = " PM"
    elif int(twentyfour_hr_format) < 12:
        period_of_day = " AM"

    # Calculating how many days if any have passed.
    if int(days) == 1:
        days_passed = ('(next day)')
    if int(days) > 1:
        days_passed = ('(' + str(days) + ' days later)')

    # Calculating the weekday if its asked.
    if weekday is not None:
      if int(days) >= 7:
        dayofweek = (int(days) % 7)
        weekday = (int(weekday) + int(dayofweek))
        if int(weekday) >= 7:
            weekday = (int(weekday) % 7)
            weekday = ((int(weekday)))
        calculated_weekday = day_of_week[weekday]
      if int(days) < 7:
        weekday = (int(weekday) + int(days))
        if int(weekday) >= 7:
            weekday = (int(weekday) % 7)
            weekday = ((int(weekday)))
        calculated_weekday = day_of_week[weekday]

    # Formatting the solutions.
      if int(days) == 0:
        new_time = (str(twelve_hr_format) + ':' + str(sixty_min_format) + str(period_of_day) + ',' + ' ' + str(calculated_weekday))
      else:
        new_time = (str(twelve_hr_format) + ':' + str(sixty_min_format) + str(period_of_day) + ',' + ' ' + str(calculated_weekday) + ' ' +str(days_passed))
    else:
      if int(days) == 0:
        new_time = (str(twelve_hr_format) + ':' + str(sixty_min_format) + str(period_of_day))
      else:
        new_time = (str(twelve_hr_format) + ':' + str(sixty_min_format) + str(period_of_day) + ' ' + str(days_passed))

    return new_time
