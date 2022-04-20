let total = 1000000;
let cost1 = 1;
let cost2 = 1;

let cost1Moves = [];
let forCost1 = total;
let i = 0;
while(forCost1 <= total){
  if(i*cost1 <= total){
    cost1Moves.push(i);
  }
  forCost1 = cost1*i;
  i++;
}

let count = 0;
let k = 0;
let cost2Left = 0;
let forCost2 = 0;
for(var j=0; j<cost1Moves.length; j++){
  cost2Left = total - (cost1*j);
  forCost2 = cost2Left;
  k=0;
  while(forCost2 <= cost2Left){
    if(k*cost2 <= cost2Left){
      count++;
    }
    forCost2 = cost2*k;
    k++;
  }
}
console.log(count);



