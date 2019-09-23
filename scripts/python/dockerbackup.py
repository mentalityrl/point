#!/usr/bin/env python
from subprocess import Popen
from os.path import isdir
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Target directories.
source = "/mnt/docker"
destination = "/mnt/pool/Backups/Docker"
archive = "{destination}/{date}.tar.gz".format(destination=destination, date=current_date)
log_file = "{destination}/{log_name}".format(destination=destination, log_name="backup.log")

# Check if target directories both exist and are actually directories.
source_exists = isdir(source)
destination_exists = isdir(destination)

with open(log_file, "a+") as log:
    if source_exists and destination_exists: # Check if both directories exist and are actually directories before proceeeding
        print("Backing up Docker folders")
        date = current_date # Grab the current time
        log.write("Backup Started at " + date + "\n") # Write when the backup started
        log.write("Stopping ALL running containers " +  "\n\n") # Write when the backup started
        print("Stopping all running containers...")
        dockerDown = Popen(["systemctl", "stop", "docker.service"])
        dockerDown.wait()
        print("Containers stopped: Proceeding to backup")
        log.flush() # Flush the write buffer to log file
        tar = Popen(["tar", "-pczf", archive, source], stdout=log, stderr=log) # Tar directory and write output to log file
        tar.wait() # Wait for tar process to finish
        log.write("\n") # Write a new line to log for formatting purposes
        log.flush() # Flush the buffer to log again
        print("Bringing containers back online")
        log.write("Bringing containers back online" + "\n")
        dockerUp = Popen(["systemctl", "start", "docker.service"])
        dockerUp.wait()
        date = current_date # Grab the current time again
        log.write("Backup Finished at " + date + "\n\n") # Write when the backup finished
        log.write("-------------------------------------------------\n\n") # Write a new line to log for formatting purposes
        log.flush() # Flush the buffer to log again
        log.close() # Close the log file
        print("Backup Complete")

    elif not source_exists:
        log.write("Source folder could not be found!")
        log.flush() # Flush the write buffer to log file
        log.close() # Close the log file
        print("Source folder cloud not be found")

    elif not destination_exists:
        log.write("Destination folder could not be found!")
        log.flush() # Flush the write buffer to log file
        log.close() # Close the log file
        print("Destination folder could not be found")

    else:
        log.write("The source AND the destination folders could not be found!")
        log.flush() # Flush the write buffer to log file
        log.close() # Close the log file
        print("Destination and source folders could not be found")
