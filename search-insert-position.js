/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let index = 0;
    let previousNumber = 0;
    if(target < nums[0]){
        return 0;
    }
    for(var i = 0; i < nums.length; i++){
        if(i!=0){
            previousNumber = nums[i-1];
        }
        if(target == nums[i]){
            index = i;
            break;
        }
        if(previousNumber != 0){
            if(target < nums[i] && target > previousNumber){
                index = i;
                break;
            }
        }
        if(i == nums.length - 1){
            index = i + 1;
        }
    }

    return index
};

// Better Solution:
// Binary Search

// var searchInsert = function(nums, target) {
//     let left = 0;
//     let right = nums.length - 1;

//     while (left <= right) {
//         let mid = Math.floor((left + right) / 2);

//         if (nums[mid] === target) {
//             return mid;
//         } else if (nums[mid] > target) {
//             right = mid - 1;
//         } else {
//             left = mid + 1;
//         }
//     }

//     return left;    
// };
