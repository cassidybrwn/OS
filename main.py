import random
print("Hello world")

class Priority:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))
            arrival_time = random.randint(0, 29)
            burst_time = random.randint(1, 5)

            priority = int(input(f"Enter Priority for Process {process_id}: "))


            temporary.extend([process_id, arrival_time,burst_time, priority])
            '''
            random generates arrival time 
            '''
            process_data.append(temporary)
        Priority.schedulingProcess(self, process_data)

        '''
            self refers to instance of the class
            '''

    def schedulingProcess(self, process_data):
        process_data.sort(key=lambda x: x[3], reverse=True)
        '''
        Sort according to Priority considering Higher the Value, Higher the Priority
        '''
        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(process_data)):
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            e_time = s_time
            exit_time.append(e_time)
            process_data[i].append(e_time)

        w_time = Priority.calculateWaitingTime(self, process_data)
        Priority.printData(self, process_data, w_time)




    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time


    def printData(self, process_data,average_waiting_time):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort according to the Process ID
        '''
        print("Process_ID  Arrival_Time  Burst_Time       Priority  Completion_Time    Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t\t\t")
            print()



        print(f'Average Waiting Time: {average_waiting_time}')


if __name__ == "__main__":
    no_of_processes = random.randint(1,4)
    priority = Priority()
    priority.processData(no_of_processes)
