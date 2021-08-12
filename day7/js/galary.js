window.addEventListener("load", function(){
    var cnt = 0;
    myleftbutton = this.document.getElementById("left");
    mypicture = this.document.getElementById("mypic");
    myrightbutton = this.document.getElementById("right");
    stopbutton = this.document.getElementById("stop");
    slidbutton = this.document.getElementById("slide");
    aud = new Audio("audio/music.wav");

    
    myrightbutton.addEventListener("click", function(){
        cnt++; 
        if(cnt == 9){
            cnt = 1;
        }
        mypicture.src = "images/" + cnt + ".jpeg";
        
    });


    myleftbutton.addEventListener("click", function(){
        if(cnt == 1){
            cnt = 9;
        }
        mypicture.src = "images/" + cnt + ".jpeg";
        cnt--;

    });


  


    slidbutton.addEventListener("click", function(){
        
        
        tme = setInterval(function(){
            aud.play();
            cnt++;
            mypicture.src = "images/" + cnt + ".jpeg";
            if(cnt == 9){
                cnt = 1;
            }

        }, 1000);
        slidbutton.disabled = true;
    });

    stopbutton.addEventListener("click", function(){
        aud.pause();
        clearInterval(tme);
        
        myleftbutton.disabled = false;
        myrightbutton.disabled = false;
        slidbutton.disabled = false;

    });


    slidbutton.addEventListener("click", function(){
        myleftbutton.disabled = true;
        myrightbutton.disabled = true;

    });








});