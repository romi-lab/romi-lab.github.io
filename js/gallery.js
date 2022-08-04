var slideIndex = 0;
var grpIndex = 0;

showSlides(0, 0);
showSlides(0, 1);

// Next/previous controls
function plusSlides(n, d) {
	if (d != grpIndex){
		slideIndex = n;
	}else{
		slideIndex += n;
	}
	grpIndex = d;
	showSlides(slideIndex, grpIndex);
}

// Thumbnail image controls
function currentSlide(n, d) {
	slideIndex = n;
	showSlides(n, d);
}

function showSlides(n, d) {
	var i;
	var slides = document.getElementsByClassName("mySlides");
	var dots = document.getElementsByClassName("thumnbailImg");
	var dNumberBegin = 0;
	var dNumber = 0;

	if (n >= 5) {
		slideIndex = 4;
	} else if (n < 0) {
		slideIndex = 0;
	} else {
		slideIndex = n;
	}
	dNumberBegin = slides.length - (d+1) * 5;
	dNumber = dNumberBegin + slideIndex;	
	for (i = dNumberBegin; i < (dNumberBegin+5); i++) {
		slides[i].style.display = "none";
	}
	for (i = dNumberBegin; i < (dNumberBegin+5); i++) {
		dots[i].className = dots[i].className.replace(" active", "");
	}

	slides[dNumber].style.display = "block";
	dots[dNumber].className += " active";
}
