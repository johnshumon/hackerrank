// Problem statement: https://www.hackerrank.com/challenges/grading/problem

function gradingStudents(grades) {
  // Write your code here
  if(grades.length < 1 || grades.length > 60) return;
  grades.forEach(item =>{
    if (item < 0 || item > 100) return;
  });

  let finalGrades = [];
  let counter = 0;

  grades.forEach(item =>{
    if(item < 38){
      finalGrades.push(item);
      
    } else {
      while(item % 5 != 0) {
        item += 1;
        counter += 1;
      }

      if (counter < 3) {
        finalGrades.push(item);
      } else {
        finalGrades.push(item - counter);
      }
    }
    counter = 0;
  });

  console.log(finalGrades);
  return finalGrades;

}

gradingStudents([73, 67, 38, 33])