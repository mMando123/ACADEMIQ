/**
 * ACADEMIQ - Main JavaScript
 * Handles UI interactions and UX enhancements.
 * No external dependencies (GSAP removed).
 */

document.addEventListener('DOMContentLoaded', () => {

    // 1. Skeleton Loader Simulation for Images
    const lazyImages = document.querySelectorAll('img');
    lazyImages.forEach(img => {
        if (!img.complete) {
            img.classList.add('animate-pulse', 'bg-secondary-200', 'dark:bg-secondary-700');
            img.addEventListener('load', () => {
                img.classList.remove('animate-pulse', 'bg-secondary-200', 'dark:bg-secondary-700');
            });
        }
    });

    // 2. Form Progress Indicator for Order Page
    const orderProgressBar = document.getElementById('order-progress-bar');
    if (orderProgressBar) {
        const form = orderProgressBar.closest('form') || document.querySelector('form');
        if (form) {
            const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
            const updateProgress = () => {
                let filled = 0;
                inputs.forEach(input => {
                    if (input.value.trim() !== '') filled++;
                });
                const percentage = inputs.length > 0 ? (filled / inputs.length) * 100 : 0;
                orderProgressBar.style.width = `${Math.max(5, percentage)}%`;
            };
            inputs.forEach(input => {
                input.addEventListener('input', updateProgress);
                input.addEventListener('change', updateProgress);
            });
        }
    }

    // 3. Micro-interactions for Buttons
    document.querySelectorAll('button[type="submit"], .btn').forEach(btn => {
        btn.addEventListener('mousedown', () => btn.style.transform = 'scale(0.97)');
        btn.addEventListener('mouseup', () => btn.style.transform = '');
        btn.addEventListener('mouseleave', () => btn.style.transform = '');
    });

    // 4. Auto-dismiss flash messages after 6 seconds
    document.querySelectorAll('[data-auto-dismiss]').forEach(msg => {
        setTimeout(() => {
            msg.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            msg.style.opacity = '0';
            msg.style.transform = 'translateX(20px)';
            setTimeout(() => msg.remove(), 500);
        }, 6000);
    });

    // 5. Counter animation (used on home page)
    const counters = document.querySelectorAll('.counter');
    if (counters.length > 0) {
        const animateCounter = (counter) => {
            const target = parseInt(counter.getAttribute('data-target'), 10);
            const duration = 2000; // ms
            const startTime = performance.now();

            const step = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                // Ease-out cubic for smooth deceleration
                const easedProgress = 1 - Math.pow(1 - progress, 3);
                counter.textContent = Math.round(easedProgress * target).toLocaleString();

                if (progress < 1) {
                    requestAnimationFrame(step);
                }
            };
            requestAnimationFrame(step);
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    counters.forEach(animateCounter);
                    observer.disconnect();
                }
            });
        }, { threshold: 0.3 });

        observer.observe(counters[0].closest('section') || counters[0]);
    }

    // 6. Language switcher click toggle (desktop)
    document.querySelectorAll('.lang-switcher-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            const dropdown = toggle.nextElementSibling;
            if (dropdown) {
                dropdown.classList.toggle('hidden');
            }
        });
    });

    // Close language dropdown on outside click
    document.addEventListener('click', () => {
        document.querySelectorAll('.lang-dropdown').forEach(d => d.classList.add('hidden'));
    });

    console.log('%c ACADEMIQ System Loaded ', 'background: #0ea5e9; color: #fff; border-radius: 4px; padding: 2px 5px;');
});
