export default function updateStudentGradeByCity(list, city, newGrades) {

    return list
        .filter((student) => student.location === city)
        .map((student) => {
            const gradeEntry = newGrades.find((entry) => entry.studentId === student.id);
            return {
                ...student,
                grade: gradeEntry ? gradeEntry.grade: 'N/A',
            };

        });
}