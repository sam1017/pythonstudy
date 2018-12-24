from random import randint
class Customer(object):
    def __init__(self, arrived_time):
        self.arrived_time = arrived_time

    def set_status(self, status):
        self.status = status

    def set_queqe_number(self,queqe_number):
        self.queqe_number = queqe_number

    def set_start_process_time(self, start_process_time):
        self.start_process_time = start_process_time

    def set_end_process_time(self, end_process_time):
        #end_process_time = self.start_process_time + randint(5,30)
        self.end_process_time = end_process_time

    def get_arrived_time(self):
        return self.arrived_time

    def show(self):
        print("this customer arrived : " + str(self.arrived_time) + " stand by queue : " + str(self.queqe_number) + " waiting until: " + str(self.start_process_time) + " leave bank at : " + str(self.end_process_time))

class Event_type(object):
    def __init__(self, event_type, occur_time):
        self.event_type = event_type
        self.occur_time = occur_time
    def get_occur_time(self):
        return self.occur_time
    def get_event_type(self):
        return self.event_type

def find_minimal_queue(queue_list):
    min_len = 99
    index = 0
    found_index = 0
    for queue in queue_list:
        if len(queue) == 0:
            return index
        elif len(queue) < min_len:
            min_len = len(queue)
            found_index = index
        index = index + 1
    if found_index < len(queue_list) and found_index >= 0:
        return found_index

def insert_new_event(new_event, event_queue):
    print("insert new event type = " + str(new_event.get_event_type()) + " occur_time = " + str(new_event.get_occur_time()))
    for value in range(0, len(event_queue)):
        if event_queue[value].get_occur_time() > new_event.get_occur_time():
            event_queue.insert(value, new_event)
            #print("insert new event at : " + str(value))
            return None
    event_queue.append(new_event)
    print("insert new event at end : " + str(len(event_queue)))

def customerarrived(occur_time, queue_list, event_queue):
    new_customer = Customer(occur_time)
    queue_index = find_minimal_queue(queue_list)
    print("customerarrived : " + str(occur_time))
    print("find_minimal_queue  : " + str(queue_index + 1))
    new_customer.set_queqe_number(queue_index+1)
    queue_list[queue_index].append(new_customer)
    if len(queue_list[queue_index]) == 1:
        queue_list[queue_index][0].set_start_process_time(occur_time)
        new_event = Event_type(queue_index + 1, occur_time + randint(1,30))
        insert_new_event(new_event, event_queue)
    new_customer_time = occur_time + randint(1,5)
    if new_customer_time < 180:
        new_event = Event_type(0, new_customer_time)
        insert_new_event(new_event, event_queue)

def customerdeparture(event, queue_list, event_queue, customers):
    print("this customer departure at : " + str(event.get_occur_time()) + " from queue : " + str(event.get_event_type()))
    queue_index = event.get_event_type() - 1;
    queue_list[queue_index][0].set_end_process_time(event.get_occur_time())
    customers.append(queue_list[queue_index][0])
    del queue_list[queue_index][0]
    if len(queue_list[queue_index]) > 0:
        queue_list[queue_index][0].set_start_process_time(event.get_occur_time())
        new_event = Event_type(event.get_event_type(), event.get_occur_time() + randint(1,30))
        insert_new_event(new_event, event_queue)

def getCustomerArrivedTime(elem):
    return elem.get_arrived_time()

begin_time = 0
close_time = 100
event_queue = [Event_type(0,begin_time)]
queue_list = []
customers = []
for queue_number in range(4):
    new_queue = []
    queue_list.append(new_queue)

while len(event_queue) > 0 :
    event = event_queue[0]
    if event.event_type == 0:
        customerarrived(event.get_occur_time(), queue_list, event_queue)
    else:
        customerdeparture(event, queue_list, event_queue, customers)
    del event_queue[0]

customers.sort(key = getCustomerArrivedTime)
for customer in customers:
    customer.show()