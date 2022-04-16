var nums1 = [1,2,3]; 
var nums2 = [2,4,6];

var num1UniqueElements = [... new Set(nums1)];
var num2UniqueElements = [... new Set(nums2)];

var num1results = [];
var num2results = [];

for(var i=0; i<num1UniqueElements.length; i++){
  if(!num2UniqueElements.includes(num1UniqueElements[i])){
    num1results.push(num1UniqueElements[i]);
  }
}

for(var i=0; i<num2UniqueElements.length; i++){
  if(!num1UniqueElements.includes(num2UniqueElements[i])){
    num2results.push(num2UniqueElements[i]);
  }
}

let answer = [];
answer.push(num1results);
answer.push(num2results);

console.log(answer);