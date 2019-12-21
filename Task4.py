ts1 = [6, 1, 30]
ts2 = [6, 2, 10]

difference = (ts2[0] * 360 + ts2[1] * 60 + ts2[2]) - (ts1[0] * 360 + ts1[1] * 60 + ts1[2])

print(difference)


# ts1_seconds = ts1[0] * 360 + ts1[1] * 60 + ts1[2]
# ts2_seconds = ts2[0] * 360 + ts2[1] * 60 + ts2[2]



# a = 6 # часы
# a_ = a * 60 # минуты
# b = 1 # минуты
# b_ = b * 60 # секунды
# c = 30
# x = a_ * b_ + (b * 60) + c
# print(x)

# x = 1
# a = x * 60
# b = a * 60
# c1 = b * 6 + a + x * 30
# c2 = b * 6 + a * 2 + x * 10
# c3 = c2 - c1
# print(c3)



# from datetime import datetime, timedelta
# a = datetime(2010, 12, 12)
# b = timedelta(days=1, hours=2, seconds=15)
# str(a)
# '2010-12-12 00:00:00'
# c = str(a+b)
# '2010-12-13 02:00:15'

# print(c)

# from datetime import datetime, timedelta
# # timestamp1 = datetime(2010, 12, 12)
# timestamp1 = timedelta(hours=1, minutes=5, seconds=10)
# timestamp2 = timedelta(hours=2, minutes=15, seconds=15)

# hours_ = hours * 60
# minutes_ = minutes * 60

# str(timestamp1)
# c = str(timestamp2 - timestamp1)
# print(c)


# timestamp1 = input()