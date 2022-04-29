let char_list =  ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
"U", "V", "W", "X", "Y", "Z"]

var titleToNumber = function(columnTitle) {
    var result = 0
    var index_ = 0
    for(let c of columnTitle.split("").reverse().join("")) {
        result += (26 ** index_) * (char_list.indexOf(c) + 1)
        index_ ++;
    }
    return result
};


var sample = 'AB'
titleToNumber(sample);