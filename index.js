var nums = [0,1,5,4,2,4,7,2,3,0,3,0,0,9,7,5,9,4,3,9,9,2,1,6,3,1,0,7,6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5]
;

let count = 0;
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
console.log(nums);
