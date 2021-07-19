
var columns = [
  {"name":"estDepartureAirport","title":"Departure Airport"},
  {"name":"callsign","title":"Call sign"},
  {"name":"estDepartureAirportHorizDistance","title":"Departure airport distance"},
  {"name":"arrivalAirportCandidatesCount","title":"Possible arrival airports","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"departureAirportCandidatesCount","title":"Possible departure airports","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"estArrivalAirport","title":"Arrival airport (ICAO)","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"estArrivalAirportVertDistance","title":"Arrival airport altitude distance","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"estDepartureAirport","title":"Departure airport (ICAO)","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"estDepartureAirportHorizDistance","title":"Arrival airport distance","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"estDepartureAirportVertDistance","title":"Arrival airport altitude distance","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"firstSeen","title":"Time departure","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"icao24","title":"Aircraft ICAO 24","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
  {"name":"lastSeen","title":"Est time arrival","breakpoints":"xs sm","style":{"maxWidth":200,"overflow":"hidden","textOverflow":"ellipsis","wordBreak":"keep-all","whiteSpace":"nowrap"}},
];


function load_arrivals(icao, date) {
  $("#cargando").css("display", "");
  $.ajax({
    url: "/load/airports",
    type: "get",
    data: {airport: icao,
           date: date},
    success: function(response) {
      $("#dato_actual").html(response);
      if (response != "None") {
        var rows = [];  
        var si;
        //console.log(si)
        Object.entries(response).forEach(element => {
          rows.push(element[1]);
          si = element[1];
        });
        //var columns = [];
        //for(var k in si) columns.push(k);
        
        $('.table').footable({
          "columns": columns,
          "rows":rows
        });
      }
      $("#cargando").css("display", "none");      
    },
    error: function(xhr) {
      alert("Error en la carga");
      $("#cargando").css("display", "none");
    }
  });
} 