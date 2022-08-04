var a;	// true: landscape; false: portrait
if ($(window).height() > $(window).width()){
  a = false;
}else{
  a = true;
}

const fadeIn_controller = document.querySelectorAll(".fade-in");

const options_showUp = {
	threshold: 0,
	rootMargin: "0px 0px -300px 0px"
};

const scroll_showUp = new IntersectionObserver(function(entries,scroll_showUp) {
	entries.forEach(entry => {
		if (!entry.isIntersecting) {
			return;
		} else {
			entry.target.classList.add("showUp");
			scroll_showUp.unobserve(entry.target);
		}
	});
}, options_showUp);

const showUp = new IntersectionObserver(function(entries,showUp) {
	entries.forEach(entry => {
		entry.target.classList.add("showUp");
		scroll_showUp.unobserve(entry.target);
	});
}, options_showUp);

fadeIn_controller.forEach(fader => {
	scroll_showUp.observe(fader);
	if (a == true){
		scroll_showUp.observe(fader);
	}else{
		showUp.observe(fader);
	}

});
