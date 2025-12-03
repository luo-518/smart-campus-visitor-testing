bookings = []
blacklist = ["张三"]

def add_booking(record):
    bookings.append(record)

def get_all_bookings():
    return bookings

def find_booking_by_code(code):
    for b in bookings:
        if b["visitor_code"] == code:
            return b
    return None

