var convertTime = function(current, correct) {    
  let currentMinutes = parseInt(current.split(':')[0]) * 60 + parseInt(current.split(':')[1]);
  
  let correctMinutes = parseInt(correct.split(':')[0]) * 60 + parseInt(correct.split(':')[1]);
  
  let difference = correctMinutes - currentMinutes;
  
  let sixetyMultiple = Math.floor(difference/60);
  let sixetyMod = difference % 60;
  let fiveteenMultiple = Math.floor(sixetyMod/15);
  let fiveteenMod = sixetyMod % 15;
  let fiveMultiple = Math.floor(fiveteenMod/5);
  let fiveMod = fiveteenMod % 5;
  let oneMultiple = fiveMod;
  
  return sixetyMultiple + fiveMultiple + fiveteenMultiple + oneMultiple;    
};