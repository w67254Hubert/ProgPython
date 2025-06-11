document.addEventListener('DOMContentLoaded', () => {
    // Obsługa przycisku "Zaloguj" na stronie logowania
    const loginButton = document.getElementById('login-btn');
    if (loginButton) {
        loginButton.addEventListener('click', (event) => {
            event.preventDefault(); // Zapobiegaj domyślnej akcji (np. submit formy)
            // Symulacja udanego logowania - przekierowanie do panelu portfela
            window.location.href = 'portfolio.html';
        });
    }

    // Obsługa przycisku "Rejestruj" na stronie logowania
    const registerPageButton = document.getElementById('register-page-btn');
    if (registerPageButton) {
        registerPageButton.addEventListener('click', (event) => {
            event.preventDefault();
            window.location.href = 'register.html'; // Przekierowanie do strony rejestracji
        });
    }

    // Obsługa przycisku "Zaloguj" na stronie rejestracji
    const registerButton = document.getElementById('register-btn');
    if (registerButton) {
        registerButton.addEventListener('click', (event) => {
            event.preventDefault();
            // Symulacja udanej rejestracji - przekierowanie do panelu portfela
            window.location.href = 'portfolio.html';
        });
    }

    // Pozostałe przyciski nawigacyjne (Wyloguj, Portfel, Wizualizacje)
    // będą teraz po prostu linkami <a> z odpowiednimi href, nie potrzebują JS.
});