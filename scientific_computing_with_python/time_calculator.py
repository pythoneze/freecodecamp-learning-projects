def add_time(start, duration, start_day=None):
    # List of days for indexing
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Split start time into clock and AM/PM
    time_part, period = start.strip().split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert to 24-hour format
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    if period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.strip().split(':'))
    total_duration_minutes = dur_hour * 60 + dur_minute

    # Total time in minutes
    total_start_minutes = start_hour * 60 + start_minute
    total_minutes = total_start_minutes + total_duration_minutes

    # Calculate number of days passed
    days_later = total_minutes // (24 * 60)
    total_minutes %= 24 * 60  # Remaining minutes for display

    # Convert back to hour and minute
    final_hour = total_minutes // 60
    final_minute = total_minutes % 60

    # Convert back to 12-hour format
    if final_hour == 0:
        display_hour = 12
        display_period = 'AM'
    elif final_hour < 12:
        display_hour = final_hour
        display_period = 'AM'
    elif final_hour == 12:
        display_hour = 12
        display_period = 'PM'
    else:
        display_hour = final_hour - 12
        display_period = 'PM'

    # Start building the new_time string
    new_time = f"{display_hour}:{final_minute:02d} {display_period}"

    # Add day of week if given
    if start_day:
        start_day = start_day.lower()
        if start_day in days:
            new_day_index = (days.index(start_day) + days_later) % 7
            new_day = days[new_day_index].capitalize()
            new_time += f", {new_day}"

    # Add day information
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
