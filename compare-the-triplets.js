// Problem statement: https://www.hackerrank.com/challenges/compare-the-triplets/problem

function compareTriplets(a, b) {

  if(!a.length == b.length) return;
  let comparisonPoints = [];
  let alicePoint = 0;
  let bobPoint = 0;

  for (let i=0; i<a.length; i++){
      if(a[i]<1 || a[i]>100 || b[i]<1 || b[i]>100) return;
      
      if(a[i] > b[i]) {
          alicePoint += 1;
      };

      if(a[i] < b[i]) {
          bobPoint += 1;
      };
  };

  comparisonPoints.push(alicePoint, bobPoint);

  console.log(comparisonPoints);
  return comparisonPoints;

}
compareTriplets([17, 28, 30], [99, 16, 8]);
