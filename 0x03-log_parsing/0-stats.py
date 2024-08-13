#!/usr/bin/python3
import sys
import signal

"""
This script reads log lines from standard input, computes various metrics, and prints statistics.
The input format is expected to be: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>.

"""

def print_statistics(total_size, status_counts):
   
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def handle_interrupt(signum, frame):
   
    print("\nKeyboard interrupt detected. Printing statistics.")
    print_statistics(total_size, status_counts)
    sys.exit(0)

# Register the signal handler for keyboard interrupt
signal.signal(signal.SIGINT, handle_interrupt)

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Read from stdin line by line
for line in sys.stdin:
    line_count += 1
    
    # Parse the line
    parts = line.split()
    
    # Ensure the line matches the expected format
    if len(parts) >= 6 and parts[1].startswith('[') and parts[3].startswith('"GET'):
        try:
            file_size = int(parts[5])
            status_code = int(parts[3].split()[1])
            
            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            # Skip line if there's a parsing error
            continue
    
    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics(total_size, status_counts)

# Print final statistics if the script completes without interruption
print_statistics(total_size, status_counts)
