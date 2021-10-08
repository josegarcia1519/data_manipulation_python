log_file = open("um-server-01.txt") #open log file that keep tracks of events


def sales_reports(log_file): #declare a function called sales_reports passing the argument "log_file"
    for line in log_file: # declares a for loop
        line = line.rstrip() #removes spaces at the end, result is stored in the variable line
        day = line[0:3] #creation of temp variable called day that stores arguments from line 
        if day == "Mon": #equal operator
            print(line) #print line if condition is true


sales_reports(log_file) #calls the function
