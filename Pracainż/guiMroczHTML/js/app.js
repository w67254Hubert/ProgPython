// js/app.js
document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('app-container');
    let currentActivePanel = null; // Przechowuje aktualnie widoczny element panelu

    // Mapowanie nazw paneli na ich funkcje generujące HTML i dołączające listenery
    const panelConfig = {
        'login': { html: getLoginPanelHTML, listeners: attachLoginPanelListeners },
        'register': { html: getRegisterPanelHTML, listeners: attachRegisterPanelListeners },
        'portfolio': { html: getPortfolioPanelHTML, listeners: attachPortfolioPanelListeners },
        'market': { html: getMarketPanelHTML, listeners: attachMarketPanelListeners },
    };

    // Globalna funkcja nawigacji
    window.navigateTo = (panelName, options = {}) => {
        const config = panelConfig[panelName];
        if (!config) {
            console.error(`Panel o nazwie '${panelName}' nie został znaleziony w konfiguracji.`);
            return;
        }

        const { html: htmlGenerator, listeners: attachListeners } = config;
        const { direction = 'slide-left', ...params } = options; // Domyślny kierunek i reszta parametrów

        // Tworzenie nowego panelu
        const newPanelHTML = htmlGenerator(params); // Przekaż parametry (np. username)
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = newPanelHTML.trim();
        const newPanelElement = tempDiv.firstChild;

        if (!newPanelElement) {
            console.error("Nie udało się stworzyć elementu dla nowego panelu.");
            return;
        }

        const prevPanel = currentActivePanel;

        if (prevPanel) {
            // Ustalanie klasy wyjścia dla poprzedniego panelu
            if (direction === 'slide-left') { // Nowy wjeżdża z prawej, stary w lewo
                prevPanel.classList.add('exiting-left');
            } else if (direction === 'slide-right') { // Nowy wjeżdża z lewej, stary w prawo
                prevPanel.classList.add('exiting-right');
            } else { // Domyślnie fade-out (choć obecne CSS tego nie obsługuje w pełni)
                prevPanel.classList.remove('active'); // Powoduje domyślną animację wyjścia
            }

            // Usuń poprzedni panel po zakończeniu animacji
            // Użyj `animationend` lub `transitionend` w zależności od typu animacji w CSS
            prevPanel.addEventListener('transitionend', function onExitAnimationEnd() {
                prevPanel.removeEventListener('transitionend', onExitAnimationEnd);
                if (prevPanel.parentNode) {
                    prevPanel.remove();
                }
            });
        }
        
        // Dodaj nowy panel i uruchom animację wejścia
        appContainer.appendChild(newPanelElement);
        
        // Wymuś reflow przed dodaniem klasy active, aby animacja zadziałała poprawnie
        void newPanelElement.offsetWidth; 
        
        newPanelElement.classList.add('active');
        currentActivePanel = newPanelElement;

        // Dołącz listenery do nowego panelu
        if (attachListeners) {
            attachListeners(window.navigateTo, params); // Przekaż funkcję navigateTo i parametry
        }
    };

    // Inicjalizacja: załaduj panel logowania jako pierwszy
    window.navigateTo('login', { direction: 'initial' }); // 'initial' dla braku animacji
});