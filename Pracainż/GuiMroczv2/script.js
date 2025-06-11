document.addEventListener('DOMContentLoaded', () => {
    // Referencje do paneli
    const loginPanel = document.getElementById('login-panel');
    const registrationPanel = document.getElementById('registration-panel');
    const appContainer = document.getElementById('app-container'); // Główny kontener aplikacji
    const portfolioPanel = document.getElementById('portfolio-panel');
    const visualizationPanel = document.getElementById('visualization-panel');

    // Referencje do przycisków nawigacyjnych i formularzy
    const goToRegisterBtn = document.getElementById('go-to-register');
    const goToLoginFromRegBtn = document.getElementById('go-to-login-from-reg');
    const loginForm = document.getElementById('login-form');
    const registrationForm = document.getElementById('registration-form');
    const logoutBtn = document.getElementById('logout-btn');

    const navPortfolioBtn = document.getElementById('nav-portfolio');
    const navVisualizationBtn = document.getElementById('nav-visualization');

    // Domyślnie pokazuj panel logowania
    showAuthPanel('login-panel');

    function showAuthPanel(panelId) {
        loginPanel.classList.remove('active-panel');
        registrationPanel.classList.remove('active-panel');
        appContainer.classList.remove('active-panel'); // Ukryj główny kontener aplikacji

        if (panelId === 'login-panel') {
            loginPanel.classList.add('active-panel');
        } else if (panelId === 'registration-panel') {
            registrationPanel.classList.add('active-panel');
        }
    }

    function showAppPanel() {
        loginPanel.classList.remove('active-panel');
        registrationPanel.classList.remove('active-panel');
        appContainer.classList.add('active-panel'); // Pokaż główny kontener aplikacji
        showContentPanel('portfolio-panel'); // Domyślnie portfel po zalogowaniu
    }

    function showContentPanel(panelId) {
        portfolioPanel.classList.remove('active-content');
        visualizationPanel.classList.remove('active-content');

        navPortfolioBtn.classList.remove('active');
        navVisualizationBtn.classList.remove('active');

        if (panelId === 'portfolio-panel') {
            portfolioPanel.classList.add('active-content');
            navPortfolioBtn.classList.add('active');
        } else if (panelId === 'visualization-panel') {
            visualizationPanel.classList.add('active-content');
            navVisualizationBtn.classList.add('active');
        }
    }

    // Nawigacja między logowaniem a rejestracją
    if (goToRegisterBtn) {
        goToRegisterBtn.addEventListener('click', () => showAuthPanel('registration-panel'));
    }
    if (goToLoginFromRegBtn) {
        goToLoginFromRegBtn.addEventListener('click', () => showAuthPanel('login-panel'));
    }

    // Logika logowania
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Tutaj logika weryfikacji danych logowania
            console.log('Logowanie...');
            // Jeśli poprawne:
            const username = loginForm.querySelector('#login-email').value.split('@')[0]; // Przykładowa nazwa użytkownika
            document.querySelector('.app-header .username').textContent = username || "User123123";
            showAppPanel();
        });
    }

    // Logika rejestracji
    if (registrationForm) {
        registrationForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Tutaj logika weryfikacji i zapisu danych rejestracji
            console.log('Rejestracja...');
            // Jeśli poprawna:
            const username = registrationForm.querySelector('#reg-username').value;
            document.querySelector('.app-header .username').textContent = username || "User123123";
            showAppPanel();
        });
    }

    // Wylogowanie
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            console.log('Wylogowano');
            showAuthPanel('login-panel');
        });
    }

    // Nawigacja w głównej aplikacji
    if (navPortfolioBtn) {
        navPortfolioBtn.addEventListener('click', () => showContentPanel('portfolio-panel'));
    }
    if (navVisualizationBtn) {
        navVisualizationBtn.addEventListener('click', () => showContentPanel('visualization-panel'));
    }


    // --- Logika dla Panelu Portfela ---
    const addAssetForm = document.getElementById('add-asset-form');
    const portfolioAssetsTableBody = document.getElementById('portfolio-assets-table');

    if (addAssetForm && portfolioAssetsTableBody) {
        addAssetForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('add-crypto-name').value;
            const amount = parseFloat(document.getElementById('add-crypto-amount').value);

            if (name && amount > 0) {
                // TODO: Zintegrować z API do pobierania ceny i wartości
                const price = Math.random() * 1000; // Placeholder
                const value = price * amount;

                const newRow = portfolioAssetsTableBody.insertRow();
                newRow.innerHTML = `
                    <td>${name}</td>
                    <td>${amount.toFixed(2)}</td>
                    <td>${price.toFixed(2)}</td>
                    <td>${value.toFixed(2)}</td>
                `;
                addAssetForm.reset();
                console.log(`Dodano: ${name}, Ilość: ${amount}`);
            } else {
                alert('Wprowadź poprawną nazwę i ilość.');
            }
        });
    }

    const sellAssetForm = document.getElementById('sell-asset-form');
    const soldAssetsTableBody = document.getElementById('sold-assets-table');

    if (sellAssetForm && soldAssetsTableBody) {
        sellAssetForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('sell-crypto-name').value;
            const amount = parseFloat(document.getElementById('sell-crypto-amount').value);

            if (name && amount > 0) {
                // TODO: Logika sprzedaży, usuwanie z portfela, dodawanie do sprzedanych
                const purchasePrice = Math.random() * 900; // Placeholder
                const sellPrice = purchasePrice * (1 + (Math.random() - 0.4) / 5); // Placeholder

                const newRow = soldAssetsTableBody.insertRow();
                newRow.innerHTML = `
                    <td>${name}</td>
                    <td>${amount.toFixed(2)}</td>
                    <td>${(purchasePrice * amount).toFixed(2)}</td>
                    <td>${(sellPrice * amount).toFixed(2)}</td>
                `;
                sellAssetForm.reset();
                console.log(`Sprzedano: ${name}, Ilość: ${amount}`);
            } else {
                alert('Wprowadź poprawną nazwę i ilość.');
            }
        });
    }

    const updateForecastBtn = document.getElementById('update-forecast-btn');
    const forecastResultsTableBody = document.getElementById('forecast-results-table');
    if (updateForecastBtn && forecastResultsTableBody) {
        updateForecastBtn.addEventListener('click', () => {
            console.log('Aktualizowanie prognozy portfela...');
            // Placeholder - aktualizacja tabeli prognoz
            const currentValue = Math.random() * 10000;
            forecastResultsTableBody.innerHTML = `
                <tr>
                    <td>${currentValue.toFixed(2)}</td>
                    <td>${(currentValue * (1 + (Math.random() - 0.5) / 10)).toFixed(2)}</td>
                    <td>${(currentValue * (1 + (Math.random() - 0.5) / 8)).toFixed(2)}</td>
                    <td>${(currentValue * (1 + (Math.random() - 0.5) / 5)).toFixed(2)}</td>
                </tr>
            `;
            alert('Prognozy zaktualizowane (dane placeholder).');
        });
    }

    const optimizePortfolioBtn = document.getElementById('optimize-portfolio-btn');
    const optimizationResultsDiv = document.getElementById('optimization-results');
    if (optimizePortfolioBtn && optimizationResultsDiv) {
        optimizePortfolioBtn.addEventListener('click', () => {
            console.log('Optymalizacja portfela...');
            optimizationResultsDiv.textContent = 'Analizowanie portfela... Proszę czekać.';
            setTimeout(() => {
                optimizationResultsDiv.innerHTML = `
                    <p><strong>Rekomendacje:</strong></p>
                    <ul>
                        <li>Rozważ zwiększenie udziału w XYZ Coin o 15%.</li>
                        <li>Zmniejsz pozycję w ABC Token o 10% ze względu na wysoką zmienność.</li>
                        <li>Dodaj DEF Stablecoin dla dywersyfikacji i zmniejszenia ryzyka.</li>
                    </ul>
                `;
                alert('Optymalizacja zakończona (dane placeholder).');
            }, 2000);
        });
    }

    // --- Logika dla Panelu Wizualizacji ---
    const analyzeCryptoForm = document.getElementById('analyze-crypto-form');
    const selectedCryptoNameStats = document.getElementById('selected-crypto-name-stats');
    const statKeyValue = document.getElementById('stat-key-value');
    const statMarketCap = document.getElementById('stat-market-cap');
    const statVolume24h = document.getElementById('stat-volume-24h');
    const change24h = document.getElementById('change-24h');
    const change7d = document.getElementById('change-7d');
    const change1m = document.getElementById('change-1m');

    if (analyzeCryptoForm) {
        analyzeCryptoForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const cryptoToAnalyze = document.getElementById('analyze-crypto-input').value.trim();
            if (cryptoToAnalyze) {
                console.log(`Analizowanie: ${cryptoToAnalyze}`);
                selectedCryptoNameStats.textContent = cryptoToAnalyze.toUpperCase();
                // Placeholder - aktualizacja statystyk
                statKeyValue.textContent = `${(Math.random()*50000).toFixed(2)} USD`;
                statMarketCap.textContent = `${(Math.random()*100).toFixed(2)}B`;
                statVolume24h.textContent = `${(Math.random()*500).toFixed(0)}tys.`;

                const c24 = (Math.random() - 0.5) * 20;
                const c7d = (Math.random() - 0.5) * 40;
                const c1m = (Math.random() - 0.5) * 60;

                change24h.textContent = `${c24.toFixed(2)}%`;
                change24h.className = `stat-value price-change ${c24 >= 0 ? 'positive' : 'negative'}`;
                change7d.textContent = `${c7d.toFixed(2)}%`;
                change7d.className = `stat-value price-change ${c7d >= 0 ? 'positive' : 'negative'}`;
                change1m.textContent = `${c1m.toFixed(2)}%`;
                change1m.className = `stat-value price-change ${c1m >= 0 ? 'positive' : 'negative'}`;

                alert(`Wygenerowano analizę dla ${cryptoToAnalyze} (dane placeholder).`);
                // Tutaj można by też dynamicznie zmieniać src obrazków wykresów, jeśli byłyby generowane
            } else {
                alert('Wprowadź nazwę kryptowaluty do analizy.');
            }
        });
    }
});