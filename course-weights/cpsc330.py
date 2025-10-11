from utils import dict_average

# calculate weights for each course necessary to pass
# cpsc330
# grades
syllabus_grade = 100
iclicker_grade = 100 # 100 as long as participation is over 80%
assignment_grades = {
    "a1": None,
}
midterm_1_grade = None
midterm_2_grade = None
final_exam_grade = None # must be over 40%
attendance_grade = 50 # assuming 0.1 for each attendance

# weights
syllabus_weight = 0.01
iclicker_weight = 0.05
assignments_weight = 0.22
midterm_1_weight = 0.21
midterm_2_weight = 0.21
final_exam_weight = 0.30
attendance_bonus = 0.02

# calculation