from temp import*

input_file = 'input_csv_courses.csv'
output_file = 'output_csv_courses.csv'

calculate_averages(input_file, 'averages.csv')
calculate_sorted_averages(input_file, 'sorted_averages.csv')
calculate_three_best(input_file, 'three_best.csv')
calculate_three_worst(input_file, 'three_worst.csv')
calculate_average_of_averages(input_file, 'average_of_averages.csv')