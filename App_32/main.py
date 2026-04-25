import smtplib

email = "saadpy15@gmail.com"
password = "fwps zond rhpz bimk"
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs="sumaiya.hassan151@gmail.com", msg="I sent this using Python smtplib.")
connection.close()
