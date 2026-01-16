document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    // Default is dark by CSS, so we only need to act if light is saved
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        updateIcon(false);
    } else {
        // No saved theme or 'dark' saved - remove attribute to use default (dark)
        document.documentElement.removeAttribute('data-theme');
        updateIcon(true);
    }

    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        // If data-theme is 'light', we want to go dark (remove attr)
        // If data-theme is null (default dark), we want to go light

        if (currentTheme === 'light') {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'dark');
            updateIcon(true);
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            updateIcon(false);
        }
    });

    function updateIcon(isDark) {
        themeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    }
});
