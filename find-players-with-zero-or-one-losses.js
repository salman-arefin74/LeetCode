var findWinners = function(matches) {
  let winners = [];
  let losers = [];
  
  for(var i = 0; i < matches.length; i++){
    winners.push(matches[i][0]);
    losers.push(matches[i][1]);
  }
  
  let onlyWinners = [];
  let oneMatchLoser = [];
  
  const occurrences = losers.reduce(function (acc, curr){
    return acc[curr] ? ++acc[curr] : acc[curr] = 1, acc
  }, {});
  
  for (var key of Object.keys(occurrences)) {
    if(occurrences[key] == 1){
      oneMatchLoser.push(parseInt(key));
    }
  }
  
  for(var i = 0; i < winners.length; i++){
    if(!losers.includes(winners[i])){
      onlyWinners.push(winners[i]);
    }
  }
  
  onlyWinners = [... new Set(onlyWinners)];
  
  let result = [];
  result.push(onlyWinners.sort(function(a, b){return a-b}));
  result.push(oneMatchLoser.sort(function(a, b){return a-b}));
  
  return result;
};