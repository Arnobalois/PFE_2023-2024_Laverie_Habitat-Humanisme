
function convert_table() {
    var tableLocataire = document.getElementById("LocataireTable")
    var Data= [] ;
    for (var i =1, row; row = tableLocataire.rows[i]; i++) {
        var checkboxElement = row.querySelector(".checkbox-option");
        if (checkboxElement.checked){  
            var selectElementYear = row.querySelector(".select-option-Years");
            var selectElementMonth = row.querySelector(".select-option-Months");
                Data.push({Id:row.cells[0].innerHTML,last_name:row.cells[1].innerHTML , first_name:row.cells[2].innerHTML, Years:selectElementYear.value,Months:selectElementMonth.value});
        }
    }

    sendValue(Data);
  }
  function convert_all() {
    var selectElementYearsAll = document.getElementById("select-option-Years-All")
    var Data= [] ;
    Data.push({Id:"all",last_name:"all" , first_name:"all", Years:selectElementYearsAll.value,Months:"all"});
    sendValue(Data);
  }

  function sendValue(Data){
    console.log(Data)
    var csrftoken = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
    $.ajax({
      url: 'http://127.0.0.1:8000/Convert',  // Replace with the actual URL of your Django view
      type: 'POST',
      headers: {
        'X-CSRFToken': csrftoken
      },
      data:JSON.stringify( Data),
      success: function(response, status, xhr) {
        console.log(typeof response);
       if (typeof response == "string"){
        // Create a blob object from the response
        var blob = new Blob([response], { type: xhr.getResponseHeader('content-type') });

            // Create a download link
        var downloadLink = document.createElement('a');
        downloadLink.href = window.URL.createObjectURL(blob);
        downloadLink.download = 'file.csv'; // Set the file name
        downloadLink.click(); // Simulate click to download
       }
       else {
        alert(response.message)
       }   
        
    },
      error: function (error) {
        console.error(error);
      }
    });
  }