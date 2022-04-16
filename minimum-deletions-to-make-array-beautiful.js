var minDeletion = function(nums) {
  let count = 0;

  if(nums.length == 0)
    return 0;
  
  for(var i=0; i< nums.length; i++){
    let j = i-count;
    if(nums[i] == nums[i+1] && j%2 == 0 && i<nums.length-1){
      count++;
    }
  }
  
  if((nums.length-count) % 2 != 0){
    nums.splice((nums.length-1), 1);
    count++;
  }
  
  return count;
};


