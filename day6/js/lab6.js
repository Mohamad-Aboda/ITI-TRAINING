
function Employee(_name, age, department){
    this._name = _name;
    this.age = age;
    this.department = department;
    var salary;
    
    function setSalaty(salary){
        this.salary = salary;
    }

    salary = function getSalary(){
        return salary;
    }
      
    

    this.show = function(){
        console.log(this._name);
        console.log(this.age);
        console.log(this.department);
        console.log(this.salary);
    }


}

var emp = new Employee("mohamed", 22, "computer engineering", 1000);


////////////////////////////////////////////////////////////////////////////////////////////////////


var len = prompt("Enter Array size");
emp = {
    _name:null, 
    age:null, 
    id: null, 
    salary:null, 
};
for(var i = 0; i < len; ++i){
    emp._name = prompt("Enter Employee Name");
    emp.age = prompt("Enter Employee age");
    emp.id = prompt("Enter Employee Id");
    emp.salary = prompt("Enter Employee Salary");
}

// ////////////////////////////////////////////////////////////////////////////////////////////////////


var arrDept = [];
var arrSal = [];
for(i in Employee){
    arrDept.push(Employee["department"]);
    arrSal.push(Employee["salary"]);
}




arrDept.sort(function(a, b){
    return b - a;
});

arrSal.sort(function(a, b){
    return a - b;
});


// ////////////////////////////////////////////////////////////////////////////////////////////////////


var res = arrSal.filter(
    function(a){
        return a > 2000;
    }
);


// ////////////////////////////////////////////////////////////////////////////////////////////////////
arr = [];
var len = prompt("Enter Array size");
for(var i = 0; i < len; ++i){
    arr[i] = prompt("Enter Employee Salary");
}

var total = 0;

for(i in arr){
    total += arr[i];
}
console.log("The Total Salary is " + total);
console.lof("The Avg Salary is " + total/len);

// ////////////////////////////////////////////////////////////////////////////////////////////////////


var arrSal = [];
for(i in Employee){
    arrSal.push(Employee["salary"]);
}

var high_employee_salary = Math.max(...arrSal);


// ////////////////////////////////////////////////////////////////////////////////////////////////////


var cnt = 0;
setInterval(function () {
    cnt++;
    document.title = cnt;


}, 1000)