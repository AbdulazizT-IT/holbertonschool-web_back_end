const fs = require('fs');

function countStudents(path) {
  const studentsByField = {};

  try {
    const data = fs.readFileSync(path, 'utf8');
    const rows = data.split('\n').filter((row) => row.trim() !== '');

    if (rows.length === 0) {
      throw new Error('Cannot load the database');
    }

    let totalStudents = 0;

    rows.forEach((line, index) => {
      if (index === 0) return;
      const [firstName, lastName, age, field] = line.split(',');

      if (!firstName || !field) return;

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }

      studentsByField[field].push(firstName);
      totalStudents += 1;
    });

    console.log(`Number of students: ${totalStudents}`);

    Object.keys(studentsByField).forEach((field) => {
      console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`);
    });
  } catch (err) {
    console.error(err.message);
  }
}

module.exports = countStudents;
