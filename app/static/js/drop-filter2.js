var date = -1;
var icao = -1;


function dropSelect() {
  document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function changeDate() {
  date = document.getElementById("dateInic").value;

  load_arrivals(icao, date);
}

var elements = document.getElementsByClassName("input-airport");

var getAirport = function() {
    icao = this.id;
    var nombre = this.innerText;
    document.getElementById("myButton").textContent = nombre;
    document.getElementById("myDropdown").classList.toggle("show");
    
    load_arrivals(icao, date);
};



for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', getAirport, false);
}


$( function() {
  $( "#dateInic" ).datepicker({
      dateFormat: 'dd MM yy',
  });
} );


