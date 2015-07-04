$(function () {

	// Init Scroll Magic
	var scrollMagicController = new ScrollMagic();

	TweenMax.from('.devf-center-vh', 0.8,{
		y: 100,
		ease: Elastic.easeOut
	});

	var animateHDTexts = TweenMax.staggerFrom('.devf-hd-text', 0.3, {
		y: '500',
		ease: Power2.easeIn
	});

	var scene = new ScrollScene({
	    triggerElement: '#devf-hacker-definitions',
	    offset: 1
	})
	.setTween(animateHDTexts)
	.addTo(scrollMagicController);
});
