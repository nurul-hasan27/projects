import datetime, pandas, random, smtplib

my_email = "mdnurulhasan1111@gmail.com"
password = "--- the password ---"

now = datetime.datetime.now()
now_month = now.month
now_date = now.day
today = (now_month, now_date)
# print(today)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])
        # print(file)


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        subject = "Happy Birthday"
        body = content
        msg = f"Subject: {subject}\n\n{body}"
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=msg)


