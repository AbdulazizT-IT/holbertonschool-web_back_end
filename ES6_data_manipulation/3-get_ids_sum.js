export default function getStudentIdsSum(Ids) {
    if (!Array.isArray(Ids)) return [];

    return Ids.reduce((acc, student) => acc + student.id, 0);
}
