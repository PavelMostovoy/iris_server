// Grab elements, create settings, etc.
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var http = new XMLHttpRequest();
var url = "/api";


// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
    video.src = window.URL.createObjectURL(stream);
    video.play();
    });
}



// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
    var params;
    var dataURL;
    context.drawImage(video, 0, 0, 640,480);

    dataURL = canvas.toDataURL('image/png');
    params = "imgBase64=" + dataURL;

    //console.log(params);

    http.open("POST", url,true);
    //http.onreadystatechange = function() {
   // console.log(http.responseText);
 // }
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.send(params);

});

