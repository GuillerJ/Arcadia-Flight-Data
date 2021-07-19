

function load_arrivals(icao, date) {
  
$.ajax({
    url: "/load/airports",
    type: "get",
    data: {airport: icao,
           date: date},
    success: function(response) {
      $("#dato_actual").html(response);
      $("#fecha-upd").html("Refrescar Datos");
      $("#cargando").css("display", "none");
    },
    error: function(xhr) {
      alert("Error en la carga");
    }
  });

} 