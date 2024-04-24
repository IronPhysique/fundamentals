
import statistics
data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(',')

grades = list(map(int, grades))

min_grade = min(grades)
max_grade = max(grades)
print("Minimum Grade:", min_grade)
print("Maximum Grade:", max_grade)

average = sum(grades) / len(grades)
print("Average Grade:", round(average, 2))

mean_grade = statistics.mean(grades)
median_grade = statistics.median(grades)

print("Mean Grade:", round(mean_grade, 2))
print("Median Grade:", median_grade)

output = "Min: {}, Max: {}, Average: {:.2f}, Mean: {:.2f}, Median: {}".format(min_grade, max_grade, average, mean_grade, median_grade)
print(output)
