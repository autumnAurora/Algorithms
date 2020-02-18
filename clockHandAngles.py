import math

'''
# The minute hand travels 360 degrees in 60 minutes. Per minute: 360/60 = 6 deg/min
# The hour hand travels 360 degrees in 12 hours. Per minute: 360/12/60 = 0.5 deg/min
# From Above, we know that the hour hand travels 30 deg/hr
'''
CIRCLE = 360
minuteHandDPM = 6
hourHandDPM = 0.5
hourHandDPH = 30


'''
Returns the absolute angle between the hour hand and minute on a clock for the given time.
Args:
    time: (Str) The time to be represented.
Returns:
    angle: (Float) The angle.
'''
def clockHandAngle(time):
    time = (time.strip().split(":"))
    hour = int(time[0])
    minute = int(time[1])

    # The hour hand angle is the base angle + an offset (between two numbers)
    hourBaseAngle = hour * hourHandDPH
    hourOffset = minute * hourHandDPM
    absoluteHourAngle = hourBaseAngle + hourOffset

    # The minute hand angle calculation is trivial
    absoluteMinuteAngle = minute * minuteHandDPM

    difference = abs(absoluteHourAngle - absoluteMinuteAngle)
    return min((CIRCLE - difference), difference)


if __name__ == "__main__":
    times = ["12:37", "1:24", "7:03", "8:49"]
    for time in times:
        print(time + ": " + str(clockHandAngle(time)) + " degrees")
