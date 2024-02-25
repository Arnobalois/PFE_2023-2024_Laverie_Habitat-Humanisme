window.addEventListener('load', function () {
  update();
  setInterval(() => update(), 10000);
})

function update() {
  fetch("http://127.0.0.1:8000/Update/")
    .then((response) => response.json())
    .then((json) => update_front_info(json));    
}

function update_front_info(json) {
 console.log(json);
  json.forEach(element => {
    console.log(element[1])
    var disponibilite = document.getElementById(element[0]);
    if (!element[1]) {
      console.log("ici")
      disponibilite.innerHTML = "En cours d'utilisation ! ";
      disponibilite.style.color = "red";
      const button = document.getElementById("button" + element[0])
      button.disabled = true;
      var timer = document.getElementById("timer" + element[0])
      timer.innerHTML = "Temps restant : " + element[2] + " minutes restantes";
    } else {
      disponibilite.innerHTML = "Machine libre !";
      disponibilite.style.color = "green";
      const button = document.getElementById("button" + element[0])
      button.disabled = false;
      var timer = document.getElementById("timer" + element[0])
      timer.innerHTML = "Machine " + element[0] + " : Libre";
    }
  });
}

function select_Machine(idMachine) {
  const button = document.getElementById("button" + idMachine)
  button.disabled = true;
  var csrftoken = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
  $.ajax({
    url: 'http://127.0.0.1:8000/Begin/',  // Replace with the actual URL of your Django view
    type: 'POST',
    headers: {
      'X-CSRFToken': csrftoken
    },
    data: {
      MachineID: idMachine,
    },
    success: function (response) {
      if (response["Started"]) {
        console.log("Creation timer")
      }
    },
    error: function (error) {
      console.error(error);
    }
  });
  update();
}
 

