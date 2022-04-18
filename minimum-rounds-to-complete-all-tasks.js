var minimumRounds = function(tasks) {
    
    const occurrences = tasks.reduce(function (acc, curr) {
      return acc[curr] ? ++acc[curr] : acc[curr] = 1, acc
    }, {});

    let count = 0;
    let main = 0;
    let multiple = 0;
    let mod = 0;
    for (var key of Object.keys(occurrences)) {
      main = occurrences[key];
      multiple = Math.floor(occurrences[key] / 3);
      mod = occurrences[key] % 3;

      if(main == 1){
        count = -1;
        break;
      }
      else if(main == 2){
        count = count + 1;
      }
      else if(mod == 0){
        count = count + multiple + mod;
      }
      else if(mod == 2){
        count = count + multiple + mod - 1;
      }
      else if(main == 4){
        count = count + 2;
      }
      else if(mod == 1){
        count = count + (multiple - 1) + (main - 3*(multiple -1))/2;
      }
    }

return count;

};

