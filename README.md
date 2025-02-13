# Grade-Satistic
# Grade Statistics Program

This program calculates and displays grade statistics for a university course based on student exam points and completed exercises.  It takes student data as input, calculates grades, and then presents statistics including average points, pass percentage, and grade distribution.

**Note:** I'm a beginner programmer, and this is my first project. I'm excited to learn and improve my skills, so any feedback or suggestions are welcome!

## Features

* **Input:** Accepts student data in the format "exam points exercises completed" (e.g., "15 87").  Input continues until an empty line is entered.
* **Exercise Points:** Converts completed exercises (0-100) into exercise points (0-10) based on percentage completed (10% = 1 point, 20% = 2 points, etc.).
* **Grade Calculation:** Calculates the final grade based on the sum of exam points and exercise points, according to the following table:

| Total Points | Grade |
|---|---|
| 0–14 | 0 (Fail) |
| 15–17 | 1 |
| 18–20 | 2 |
| 21–23 | 3 |
| 24–27 | 4 |
| 28–30 | 5 |

* **Exam Cutoff:** Students with less than 10 exam points automatically fail, regardless of total points.
* **Statistics:** Displays the following statistics:
    * Average total points (exam points + exercise points).
    * Pass percentage (percentage of students with a passing grade).
    * Grade distribution (histogram showing the number of students in each grade category).

## How to Use

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/YankeyNwolle/Grade-Statistics.git

## Example Input and Output
Exam points and exercises completed: 15 87
Exam points and exercises completed: 10 55
Exam points and exercises completed: 11 40
Exam points and exercises completed: 4 17
Exam points and exercises completed: 18 95
Exam points and exercises completed: 12 60
Exam points and exercises completed:
Statistics:
Points average: 18.2
Pass percentage: 83.3
Grade distribution:
5: *
4: **
3: *
2: *
1: *
0:

2. **Contributing:**

   ## Contributing

Contributions are welcome! Since I'm still learning, I would especially appreciate feedback on my code, including suggestions for improvements or best practices. Please submit a pull request if you'd like to contribute.

3. **Author**
## Author

**P.S.** I'm a beginner in programming, and this is my first project. I'm eager to learn and grow, so any feedback or guidance would be greatly appreciated! 
of course Python programming Mooc 2025

4. **THANK YOU**
