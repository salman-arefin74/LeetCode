var interpret = function(command) {
	let result = command;
  while(result.includes("()") || result.includes("(al)")){
  	result = result.replace("()", "o").replace("(al)", "al");
  }  
  return result;
};
