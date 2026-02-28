document.addEventListener('DOMContentLoaded', () => {

  /* ---- NAVBAR SCROLL ---- */
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });

  /* ---- MOBILE MENU ---- */
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  hamburger.addEventListener('click', () => mobileMenu.classList.toggle('open'));
  document.querySelectorAll('.mob-link').forEach(link => {
    link.addEventListener('click', () => mobileMenu.classList.remove('open'));
  });

  /* ---- SMOOTH SCROLL ---- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 80, behavior: 'smooth' });
      }
    });
  });

  /* ---- FADE IN ON SCROLL ---- */
  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('visible'); fadeObserver.unobserve(entry.target); }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.fade-in-up').forEach(el => fadeObserver.observe(el));

  /* ---- HERO SLIDER ---- */
  const slides = document.querySelectorAll('.hero-slide');
  if (slides.length > 0) {
    let currentSlide = 0;

    function playActiveSlide() {
      const slide = slides[currentSlide];
      const duration = parseInt(slide.getAttribute('data-duration'), 10) || 6000;

      // Pause all background videos to save resources
      slides.forEach(s => {
        const v = s.querySelector('video');
        if (v) v.pause();
      });

      // Play the active video from its exact starting timestamp
      const video = slide.querySelector('video');
      if (video) {
        const startSec = parseFloat(slide.getAttribute('data-video-start')) || 0;
        video.currentTime = startSec;
        video.play().catch(e => console.log("Autoplay blocked:", e));
      }

      setTimeout(() => {
        slide.classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');

        playActiveSlide();
      }, duration);
    }

    // Initialize loop
    playActiveSlide();
  }

  /* ---- COUNTER ANIMATION ---- */
  const countEls = document.querySelectorAll('.stat-number[data-target]');
  const countUp = (el) => {
    const target = parseInt(el.getAttribute('data-target'), 10);
    const duration = 1800;
    const start = performance.now();
    const step = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.floor(eased * target).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const countObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { countUp(e.target); countObserver.unobserve(e.target); } });
  }, { threshold: 0.5 });
  countEls.forEach(el => countObserver.observe(el));

  /* ---- FORM SUBMISSION (Redirect based to preserve FormSubmit workflow) ---- */
  // Instead of intercepting the submit using JS which can block the FormSubmit 
  // Captcha or redirect, we will allow the native HTML form submit to proceed.
  // We added a hidden _next field in the HTML to redirect back to this page with ?success=true

  // Checking if redirected back after successful submission
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.get('success') === 'true') {
    const applyForm = document.getElementById('applyForm');
    const formSuccess = document.getElementById('formSuccess');
    if (applyForm && formSuccess) {
      applyForm.style.display = 'none';
      formSuccess.style.display = 'block';
      // Scroll down to the contact secton to show success message
      setTimeout(() => {
        const contactSec = document.getElementById('contact');
        if (contactSec) window.scrollTo({ top: contactSec.getBoundingClientRect().top + window.scrollY - 80, behavior: 'smooth' });
      }, 500);
    }
  }

});
