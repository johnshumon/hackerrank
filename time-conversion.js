// Problem statement: https://www.hackerrank.com/challenges/time-conversion/problem

function timeConversion(s) {
  let splitedTime = s.split(":");
  let seconds = splitedTime.pop();
  let regexed = seconds.match(/([0-9]+)([A-za-z]+)/);
  let convertedTime = {};
  
  splitedTime.push(regexed[1]);
  splitedTime.push(regexed[2]);
  
  console.log(splitedTime)

  if (!parseInt(splitedTime[0]) < 0 || 
    !parseInt(splitedTime[0]) > 12 ||
    !(parseInt(splitedTime[1]) || parseInt(splitedTime[2])) < 0 ||
    !(parseInt(splitedTime[1]) || parseInt(splitedTime[2])) > 59 
  ) {
    console.log("invalid hour");
    return;
  }

  if (splitedTime[3] == "AM") {
    if ( parseInt(splitedTime[0]) <= 11 && parseInt(splitedTime[0]) >= 0 ) {
      convertedTime.hh = splitedTime[0];
      convertedTime.mm = splitedTime[1];
      convertedTime.ss = splitedTime[2];
    } else {
      convertedTime.hh = "00";
      convertedTime.mm = splitedTime[1];
      convertedTime.ss = splitedTime[2];
    }


  } else if (splitedTime[3] == "PM") {
    if ( parseInt(splitedTime[0]) <= 11 && parseInt(splitedTime[0]) >= 0 ) {
      convertedTime.hh = (parseInt(splitedTime[0]) + 12);
      convertedTime.mm = splitedTime[1];
      convertedTime.ss = splitedTime[2];
    } else {
      convertedTime.hh = "12";
      convertedTime.mm = splitedTime[1];
      convertedTime.ss = splitedTime[2];
    }
  }

  let militaryTime = `${convertedTime.hh}:${convertedTime.mm}:${convertedTime.ss}`;
  return militaryTime;
}

console.log(timeConversion("12:05:05PM"));
