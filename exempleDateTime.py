from datetime import datetime, timedelta

original_time = datetime(2023, 3, 14, 9, 26)
added_time = original_time + timedelta(minutes=90)
print(added_time)