// panels/marketPanel.js

function getMarketPanelHTML(params = {}) {
    const username = params.username || "User123123";
    return `
        <div id="market-panel" class="panel main-app-panel">
            <header class="app-header">
                 <div class="user-info">
                    <i class="fas fa-user-circle user-icon"></i>
                    <span id="username-display-market">${username}</span>
                    <button id="logout-button-market" class="btn-logout"><i class="fas fa-sign-out-alt"></i> Wyloguj</button>
                </div>
                <nav class="app-nav">
                    <button data-target-panel="portfolio" class="nav-tab">Portfel Kryptowalut</button>
                    <button data-target-panel="market" class="nav-tab active">Wizualizacje Rynkowe</button>
                </nav>
            </header>
            <main class="panel-content columns">
                <section class="column narrow-column">
                    <!-- Wybór kryptowaluty -->
                    <!-- Lista kryptowalut -->
                </section>
                <section class="column wide-column scrollable-column">
                    <!-- Statystyki -->
                    <!-- Wykresy -->
                </section>
            </main>
        </div>
    `;
}

function attachMarketPanelListeners(navigateTo, params = {}) {
     document.querySelectorAll('#market-panel .nav-tab').forEach(tab => {
        tab.addEventListener('click', (event) => {
            const targetPanel = event.currentTarget.dataset.targetPanel;
            if (targetPanel) {
                 navigateTo(targetPanel, { direction: targetPanel === 'portfolio' ? 'slide-right' : 'slide-left', username: params.username });
            }
        });
    });
    
    const logoutButton = document.getElementById('logout-button-market');
    if (logoutButton) {
        logoutButton.addEventListener('click', () => {
            navigateTo('login', { direction: 'slide-right' });
        });
    }
    // Listeners dla market panel
}