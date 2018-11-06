class BOL:
    def __init__(self, bill_id, date, bill_number, shipper_name, user_name, rate, rate_type, origin, destination, loads, start_time, end_time, hours_worked):
        self.bill_id = bill_id
        self.date = date
        self.bill_number = bill_number
        self.shipper_name = shipper_name
        self.user_name = user_name
        self.origin = origin
        self.destination = destination
        self.loads = loads
        self.start_time = start_time
        self.end_time = end_time
        self.hours_worked = hours_worked
        self.rate = rate
        self.rate_type = rate_type