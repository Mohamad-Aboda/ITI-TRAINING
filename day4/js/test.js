// 1- Write a JavaScript code that converts the first letter of each word of the string in
// upper case.
//Example : 'the quick brown fox'
//Output : 'The Quick Brown Fox'
function ass1(a){
    var str = a;
    var temp = null;
    temp = str[0].toUpperCase();
    for(var i = 1; i < str.length; ++i){
        if(str[i - 1] == " "){
            temp += str[i].toUpperCase();
        }else{
            temp += str[i];
        }
    }
    console.log(temp);
}



// 2- Write a JavaScript program which swap the case of each character for string.
//Example : 'Egypt'
//Output : 'eGYPT'
function ass2(a){
    var str = a;
    var temp = "";
    for(var i = 0; i < str.length; ++i){
        
        if(str[i] == str[i].toUpperCase()){
            temp += str[i].toLowerCase();
        }else{
            temp += str[i].toUpperCase();
        }
    }
   console.log(temp);

}




// 3- Write a JavaScript code to extract unique characters from a string.
//Example : "thequickbrownfoxjumpsoverthelazydog"
//Output : "thequickbrownfxjmpsvlazydg"

function ass3(a){
    var str = a;
    var temp = "";
    for(var i = 0; i < str.length; ++i){
        if(temp.indexOf(str.charAt(i)) == -1){
            temp += str[i];
        }
    }
    console.log(temp);
}





// 4- Write a JavaScript code that finds the longest word within the string. (Bonus)
// Example : 'Web Development Tutorial'
// Output : 'Development'

function ass4 (str) {
    var arr = str.split(" ");
    
    var mx = 0;
    var res = [];
    
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].length === mx) {
            res.push(arr[i]);
        }else if (arr[i].length > mx) {
            mx = arr[i].length;
            res = [];
            res.push(arr[i]);
        }
    }
        
    console.log(res);
}
    
    




  