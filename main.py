import random
import threading
import time

shared_resource = dict.fromkeys(range(1, 21), 0)
# 20 properties and the value of each property is initialized to zero
print(shared_resource)

print("Hello ")
def executeProcess():
    pass

def addRecord():
    resource_record_id = random.randint(1, 20)
    resource_record_value = random.randint(1, 100)
    shared_resource[resource_record_id] = resource_record_value
    # assigning necessary values
def deleteRecord():
    resource_record_id = random.randint(1, 20)
    shared_resource[resource_record_id] = 0

def retrieveRecord():
    resource_record_id = random.randint(1, 20)
    print(shared_resource[resource_record_id])

def dataTotal():
    print(sum(shared_resource.values()))


def main():
    # shared resource list

    process_threads = list()
    for x in range(20):
        task_selector = random.randint(1, 4)
        # thread creation
        process_thread: threading.Thread
        if task_selector == 1:
            print("Thread is doing the task add record")
            # task 1 is to add a record
            process_thread = threading.Thread(target=addRecord)

        elif task_selector == 2:
            print("Thread is doing the task delete record")
            # task 2 is to delete a record
            process_thread = threading.Thread(target=deleteRecord)

        elif task_selector == 3:
            print("Thread is doing the task retrieve record")
            # task 3 is retrieve a record
            process_thread = threading.Thread(target=retrieveRecord)

        else:
            print("Thread is doing the task calculate record data total")
            # task 4 is calculate record data total
            process_thread = threading.Thread(target=dataTotal)
        process_threads.append(process_thread)
        # adding the new thread to the thread pool process threads
        process_thread.start()

    for thread in process_threads:
        thread.join()
        # every thread will finish execution before continuing
    print(shared_resource)
if __name__ == "__main__":
    main()
