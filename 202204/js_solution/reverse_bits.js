var reverseBits = function(n) {
    /* python solution

    let lenN = 32;
    let result = 0;
    for(i = 0; i < lenN; i++){
        result += n%2 * (2**(lenN-i-1))
        n = parseInt(n/2);
    }
    return result;
    */

    
    let reversedArray = n.toString(2).split("").reverse();
    // toString을 하면 앞부분의 0은 지워지기 때문에 32bit에 맞게 0을 채워줘야 함
    while(reversedArray.length <32){
        reversedArray.push('0')
       }
    return  parseInt(reversedArray.join(""),2);
};

var sample = 0b00000010100101000001111010011100;
var result = reverseBits(sample);
console.log(result);