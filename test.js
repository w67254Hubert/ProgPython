function add(a,b){

    return a()+b();

}
function one(){return 1}

function two(){return 2}

console.log(add(one,two))