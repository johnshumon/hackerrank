// Problem statement: https://www.hackerrank.com/challenges/plus-minus/problem

function plusMinus(arr) {
  const MINUS_100 = -100;
  const PLUS_100 = 100;
  const arrSize = arr.length;

  let plusCounter = 0
  let minusCounter = 0
  let zeroCounter = 0
  let result = []; 

  // edge condition
  if(arrSize > 100 || arrSize < 0) return;

  // edge condition
  arr.forEach(item => {
    if (item < MINUS_100 || item > PLUS_100) return;
  });

  // loop through and find out corresponding counters
  for (let i=0; i<arrSize; i++){
    if(arr[i] > 0){
      plusCounter += 1;
    } else if(arr[i] < 0){
      minusCounter += 1;
    } else {
      zeroCounter += 1;
    }
  }

  // make right precision
  plusCounter = parseFloat(plusCounter/arrSize).toPrecision(7);
  if(plusCounter < 1) plusCounter = parseFloat(plusCounter).toPrecision(6)


  minusCounter = parseFloat(minusCounter/arrSize).toPrecision(7);
  if(minusCounter < 1) minusCounter = parseFloat(minusCounter).toPrecision(6);

  zeroCounter = parseFloat(zeroCounter/arrSize).toPrecision(7);
  if(zeroCounter < 1) zeroCounter = parseFloat(zeroCounter).toPrecision(6);

  // print them out
  console.log(plusCounter);
  console.log(minusCounter);
  console.log(zeroCounter);
}

// sample test case
let testArr = [-4, 3, -9, 0, 4, 1];
plusMinus(testArr)