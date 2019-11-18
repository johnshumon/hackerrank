// Problem statement: 

function oddNumbers(l, r) {
  if((l||r) < 1 || (l||r) > Math.pow(10, 5)) return;
  let oddNumbers = [];

  for(let i=l; i<=r; i++){
    if (i % 2 != 0) {
      oddNumbers.push(i);
    }
  }
  return oddNumbers;
}

console.log(oddNumbers(2,5));