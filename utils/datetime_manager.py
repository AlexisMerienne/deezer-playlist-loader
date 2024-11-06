from datetime import datetime, timedelta


def get_previous_day_timestamp(days=1):
    # Get the current date and time
    now = datetime.now()

    # Subtract one day from the current date
    previous_day = now - timedelta(days=days)

    # Replace hour, minute, second, and microsecond to get midnight
    previous_day_midnight = previous_day.replace(hour=0, minute=0, second=0, microsecond=0)

    # Convert to timestamp
    timestamp = int(previous_day_midnight.timestamp())

    return timestamp

def is_less_than_24h(timestamp1, timestamp2):
    # Calculate the difference in seconds between the two timestamps
    difference = abs(timestamp1 - timestamp2)
    
    # Check if the difference is less than 24 hours (24 hours * 60 minutes * 60 seconds)
    return difference < 24 * 60 * 60