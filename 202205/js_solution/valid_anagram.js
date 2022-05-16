var isAnagram = function(s, t) {
  /*
  python 풀이

  const checkAnagram = s.split("");
  for(let i = 0; i < t.length; i++) {
      const index = checkAnagram.indexOf(t[i]);
      if(checkAnagram.includes(t[i]))  {
        checkAnagram.splice(index, 1);
      }else return false;
    }
  return checkAnagram.length == 0;
  */

  
  //hashmap(object) 사용으로 풀이
  if (s.length !== t.length) return false;

  let countS = {};
  let countT = {};

  for (let i = 0; i < s.length; i++){
    if(s[i] in countS){
      countS[s[i]] = countS[s[i]] + 1;
    }else{
      countS[s[i]] = 0;
    }
  
    if(t[i] in countT){
      countT[t[i]] = countT[t[i]] + 1;
    }else{
      countT[t[i]] = 0;
    }
  }

  for (let i in countS) {
    if (countS[i] !== countT[i]) return false;
  }

  return true;

};

console.log(isAnagram("a", "ab"));