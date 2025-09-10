import os 
import sys


log_string = """
A-0007,4090,7,0,0.1722,17.590395551990024,102.0,OK,2021-06-18 00:07:40
A-0007,4090,7,0,0.5296,43.45677011504327,107.0,OK,2021-06-18 00:15:44
A-0007,4090,7,0,0.8817,52.762711669599724,102.0,WARNING,2021-06-18 00:43:33
A-0007,4090,7,0,0.2175,25.67431905287205,108.0,OK,2021-06-18 01:35:35
A-0007,4090,7,0,0.73,43.851165573720664,98.0,OK,2021-06-18 01:46:06
A-0007,4090,7,0,0.3604,40.06330698212658,89.0,OK,2021-06-18 01:49:15
"""

Log = [line.split(',') for line in log_string.strip().split('\n')]

class StatusFilter:
    def filter_by_status(log_list, status):
        return [entry for entry in log_list if entry[7].strip().upper() == status.upper()]

class LogTracker:
    def __init__(self):
        self.count_4090 = []
        self.count_H100 = []
        self.count_A100 = []
        self.count_T5 = []
        self.count_CUDA = []
    def process_log(self, log_str):
        lines = log_str.strip().split('\n')
        for line in lines:
            parts = line.split(',')
            if len(parts) > 1 and parts[1].strip() == '4090':
                self.count_4090.append(1)
            elif len(parts) > 1 and parts[1].strip() == 'H100':
                self.count_H100.append(1)
            elif len(parts) > 1 and parts[1].strip() == 'A100':
                self.count_A100.append(1)
            elif len(parts) > 1 and parts[1].strip() == 'T5':
                self.count_T5.append(1)
            elif len(parts) > 1 and parts[1].strip() == 'CUDA':
                self.count_CUDA.append(1)
    def get_count(self):
        return {
            "4090": len(self.count_4090),
            "H100": len(self.count_H100),
            "A100": len(self.count_A100),
            "T5": len(self.count_T5),
            "CUDA": len(self.count_CUDA),
    }

    def get_list(self):
        return self.count_4090

filtered_by_warning = StatusFilter.filter_by_status(Log, "WARNING")
for row in filtered_by_warning:
    print(row)
type = LogTracker()
type.process_log(log_string)

print("GPU INV by Type:", type.get_count())

