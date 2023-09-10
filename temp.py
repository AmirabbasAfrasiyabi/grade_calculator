import csv
# For the average
from statistics import mean

# Calculating the average for each individual . 

def calculate_averages(input_file_name, output_file_name):

    with open(input_file_name, mode='r') as input_csv_file, open(output_file_name, mode='w') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        
        for row in csv_reader:
            name = row[0]
            # Convert grades to integers
            grades = [int(grade) for grade in row[1:]]
            average = mean(grades)
            csv_writer.writerow([name, average])

# Calculating the sorted average for each individual . 

def calculate_sorted_averages(input_file_name, output_file_name):

    with open(input_file_name, mode='r') as input_csv_file, open(output_file_name, mode='w') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        
        data = []
        for row in csv_reader:
            name = row[0]
            # Convert grades to integers
            grades = [int(grade) for grade in row[1:]]
            average = mean(grades)
            data.append((name, average))

        # Sort the data by average in ascending order
        sorted_data = sorted(data, key=lambda x: x[1])
        
        for item in sorted_data:
            csv_writer.writerow([item[0], item[1]])

def calculate_three_best(input_file_name, output_file_name):

    with open(input_file_name, mode='r') as input_csv_file, open(output_file_name, mode='w') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        
        data = []

        for row in csv_reader:
            name = row[0]
             # Convert grades to integers
            grades = [int(grade) for grade in row[1:]]
            average = mean(grades)
            data.append((name, average))
        
        # Sort the data by average in descending order

        sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
        top_three = sorted_data[:3]
        
        for item in top_three:
            csv_writer.writerow([item[0]])

# Calculating three worst for each individual .       

def calculate_three_worst(input_file_name, output_file_name):

    with open(input_file_name, mode='r') as input_csv_file, open(output_file_name, mode='w') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        
        data = []

        for row in csv_reader:
            name = row[0]
            # convert grades to integers
            grades = [int(grade) for grade in row[1:]]
            average = mean(grades)
            data.append((name, average))

        # Sort the data by average in ascending order
        
        sorted_data = sorted(data, key=lambda x: x[1])
        bottom_three = sorted_data[:3]
        
        for item in bottom_three:
            csv_writer.writerow([item[0]])

# "Calculating the average of averages for each individual" 

def calculate_average_of_averages(input_file_name, output_file_name):

    with open(input_file_name, mode='r') as input_csv_file, open(output_file_name, mode='w') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        
        averages = []
        for row in csv_reader:
            name = row[0]
            # Convert grades to integers
            grades = [int(grade) for grade in row[1:]]
            average = mean(grades)
            averages.append(average)
        
        overall_average = mean(averages)
        csv_writer.writerow([overall_average])

