document.addEventListener('DOMContentLoaded', () => {
    // Generate stars
    const starsContainer = document.getElementById('stars');
    for (let i = 0; i < 50; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 1.5}s`;
        starsContainer.appendChild(star);
    }

    // Theme switching functionality
    const themeSwitch = document.querySelector('.theme-switch');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Set initial theme based on system preference
    const currentTheme = localStorage.getItem('theme') || 
        (prefersDarkScheme.matches ? 'dark' : 'light');
    document.body.setAttribute('data-theme', currentTheme);
    updateThemeButtonText(currentTheme);

    // Theme switch event listener
    themeSwitch.addEventListener('click', () => {
        const currentTheme = document.body.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        document.body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeButtonText(newTheme);
    });

    // Update theme button text
    function updateThemeButtonText(theme) {
        themeSwitch.textContent = theme === 'light' 
            ? '🌙 Night Falls' 
            : '☀️ Dawn Breaks';
    }

    // Form submission
    const loginForm = document.querySelector('form');
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const username = document.querySelector('#username').value;
        const password = document.querySelector('#password').value;
        
        // Add your authentication logic here
        console.log('Login attempt:', { username, password });
        
        // Example animation for form submission
        const button = document.querySelector('button[type="submit"]');
        button.textContent = 'Opening Gates...';
        button.style.opacity = '0.7';
        
        setTimeout(() => {
            button.textContent = 'Enter the Realm';
            button.style.opacity = '1';
        }, 2000);
    });
}); 