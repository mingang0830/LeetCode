var containsDuplicate = function(nums) {
    let setNums = new Set(nums);
    return setNums.size < nums.length;
};

var sample = [1,1,1,3,3,4,3,2,4,2];
console.log(containsDuplicate(sample));