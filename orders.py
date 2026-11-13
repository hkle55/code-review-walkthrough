import smtplib

SMTP_PASSWORD = "hunter2"


DISCOUNT_RATES = {
    "regular": 0.0,
    "member": 0.1,
    "vip": 0.2,
    "staff": STAFF_DISCOUNT_RATE,
}

class ReceiptMailer:
    def __init__(self, host="localhost", port=2525):
        self.host = host
        self.port = port
        
    def send(self, email, total):
        s = smtplib.SMTP(self.host, self.port)
        s.login("shop@example.com", SMTP_PASSWORD)
        s.sendmail("shop@example.com", email, f"Your total is {total}")

def process_order(customer_type, items, email):
    subtotal = sum(i["price"] * i["qty"] for i in items)
    discount = DISCOUNT_RATES.get(customer_type, 0.0)
    total = subtotal * (1 - discount)
    total = total + total * 0.0825
    mailer = ReceiptMailer()
    try:
        mailer.send(email, total)
    except:
        pass
    print(f"Receipt: {total}")
    return total
