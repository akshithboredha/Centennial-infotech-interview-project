const form = document.getElementById("form");

form.addEventListener("submit", async function(e){

e.preventDefault();

let formData = new FormData(form);

let response = await fetch("/register",{
method:"POST",
body:formData
});

let data = await response.json();

document.getElementById("msg").innerText = data.message;

form.reset();

});