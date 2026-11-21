(() => {
    const root = document.documentElement;
    try {
        if (localStorage.getItem('portfolio-theme') === 'light') {
            root.dataset.theme = 'light';
        }
    } catch {
        // The switch also works for this page when browser storage is unavailable.
    }

    document.addEventListener('DOMContentLoaded', () => {
        const button = document.querySelector('.theme-toggle');
        function updateLabel() {
            const next = root.dataset.theme === 'light' ? 'dark' : 'light';
            button.title = `Switch to ${next} mode`;
            button.setAttribute('aria-label', button.title);
        }
        updateLabel();
        button.hidden = false;
        button.addEventListener('click', () => {
            root.dataset.theme = root.dataset.theme === 'light' ? 'dark' : 'light';
            updateLabel();
            try {
                localStorage.setItem('portfolio-theme', root.dataset.theme);
            } catch {
                // Keep the chosen theme active in memory.
            }
        });
    });
})();
