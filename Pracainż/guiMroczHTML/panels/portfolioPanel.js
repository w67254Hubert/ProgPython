// panels/portfolioPanel.js

function getPortfolioPanelHTML(params = {}) {
    const username = params.username || "User123123"; // Użyj przekazanej nazwy użytkownika lub domyślnej

    return `
        <div id="portfolio-panel" class="panel main-app-panel active"> {/* Dodana klasa active dla widoczności przy starcie */ }
            <header class="app-header">
                <div class="user-info">
                    <i class="fas fa-user-circle user-icon"></i>
                    <span id="username-display">${username}</span>
                    <button id="logout-button-portfolio" class="btn-logout">
                        <i class="fas fa-sign-out-alt"></i> Wyloguj
                    </button>
                </div>
                <nav class="app-nav">
                    <button data-target-panel="portfolio" class="nav-tab active">Portfel Kryptowalut</button>
                    <button data-target-panel="market" class="nav-tab">Wizualizacje Rynkowe</button>
                </nav>
            </header>

            <main class="panel-content columns">
                <section class="column left-column">
                    <!-- Karta: Dodanie aktywów -->
                    <div class="card">
                        <h2 class="card-title">Dodanie aktywów</h2>
                        <div class="card-content">
                            <form class="form-inline-card">
                                <div class="form-group">
                                    <label for="add-asset-name">Nazwa kryptowaluty</label>
                                    <select id="add-asset-name">
                                        <option selected disabled>Nazwa Kryptowaluty</option>
                                        <option value="btc">Bitcoin (BTC)</option>
                                        <option value="eth">Ethereum (ETH)</option>
                                        <option value="ada">Cardano (ADA)</option>
                                    </select>
                                </div>
                                <div class="form-group">
                                    <label for="add-asset-amount">Ilość aktywów</label>
                                    <input type="number" id="add-asset-amount" placeholder="Liczba">
                                </div>
                                <button type="button" class="btn btn-accent-small">Dodaj</button>
                            </form>
                        </div>
                    </div>

                    <!-- Karta: Aktywa w portfelu -->
                    <div class="card card-table-container"> 
                        <h2 class="card-title">Aktywa w portfelu</h2>
                        <div class="card-content full-height-content"> {/* Aby tabela wypełniła kartę */}
                            <table class="data-table" id="portfolio-assets-table">
                                <thead>
                                    <tr>
                                        <th>Kryptowaluta</th>
                                        <th>Ilość Aktywów</th>
                                        <th>Cena</th>
                                        <th>Wartość</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr><td>exsample</td><td>2.0</td><td>123.22</td><td>111.00</td></tr>
                                    <!-- Puste wiersze symulujące przestrzeń z obrazka -->
                                    ${Array(12).fill('<tr><td></td><td></td><td></td><td></td></tr>').join('')}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <section class="column right-column">
                    <!-- Karta: Sprzedaż aktywów -->
                    <div class="card">
                        <h2 class="card-title">Sprzedaż aktywów</h2>
                        <div class="card-content">
                            <form class="form-inline-card">
                                <div class="form-group">
                                    <label for="sell-asset-name">Nazwa kryptowaluty</label>
                                    <select id="sell-asset-name">
                                        <option selected disabled>Nazwa Kryptowaluty</option>
                                        {/* Dynamicznie wypełniane z portfela */}
                                    </select>
                                </div>
                                <div class="form-group">
                                    <label for="sell-asset-amount">Ilość aktywów</label>
                                    <input type="number" id="sell-asset-amount" placeholder="Liczba">
                                </div>
                                <button type="button" class="btn btn-danger-small">Sprzedaj</button>
                            </form>
                        </div>
                    </div>

                    <!-- Karta: Lista ostatnio sprzedanych aktywów -->
                    <div class="card">
                        <h2 class="card-title">Lista ostatnio sprzedanych aktywów</h2>
                        <div class="card-content">
                            <table class="data-table" id="sold-assets-table">
                                <thead>
                                    <tr>
                                        <th>Kryptowaluta</th>
                                        <th>Ilość Aktywów</th>
                                        <th>Cena zakupu</th>
                                        <th>Cena sprzedaży</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr><td>exsample</td><td>1.0</td><td>111.00</td><td>120.00</td></tr>
                                    ${Array(3).fill('<tr><td></td><td></td><td></td><td></td></tr>').join('')}
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Karta: Predykcja wartości portfela -->
                    <div class="card">
                        <h2 class="card-title">
                            Predykcja wartości portfela
                            <button class="btn btn-accent-small header-btn">Aktualizuj Prognozy</button>
                        </h2>
                        <div class="card-content prediction-area">
                            <div class="prediction-box">
                                <span>Aktualna wartość</span>
                                <strong>100.00</strong>
                            </div>
                            <div class="prediction-box">
                                <span>za 7 dni</span>
                                <strong>98.80</strong>
                            </div>
                            <div class="prediction-box">
                                <span>za 14 dni</span>
                                <strong>105.02</strong>
                            </div>
                             <div class="prediction-box">
                                <span>za 30 dni</span>
                                <strong>120.00</strong>
                            </div>
                        </div>
                    </div>

                    <!-- Karta: Optymalizacja portfela -->
                    <div class="card">
                        <h2 class="card-title">
                            Optymalizacja portfela
                            <button class="btn btn-accent-small header-btn">Optymalizuj</button>
                        </h2>
                        <div class="card-content">
                            <textarea class="optimization-results" readonly placeholder="Oczekiwanie na wynik optymalizacji..."></textarea>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    `;
}

// Funkcja attachPortfolioPanelListeners pozostaje taka sama jak poprzednio
function attachPortfolioPanelListeners(navigateTo, params = {}) {
    document.querySelectorAll('#portfolio-panel .nav-tab').forEach(tab => {
        tab.addEventListener('click', (event) => {
            const targetPanelId = event.currentTarget.dataset.targetPanel; // np. 'market'
            if (targetPanelId) {
                // Sprawdzenie kierunku animacji
                const currentPanelId = 'portfolio'; // Wiemy, że jesteśmy na panelu portfolio
                let direction = 'slide-left'; // Domyślnie
                if (targetPanelId === 'portfolio' && currentPanelId === 'market') {
                    direction = 'slide-right'; // Jeśli wracamy z market do portfolio
                }
                // Dla innych przejść można dodać logikę
                
                navigateTo(targetPanelId, { direction: direction, username: params.username });
            }
        });
    });

    const logoutButton = document.getElementById('logout-button-portfolio');
    if (logoutButton) {
        logoutButton.addEventListener('click', () => {
            navigateTo('login', { direction: 'slide-right' }); // Ucieka w prawo
        });
    }
    // Dodaj listenery dla przycisków "Dodaj", "Sprzedaj", "Aktualizuj Prognozy", "Optymalizuj"
    // Np.
    // const addButton = document.querySelector('#portfolio-panel .form-inline-card .btn-accent-small');
    // if(addButton) { /* ... */ }
}