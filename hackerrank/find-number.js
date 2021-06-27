// Problem statement: 

function findNumber(arr, k) {
  if (arr.length < 1 || arr.length > Math.pow(10, 5)) return;
  
  arr.forEach(item =>{
      if (item < 1 || item > Math.pow(10, 9)) return;
  });

  for (let i=0; i<arr.length; ++i){
    if (arr[i] === k){
      return "YES";
    } else {
      return "NO";
    }
  }
}

console.log(findNumber([1,2,3,4,5], 6));

