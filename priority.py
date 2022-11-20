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
            putting all those in temporary 
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
        t_time = Priority.calculateTurnaroundTime(self, process_data)
        b_time = Priority.calculateBlocked(self, process_data)
        Priority.printData(self, process_data, b_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time


    def calculateBlocked(self, process_data):
        total_blocked_time = 0
        for i in range(len(process_data)):
            blocked_time = process_data[i][5] - process_data[i][2]
            '''
             blocked is turnaround - burst 
            '''
            total_blocked_time = total_blocked_time + blocked_time
            process_data[i].append(blocked_time)
        average_blocked_time = total_blocked_time / len(process_data)
        '''
        average_blocked_time = total_blocked_time / no_of_processes
        '''
        return average_blocked_time


    def printData(self, process_data,average_blocked_time):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort according to the Process ID
        '''
        print("Process_ID  Arrival_Time  Burst_Time       Priority     Completion_Time      Blocked_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t\t\t")
            print()



        #print(f'Average Blocked Time: {average_blocked_time}')
