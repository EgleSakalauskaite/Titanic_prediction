function myFunction() {
  var prediction_value = document.getElementById('prediction_value').innerHTML;
  if (prediction_value == 'Survived') {
      document.getElementById('result_image').style.backgroundImage = "url('/static/images/survived.jpg')";
    }
  else {
      document.getElementById('result_image').style.backgroundImage = "url('/static/images/not_survived.jpg')";
    }
}
