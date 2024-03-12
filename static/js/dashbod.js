
  
// Partner Logo Footer 
function partnersLogo () {
  var logoSlide = $("#partner_logo");
  if(logoSlide.length) {
      logoSlide.owlCarousel({
        loop:true,
        margin:-1,
        nav:false,
        dots:false,
        autoplay:true,
        autoplayTimeout:2000,
        autoplaySpeed:1000,
        lazyLoad:true,
        singleItem:true,
        responsive:{
            0:{
                items:1
            },
            550:{
                items:2
            },
            751:{
                items:3
            },
            1001:{
                items:5
            }
        }
    })
  }
}

