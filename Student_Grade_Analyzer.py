import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# Generate sample CSV if it doesn't exist
csv_filename = "student_scores.csv"
if not os.path.exists(csv_filename):
    headers = ['Name', 'Math', 'Science', 'English']
    students = [
        ['Ali', 92, 88, 94],
        ['Sara', 78, 85, 80],
        ['Reza', 85, 90, 82],
        ['Niloofar', 95, 98, 96],
        ['Mohammad', 60, 70, 65],
        ['Hana', 88, 84, 90],
        ['Sina', 72, 75, 70],
        ['Mina', 89, 92, 91],
        ['Kaveh', 55, 60, 58],
        ['Elina', 99, 97, 100],
    ]

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(students)

# Load and clean data
names = []
scores = []

with open(csv_filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        try:
            name = row[0]
            values = list(map(float, row[1:]))
            if len(values) == 3:
                names.append(name)
                scores.append(values)
        except ValueError:
            continue

scores_np = np.array(scores)

# Compute statistics
mean_scores = np.mean(scores_np, axis=0)
max_scores = np.max(scores_np, axis=0)
min_scores = np.min(scores_np, axis=0)
student_averages = np.mean(scores_np, axis=1)
best_index = np.argmax(student_averages)
best_student = names[best_index]

# Plot 1: Line chart for average scores per subject
subjects = header[1:]
plt.figure(figsize=(6, 4))
plt.plot(subjects, mean_scores, marker='o', label='Average Score')
plt.title("Average Score Per Subject")
plt.ylabel("Score")
plt.grid(True)
plt.legend()
plt.savefig("/mnt/data/line_chart.png")
plt.close()

# Plot 2: Bar chart of best student's scores
plt.figure(figsize=(6, 4))
plt.bar(subjects, scores_np[best_index], color='orange')
plt.title(f"{best_student}'s Scores")
plt.ylabel("Score")
plt.savefig("/mnt/data/bar_chart.png")
plt.close()

# Plot 3: Pie chart of average subject contributions
plt.figure(figsize=(6, 6))
plt.pie(mean_scores, labels=subjects, autopct='%1.1f%%', startangle=140)
plt.title("Average Subject Distribution")
plt.savefig("/mnt/data/pie_chart.png")
plt.close()

# Plot 4: Histogram of all student averages
plt.figure(figsize=(6, 4))
plt.hist(student_averages, bins=5, color='green', edgecolor='black')
plt.title("Distribution of Student Averages")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.savefig("/mnt/data/histogram.png")
plt.close()

# Summary Output
summary = f"""
📊 DATA REPORT: Student Scores
------------------------------
✔ Total Records: {len(names)}
✔ Average Scores:
  - Math: {mean_scores[0]:.2f}
  - Science: {mean_scores[1]:.2f}
  - English: {mean_scores[2]:.2f}
✔ Best Student: {best_student} (Avg: {student_averages[best_index]:.2f})

📁 Charts Saved:
- line_chart.png
- bar_chart.png
- pie_chart.png
- histogram.png
"""
summary += "\n\nWould you like to filter scores above a threshold (e.g., >85)?"

summary.strip()
