// Problem statement: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

function birthdayCakeCandles(ar) {
  if (ar.length < 1 || ar.length > Math.pow(10, 5)) return;

  let counter = 0;
  let max = Math.max(...ar);

  ar.forEach(item =>{
      if (item > Math.pow(10, 7)) return;
      if (item == max) counter += 1;
  });
  
  console.log(counter);
  return counter;

}

birthdayCakeCandles([3,2,1,3]);

