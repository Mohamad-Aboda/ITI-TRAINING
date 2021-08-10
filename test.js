var mydiv = document.getElementById("div1");
var newelement = document.createElement("p");
var text = document.createTextNode("my paragraph text ");


newelement.appendChild(text);

mydiv.appendChild(newelement);
