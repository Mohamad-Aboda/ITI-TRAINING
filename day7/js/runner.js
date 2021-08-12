window.addEventListener("load", function(){
    btn = document.getElementsByTagName('button')[0];
    txt = document.getElementsByTagName('textarea')[0];
    
    btn.addEventListener('click', function () {
        right.innerHTML = txt.value;
    });
});