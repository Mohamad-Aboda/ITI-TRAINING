//  remove duplicates 
var arr = [3, 1, 2, 4, 3, 5, 1];
var res = [];

for(i in arr){
    if(res.indexOf(arr[i]) === -1){
        res.push(arr[i]);
    }
}

console.log(res);

// sort assending 
arr.sort(function(a, b){
    return a - b;
});

console.log(arr);

// Filter numbers larger than 50

var ans = [];
for(i in arr){
    if(arr[i] > 50){
        ans.push(arr[i]);
    }
}
console.log(ans);



var ans2 = arr.filter(function(a){
    if(a > 50){
        return a;
    }
})
console.log(ans2);


// Display Max and Min Numbers

var mx = -1000000000;
var mn =  1000000000;
for(i in arr){
    if(arr[i] > mx){
        mx = arr[i];
    }
    
    if(arr[i] < mn){
        mn =  arr[i];
    }
}
console.log("min number is " + mn);
console.log("max number is  " + mx );// Display Max and Min Numbers

var mx = -1000000000;
var mn =  1000000000;
for(i in arr){
    if(arr[i] > mx){
        mx = arr[i];
    }
    
    if(arr[i] < mn){
        mn =  arr[i];
    }
}
console.log("min number is " + mn);
console.log("max number is  " + mx );



var mx = -1000000000;
var mn =  1000000000;
for(i in arr){
    if(arr[i] > mx){
        mx = arr[i];
    }
    
    if(arr[i] < mn){
        mn =  arr[i];
    }
}
console.log("min number is " + mn);
console.log("max number is  " + mx );


var mnNumber = Math.min(...arr);
var mxNumber = Math.max(...arr);

console.log("min number is " + mnNumber);
console.log("max number is  " + mxNumber);




// 2- Write a JavaScript function to Compute the sum and product of an array of  integers (Use eval)

function sumAll(arr){
    str = "";    
    prod = 1;
    for(i in arr){
        str += arr[i] + "+";
        prod = prod * arr[i];
    }
    str += "0";
    console.log("prod = " + prod);
    return str;
}

var res = eval(sumAll([1, 3, 3, 5]));
console.log("sum = " + res);




function sumAll() {
   sum = 0;
   var prod = 1;
   for (var i = 0; i < arguments.length; i++) {

       sum += arguments[i];
       prod = prod * arguments[i];
   }
   console.log(sum);
   console.log(prod);
}
sumAll(1, 3, 3);



