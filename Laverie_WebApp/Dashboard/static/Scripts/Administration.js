window.addEventListener('load', function () {
    StatutServeur()
    setInterval(() => StatutServeur(), 30000);
  })

  function StatutServeur() {
    fetch("http://127.0.0.1:8000/ServerStatus/")
      .then((response) => response.json())
      .then((json) => update_front_info(json));    
  }

  function update_front_info(json) {
    console.log(json);
    if (json["Error"] == "OK") {
      document.getElementById("alertServeurIndisponible").style.display = 'none';
    } else {
        document.getElementById("alertServeurIndisponible").style.display = 'block';
    }
  }
  