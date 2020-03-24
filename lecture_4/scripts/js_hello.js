document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('button').forEach(function(button){
    button.onclick = count;
  });
});

function hello(){
  document.querySelector("h1").innerHTML = "goodbye"
};

var counter = 0;
function count() {

  counter++;
  document.querySelector('#counter').innerHTML = counter;
  if (counter%10 == 0) {
    alert(`Counter is at ${counter}`);
  };
};

document.addEventListener("DOMContentLoaded", function(){
  document.querySelector('#form').onsubmit = function(){
    const name = document.querySelector('#name').value;
    alert(`Hello ${name}`);
  }
});

document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.color-change').forEach(function(button){
    button.onclick = function(){
      document.querySelector("#counter").style.color = button.dataset.color;
    };
  });
});

document.addEventListener("DOMContentLoaded",()=>{
  document.querySelector("#change-name").onchange = ()=>{
    var val = document.getElementById("change-name").value;
    document.querySelector("#hello").innerHTML = val;
    // alert(document.getElementById("change-name").value);
  };
});


