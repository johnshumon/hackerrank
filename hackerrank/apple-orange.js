// Problem statement: https://www.hackerrank.com/challenges/apple-and-orange/problem

function countApplesAndOranges(s, t, a, b, apples, oranges) {

  if ((s || t || a || b ) < 1 || (s || t || a || b ) > Math.pow(10, 5)) return;
  if (!(a < s < t < b)) return;
  
  let inclusiveRange = [];
  let appleCounter = 0;
  let orangeCounter = 0;

  for(let i=0; i<apples.length; i++){
    apples[i] = apples[i] + a;
  }

  for(let i=0; i<oranges.length; i++){
    oranges[i] = oranges[i] + b;
  }

  apples.forEach(item => {
    if (item >= s && item <= t) appleCounter += 1;
  });
  inclusiveRange.push(appleCounter);

  oranges.forEach(item => {
    if (item >= s && item <= t)  orangeCounter += 1;
  });
  inclusiveRange.push(orangeCounter);

  console.log(inclusiveRange.join("\n"));
  return inclusiveRange;
}

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]);
