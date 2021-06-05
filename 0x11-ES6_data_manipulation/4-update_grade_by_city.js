export default function updateStudentGradeByCity(students, city, newGrades) {
  if (Object.getPrototypeOf(students, newGrades) !== Array.prototype) {
    return [];
  }
  return students
    .filter((student) => student.location === city)
    .map((std) => {
      const [newGrade] = newGrades.filter((item) => item.studentId === std.id);
      return { ...std, grade: newGrade ? newGrade.grade : 'N/A' };
    });
}
