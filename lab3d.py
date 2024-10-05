#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: ajjayaratnam

import subprocess

def free_space():
    # Run the 'df' command and capture its output
    process = subprocess.Popen(['df', '-h', '/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    # Decode the output, split lines, and fetch the desired free space value
    output = stdout.decode('utf-8').strip()
    
    # Find the correct line with root (/) filesystem information
    lines = output.splitlines()
    # Extract the available free space value from the last column
    root_line = lines[1]
    free_space_value = root_line.split()[3]  # The 4th column is the available space
    
    return free_space_value

if __name__ == '__main__':
    print(free_space())

