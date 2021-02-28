import random, datetime, smtplib

current_day = datetime.datetime.today().weekday()

if datetime.datetime.today().weekday() == 0:
    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login("baczkowskifranek@gmail.com", "abcd()1234")
        conn.sendmail("baczkowskifranek@gmail.com", "kraszka1234@yahoo.com", f"monday motivational quote\n\n{quote}")
        conn.close()

