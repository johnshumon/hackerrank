// Problem statement: https://www.hackerrank.com/challenges/diagonal-difference/problem

function diagonalDifference(arr){
  for (let i=0; i<arr.length; i++){
    for (let j=0; i<i.length; j++){
      if(parseInt(arr[i][j]) < parseInt(-100) || parseInt(arr[i][j]) > parseInt(100)) return;
    }
  };

  let leftDiagonal = 0;
  let rightDiagonal = 0;
  for (let i=0, j=arr.length-1; i<arr.length; i++, j--){
    leftDiagonal += arr[i][i];
    rightDiagonal += arr[i][j];
  }

  let diff = leftDiagonal - rightDiagonal;
  
  console.log(Math.abs(diff));
  return Math.abs(diff);
}

let diff = diagonalDifference(
  [
    [-1, 1, -7, -8],
    [-10, -8, -5, -2],
    [0, 9, 7, -1],
    [4, 4, -2, 1]
  ]
);
