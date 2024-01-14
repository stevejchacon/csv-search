max_field_count = 0 
line_number_with_max_fields = 0 
line_number = 0 

# open file and loop through every line to determine the max number of columns in the file
####### change 'file.csv' to be the name of your specific csv file #######
with open('__file__.csv', 'r') as file:
    for line in file:
        line_number += 1 # increment line number/counter
        fields = line.strip().split(',') # all of the filed of the line in the csv
        field_count = len(fields) # count the number of fields in the line
        
        if field_count > max_field_count:
            max_field_count = field_count
            line_number_with_max_fields = line_number #  finds the line with the most fields (if necessary)

print(f"Line number {line_number_with_max_fields} has the most fields: {max_field_count} fields.")
