window.addEventListener('load', function () {
    //setInterval(()=>update(),5000);
  })

function update() {
    fetch("http://127.0.0.1:8000/Update")
    .then((response) => response.json())
    .then((json) => update_front_info(json));
}

function update_front_info(json){
    console.log("inside");
    console.log(json);
   json.forEach(element => {
    if (element[1] == "true"){
        document.getElementById(element[0]).innerHTML = "True";
    }
   });
}

function select_Machine(idMachine){
    console.log(idMachine);
    const button = document.getElementById("button"+idMachine)
    button.disabled = true;

    fetch("http://127.0.0.1:8000/GET/")
    .then((response) => response.json())
    .then((json) => update_front_info(json));
   //var refreshIntervalId = setInterval(fname, 10000);
    //clearInterval(refreshIntervalId);
}

