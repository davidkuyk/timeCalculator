def add_time(start, duration, dayofweek=""):
    # get hours from start using regex
    # get minutes from start using regex
    # get amPm from start using regex
    if len(start) == 7:
        startHour = int(start[0])
        startMinute = int(start[2:4])
        amPm = start[5:7]
    elif len(start) == 8:
        startHour = int(start[0:2])
        startMinute = int(start[3:5])
        amPm = start[6:8]
    # get hours from duration using regex
    # get minutes from duration using regex
    durationHour = int(duration[:-3])
    durationMinute = int(duration[-2:])
    
    # get duration in total minutes
    durationTotal = (durationHour * 60) + durationMinute
    
    # get start in total minutes
    if amPm == 'AM':
        startTotal = (startHour * 60) + startMinute
    else:
        startTotal = ((startHour+12) * 60) + startMinute
    
    daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # convert dayofweek to number:
    if dayofweek != None and dayofweek != '':
        dowNum = daysOfWeek.index(dayofweek[0].upper() + dayofweek[1:].lower())
    else:
        dowNum = None

    dayIncrement = 0
    resultTotal = startTotal
    # start adding the durationTotal to the resultTotal. 
    while durationTotal > 0:
        resultTotal += 1
        durationTotal -= 1
        if resultTotal == 1440:
            if dayofweek != None and dayofweek != '':
                if dowNum == 6:
                    dowNum = 0
                else:
                    dowNum += 1
            dayIncrement += 1
            resultTotal = 00
    if resultTotal > 719:
        resultAmPm = "PM"
    else:
        resultAmPm = "AM"
    # divide resulting number by 60 and make the remainder the resultMinutes
    if resultTotal < 60:
        resultHour = '00'
        resultMinute = resultTotal
    else:
        resultMinute = resultTotal % 60
        resultHour = resultTotal // 60

        if resultHour > 12:
            resultHour = str(resultHour - 12)
        else:
          resultHour = str(resultHour)
    if resultHour == "00":
      resultHour = "12"

    if resultMinute < 10:
        resultMinute = '0' + str(resultMinute)
    else:
        resultMinute = str(resultMinute)

    if dayofweek != None and dayofweek != '':
        resultDow = ", " + daysOfWeek[dowNum]
    else:
      resultDow = ""

    if dayIncrement == 1:
        dayChange = " (next day)"
    elif dayIncrement > 1:
        dayChange = " (" + str(dayIncrement) + " days later)"
    else:
        dayChange = ''

    new_time = resultHour + ":" + resultMinute + " " + resultAmPm + resultDow + dayChange 
    return new_time