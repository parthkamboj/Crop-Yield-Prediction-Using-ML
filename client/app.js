

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var rainfall = document.getElementById("rainfall");
  var temp = document.getElementById("temp");
  var pest = document.getElementById("pest");
  var items = document.getElementById("uiLocations1");
  var countries = document.getElementById("uiLocations");

  var url = "http://127.0.0.1:5000/predict_crop_yield"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      avg_rainfall: parseFloat(rainfall.value),
      item: items.value,
      avg_temp: parseFloat(temp.value),
      country : countries.value,
      pesticides_tonnes : parseFloat(pest.value)
  },function(data, status) {
      var est_yield = document.getElementById("uiEstimatedPrice")
      console.log(data.estimated_crop_yield);
      est_yield.innerHTML = "<h2>" + data.estimated_crop_yield.toString() + " hg/ha</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
   var url = "http://127.0.0.1:5000/get_country_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.countries;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
   url = "http://127.0.0.1:5000/get_item_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.items;
          var uiLocations = document.getElementById("uiLocations1");
          $('#uiLocations1').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations1').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;