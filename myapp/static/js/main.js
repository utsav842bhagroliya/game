// Get the modal
var ebModal = document.getElementById('mySizeChartModal');

// Get the button that opens the modal
var ebBtn = document.getElementById("mySizeChart");

// Get the <span> element that closes the modal
var ebSpan = document.getElementsByClassName("ebcf_close")[0];

// When the user clicks the button, open the modal 
ebBtn.onclick = function() {
    ebModal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
ebSpan.onclick = function() {
    ebModal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == ebModal) {
        ebModal.style.display = "none";
    }
}



function increment() {
    document.getElementById('demoInput').stepUp();
 }
 function decrement() {
    document.getElementById('demoInput').stepDown();
 }



// Get the modal
var wModal = document.getElementById('ChartModal');

// Get the button that opens the modal
var wBtn = document.getElementById("Chart");

// Get the <span> element that closes the modal
var wSpan = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
wBtn.onclick = function() {
    wModal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
wSpan.onclick = function() {
    wModal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == wModal) {
        wModal.style.display = "none";
    }
}