window.addEventListener("load", function(){

    p1 = document.getElementsByTagName("p")[0];
    stopbutton = this.document.getElementById("stop");
    resetbutton = this.document.getElementById("reset");
    startbutton = this.document.getElementById("start");
    min = 0;
    sec = 0;
    
  
    
    startbutton.addEventListener("click", function(){
            startbutton.disabled = true;
            xx = setInterval(function(){
            sec++;
            p1.innerText = "0" + min + ":" + "0"+  sec;
            if(sec > 9){
                p1.innerText = "0" + min + ":" +  sec;
    
            }
    
            if(sec == 59){
                min++;
                sec = 0;
                p1.innerText = "0" + min + ":" +  sec;
    
    
            }
    
            if(min >= 10){
                p1.innerText =  min + ":" +  sec;
            }
    
            
        }, 1000);
    
    
    });


    stopbutton.addEventListener("click", function(){
        startbutton.disabled = false;
        clearInterval(xx);
    });

    resetbutton.addEventListener("click", function(){
        clearInterval(xx);
        min = 0;
        sec = 0;
        p1.innerText = "00:00";
        startbutton.disabled = false;

        
    });


    














});