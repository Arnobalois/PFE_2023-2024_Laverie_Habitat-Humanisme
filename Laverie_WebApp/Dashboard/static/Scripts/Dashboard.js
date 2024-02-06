

window.addEventListener('load', function () {
  update();
  setInterval(() => update(), 5000);
})
let TIMER_INVTERVAL_ID ;
let IDMACHINE ; 
let TIME; 
function update() {
  fetch("http://127.0.0.1:8000/Update/")
    .then((response) => response.json())
    .then((json) => update_front_info(json));
}

function update_front_info(json) {
 // console.log(json);
  json.forEach(element => {
    if (element[1]) {
      document.getElementById(element[0]).innerHTML = "En cours d'utilisation ! ";
      const button = document.getElementById("button" + element[0])
      button.disabled = true;
    } else {
      document.getElementById(element[0]).innerHTML = "Machine libre !";
      const button = document.getElementById("button" + element[0])
      button.disabled = false;
    }
  });
}

function select_Machine(idMachine) {
  const button = document.getElementById("button" + idMachine)
  button.disabled = true;
  var csrftoken = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
  $.ajax({
    url: 'http://127.0.0.1:8000/begin/',  // Replace with the actual URL of your Django view
    type: 'POST',
    headers: {
      'X-CSRFToken': csrftoken
    },
    data: {
      MachineID: idMachine,
    },
    success: function (response) {
      console.log(response);
      console.log(response["Started"]);
      if (response["Started"]) {
        console.log("Creation timer")
     //   TIME = 50;
     //   IDMACHINE = idMachine;

       // TIMER_INVTERVAL_ID = setInterval(()=>timer(),1000);
      }
    },
    error: function (error) {
      console.error(error);
    }
  });
  update();
}
function timer(){
        // Update the count down every 1 second
  TIME = TIME - 1;
  // Time calculations for days, hours, minutes and seconds
  var minutes = Math.floor(TIME / 60);
  var seconds = TIME - (minutes * 60);
  // Output the result in an element with id="demo"
  document.getElementById("Timer"+IDMACHINE).innerHTML = minutes + "m " + seconds + "s ";

  // If the count down is over, write some text 
  if (TIME < 0) {
    clearInterval(TIMER_INVTERVAL_ID);
    document.getElementById("Timer"+IDMACHINE).innerHTML = "";
  }
}  

