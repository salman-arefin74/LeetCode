var climbStairs = function(n) {
    if(n == 1) return 1;
    else if(n == 2) return 2;
    
    let twoStepBefore = 1;
    let oneStepBefore = 2;
    
    let steps = twoStepBefore + oneStepBefore;
    for(i=3; i<n; i++){
        twoStepBefore = oneStepBefore;
        oneStepBefore = steps;
        steps = twoStepBefore + oneStepBefore;
    }
    return steps;
};