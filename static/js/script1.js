// Grab elements, create settings, etc.
var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var dataURL = canvas.toDataURL('image/png');
var params =  "imgBase64=" + dataURL;
var http = new XMLHttpRequest();
var url = "/test";



// console.log(dataURL);

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
    context.drawImage(video, 0, 0, 320, 240);


    dataURL = canvas.toDataURL('image/png');
    params = "imgBase64=" + dataURL;
    // console.log(dataURL);

    http.open("POST", url,true);
	    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

	    http.send( params);





});





