// Problem statement: https://www.hackerrank.com/challenges/a-very-big-sum/problem

function aVeryBigSum(ar) {
  let sum = 0;
  sum = ar.reduce( (accumulator, currentValue) => accumulator + currentValue, 0);

  console.log(sum);
  return sum
}

aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])