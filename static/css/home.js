
document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider");
    const slides = document.querySelectorAll(".slider img");
    const dots = document.querySelectorAll(".slider-nav a");
    let currentIndex = 0;
    const totalSlides = slides.length;

    function updateSlider(index) {
        slider.scrollTo({
            left: slider.clientWidth * index,
            behavior: "smooth"
        });
        dots.forEach(dot => dot.classList.remove("active"));
        dots[index].classList.add("active");
    }

    function autoScroll() {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateSlider(currentIndex);
    }

    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            currentIndex = index;
            updateSlider(index);
        });
    });

    // Auto-scroll every 3 seconds
    let autoScrollInterval = setInterval(autoScroll, 3000);

    // Pause auto-scroll on hover
    slider.addEventListener("mouseenter", () => clearInterval(autoScrollInterval));
    slider.addEventListener("mouseleave", () => {
        autoScrollInterval = setInterval(autoScroll, 3000);
    });

    // Initialize the first dot as active
    dots[0].classList.add("active");
});

const logoImage = document.querySelector('div.logo img');
const logoDiv = document.querySelector('div.logo');

async function setLogoStyles() {
    await setElementStyles(logoImage, {
        width: '80px',
        height: 'auto',
        objectFit: 'contain',
    });

    await setElementStyles(logoDiv, {
        width: '80px',
        height: '60px',
    });
}

setLogoStyles();