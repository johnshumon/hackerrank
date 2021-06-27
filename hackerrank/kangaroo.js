// Problem statement: https://www.hackerrank.com/challenges/kangaroo/problem

function kangaroo(x1, v1, x2, v2) {

  if ((x1 || x2) < 0 || (x1 || x2) > 10000) return;
  if ((v1 || v2) < 1 || (v1 || v2) > 10000) return;

  let kangaroo1 = x1;
  let kangaroo2 = x2;

  if(x2 > x1 && v2 > v1){
    return "NO";

  } else if(x2 > x1 && v2 === v1) {
    return "NO";

  } else {

    for(let i=0; i<=kangaroo1; i++){
      kangaroo1 += v1;
      kangaroo2 += v2;

      if(kangaroo1 === kangaroo2) {
        return "YES";
    
      } else if(kangaroo1 < kangaroo2) {
        continue;

      } else {
        return "NO"
      }
    }
  }
}

// console.log(kangaroo(0, 2, 5, 3));
console.log(kangaroo(43, 2, 70, 2))
// console.log(kangaroo(0, 3, 4, 2));
