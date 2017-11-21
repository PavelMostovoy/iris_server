var http = new XMLHttpRequest();
var url = "/test";
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var dataURL = canvas.toDataURL('image/png');
var params =  "imgBase64=" + dataURL;



window.onload = function() {

  // Normalize the various vendor prefixed versions of getUserMedia.
  navigator.getUserMedia = (navigator.getUserMedia ||
                            navigator.webkitGetUserMedia ||
                            navigator.mozGetUserMedia || 
                            navigator.msGetUserMedia);
// Get a reference to the video element on the page.


// Check that the browser supports getUserMedia.
// If it doesn't show an alert, otherwise continue.
if (navigator.getUserMedia) {
  // Request the camera.
  navigator.getUserMedia(
    // Constraints
    {
      video: true
    },

    // Success Callback
    function(localMediaStream) {
        // Get a reference to the video element on the page.
        var vid = document.getElementById('camera-stream');

        // Create an object URL for the video stream and use this
        // to set the video source.
        vid.src = window.URL.createObjectURL(localMediaStream);

    },

    // Error Callback
    function(err) {
      // Log the error to the console.
      console.log('The following error occurred when trying to use getUserMedia: ' + err);
    }
  );

} else {
  alert('Sorry, your browser does not support getUserMedia');
}
							
}



// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
    var params;
    var dataURL;
    context.drawImage(video, 0, 0, 320, 240);


    dataURL = canvas.toDataURL('image/png');

    params = "imgBase64=" + dataURL;

    http.open("POST", url,true);
	    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	    http.send( params);


});
