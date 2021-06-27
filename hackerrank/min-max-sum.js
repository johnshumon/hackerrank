// Problem statement: https://www.hackerrank.com/challenges/mini-max-sum/problem

function miniMaxSum(arr) {
  if (arr.length < 1 || arr.length > Math.pow(10, 9)) return;
  let minVal = Math.min(...arr);
  let maxVal = Math.max(...arr);

  let sum = arr.reduce((accumulate, currentValue) => accumulate + currentValue, 0); 
  let minSum = sum - maxVal;
  let maxSum = sum - minVal;

  console.log(minSum + " " + maxSum);
}

miniMaxSum([1, 2, 3, 4, 5]);