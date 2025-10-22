import sys

# =========================
# DECORATORS FOR COURSES
# =========================
def course1(func):
    def wrapper():
        # Course 1 weights
        weights = {
            'assignments': 40,
            'quizzes': 10,
            'midterm': 15,
            'final': 35
        }
        # Grades (all None initially)
        done_assignments = [100]
        assignments = done_assignments + [90, 70, 90, 90, 90]
        quizzes = 93
        midterm = 12
        final = None
        return func(weights, assignments, quizzes, midterm, final)
    return wrapper


def course2(func):
    def wrapper():
        # Course 2 weights
        weights = {
            'assignments': 30,
            'midterm': 20,
            'final': 50
        }
        # Grades (all None initially)
        done_assignments = [93, 95]
        assignments = done_assignments + [90, 90, 90, 90]
        midterm = 12
        final = None
        return func(weights, assignments, None, midterm, final)
    return wrapper


# =========================
# CORE GRADE CALCULATION
# =========================
def calculate_needed_final(weights, assignments, quizzes, midterm, final, desired_grade=50):
    """
    Calculates required final grade given partial grades and weights.
    All unknown (None) grades are ignored in current average computation.
    """
    total_weight_done = 0
    total_score = 0

    def avg(lst):
        valid = [x for x in lst if x is not None]
        return sum(valid) / len(valid) if valid else None

    # Assignments
    assignments_avg = avg(assignments)
    if assignments_avg is not None:
        total_weight_done += weights['assignments']
        total_score += assignments_avg * (weights['assignments'] / 100)

    # Quizzes
    if quizzes is not None:
        # uncomment if quizzes is a list
        # quizzes_avg = avg(quizzes)
        # if quizzes_avg is not None:
        #    total_weight_done += weights['quizzes']
        #    total_score += quizzes_avg * (weights['quizzes'] / 100)
        total_weight_done += weights['quizzes']
        total_score += quizzes * (weights['quizzes'] / 100)

    # Midterm
    if midterm is not None:
        total_weight_done += weights['midterm']
        total_score += midterm * (weights['midterm'] / 100)

    # If final already known, compute overall grade
    if final is not None:
        total_score += final * (weights['final'] / 100)
        return f"Final grade already known. Overall score: {total_score:.2f}"

    # Compute what is needed in final to reach desired grade
    remaining_weight = 100 - total_weight_done - weights['final']
    if remaining_weight < 0:
        remaining_weight = 0

    current_score = total_score
    needed_final = (desired_grade - current_score) / (weights['final'] / 100)
    # needed_final = (desired_grade / 100 - current_score) * 100 / (weights['final'] / 100)

    return f"To achieve {desired_grade}% overall, you need {needed_final:.2f}% in the final exam."


# =========================
# COURSE DEFINITIONS
# =========================
@course1
def course_A(weights, assignments, quizzes, midterm, final):
    print("Grades:", weights, "Assignments:", assignments, "Quizzes:", quizzes, "Midterm:", midterm, "Final:", final)
    return calculate_needed_final(weights, assignments, quizzes, midterm, final)


@course2
def course_B(weights, assignments, quizzes, midterm, final):
    print("Grades:", weights, "Assignments:", assignments, "Midterm:", midterm, "Final:", final)
    return calculate_needed_final(weights, assignments, quizzes, midterm, final)


# =========================
# MAIN PROGRAM
# =========================
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weights.py <course_code>")
        print("Course codes: cpsc340, cpsc425")
        sys.exit(1)

    course_code = sys.argv[1].lower()

    if course_code == 'cpsc425':
        print(course_A())
    elif course_code == 'cpsc340':
        print(course_B())
    else:
        print("Invalid course code.")