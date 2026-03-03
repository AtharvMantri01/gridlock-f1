/* ================================================================
   GridLock F1 — Main JavaScript
   Scroll animations · Mobile nav · Navbar scroll effect
   ================================================================ */

(function () {
    'use strict';

    // --- Scroll-triggered fade-in animations ---
    function initScrollAnimations() {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
        );

        document.querySelectorAll('.fade-in').forEach((el) => {
            observer.observe(el);
        });
    }

    // --- Navbar scroll effect ---
    function initNavbarScroll() {
        const navbar = document.getElementById('navbar');
        if (!navbar) return;

        let ticking = false;

        function onScroll() {
            if (!ticking) {
                requestAnimationFrame(() => {
                    navbar.classList.toggle('scrolled', window.scrollY > 50);
                    ticking = false;
                });
                ticking = true;
            }
        }

        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    // --- Mobile nav toggle ---
    function initMobileNav() {
        const toggle = document.getElementById('navToggle');
        const links = document.getElementById('navLinks');
        if (!toggle || !links) return;

        toggle.addEventListener('click', () => {
            links.classList.toggle('open');
            toggle.classList.toggle('active');
        });

        links.querySelectorAll('.nav-link').forEach((link) => {
            link.addEventListener('click', () => {
                links.classList.remove('open');
                toggle.classList.remove('active');
            });
        });
    }

    // --- Init ---
    function init() {
        initScrollAnimations();
        initNavbarScroll();
        initMobileNav();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
