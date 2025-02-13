# Grade-Satistic
# Grade Statistics Program

This program calculates and displays grade statistics for a university course based on student exam points and completed exercises.  It takes student data as input, calculates grades, and then presents statistics including average points, pass percentage, and grade distribution.

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

1. **Clone the repository:**  (If you're sharing the code on GitHub)
   ```bash
   git clone [https://github.com/your_username/your_repository.git](https://www.google.com/search?q=https://github.com/your_username/your_repository.git)
     
