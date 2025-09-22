import datetime

today = datetime.date.today()


for month in range(1, 13):
    next_date = today + datetime.timedelta(days=30)
    print("Installment Pending Alert!!!", next_date)
    today = next_date

