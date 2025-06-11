// panels/registerPanel.js

function getRegisterPanelHTML() {
    return `
        <div id="register-panel" class="panel login-register-form-panel">
            <h1>Rejestracja</h1>
            <form id="register-form">
                <div class="form-group">
                    <label for="register-username">Nazwa użytkownika</label>
                    <input type="text" id="register-username" placeholder="Nazwa" required>
                </div>
                <div class="form-group">
                    <label for="register-email">Email</label>
                    <input type="email" id="register-email" placeholder="Email" required>
                </div>
                <div class="form-group">
                    <label for="register-password">Hasło</label>
                    <input type="password" id="register-password" placeholder="Hasło" required>
                </div>
                <div class="form-group button-group-single">
                    <button type="button" id="register-button" class="btn btn-accent">Zarejestruj</button>
                </div>
                <a href="#" id="go-to-login-from-register" class="form-link">Masz już konto? Zaloguj się</a>
            </form>
        </div>
    `;
}

function attachRegisterPanelListeners(navigateTo) {
    const registerButton = document.getElementById('register-button');
    if (registerButton) {
        registerButton.addEventListener('click', () => {
            console.log('Rejestracja...');
            // Logika walidacji i rejestracji
            navigateTo('portfolio', { direction: 'slide-left' }); // Po udanej rejestracji
        });
    }

    const goToLoginLink = document.getElementById('go-to-login-from-register');
    if (goToLoginLink) {
        goToLoginLink.addEventListener('click', (e) => {
            e.preventDefault();
            navigateTo('login', { direction: 'slide-right' });
        });
    }
}