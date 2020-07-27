/**
 * Given nums = [2, 7, 11, 15], target = 9, */
var arr = [1, 2, 19, 28];
var target = 21;
var twoSum = function (nums, target) {
  for (var i = 0; i < nums.length; i++) {
    for (var j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
};
console.log(twoSum(arr, target));
