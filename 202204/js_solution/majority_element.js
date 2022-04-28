var majorityElement = function(nums) {
    const dictObject = {};

    for(let num of nums){
        if (!dictObject.hasOwnProperty(num)){
            dictObject[num] = 1;
        }else{
            dictObject[num]++;
        }

        if (dictObject[num] > nums.length / 2){
            return num;
        }

    }
    

};
var sample = [2,2,1,1,1,2,2,1,1];
var result = majorityElement(sample);
console.log(result);