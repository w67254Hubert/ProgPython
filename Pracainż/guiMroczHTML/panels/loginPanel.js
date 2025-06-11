// panels/loginPanel.js

function getLoginPanelHTML() {
    return `
        <div id="login-panel" class="panel login-register-form-panel">
            <h1>Zaloguj</h1>
            <form id="login-form">
                <div class="form-group">
                    <label for="login-email">Email</label>
                    <input type="email" id="login-email" placeholder="Email" required>
                </div>
                <div class="form-group">
                    <label for="login-password">Hasło</label>
                    <input type="password" id="login-password" placeholder="Hasło" required>
                </div>
                <div class="form-group form-options">
                    <label><input type="checkbox" id="remember-me"> Zapamiętaj mnie</label>
                </div>
                <div class="form-group button-group">
                    <button type="button" id="login-button" class="btn btn-accent">Zaloguj</button>
                    <button type="button" id="go-to-register-button" class="btn btn-accent">Rejestruj</button>
                </div>
                <a href="#" class="form-link" id="forgot-password">Zapomniałeś hasła?</a>
            </form>
        </div>
    `;
}

function attachLoginPanelListeners(navigateTo) {
    const loginButton = document.getElementById('login-button');
    if (loginButton) {
        loginButton.addEventListener('click', () => {
            console.log('Logowanie...');
            // Tutaj logika walidacji, a następnie nawigacja
            // Na przykład, pobranie nazwy użytkownika i przekazanie jej:
            // const username = "UserFromLogin"; // Pobierz z backendu po udanym logowaniu
            // navigateTo('portfolio', { username: username, direction: 'slide-left' });
            navigateTo('portfolio', { direction: 'slide-left' }); 
        });
    }

    const goToRegisterButton = document.getElementById('go-to-register-button');
    if (goToRegisterButton) {
        goToRegisterButton.addEventListener('click', () => {
            navigateTo('register', { direction: 'slide-left' });
        });
    }
    
    const forgotPasswordLink = document.getElementById('forgot-password');
    if(forgotPasswordLink) {
        forgotPasswordLink.addEventListener('click', (e) => {
            e.preventDefault();
            alert('Funkcja "Zapomniałeś hasła?" do zaimplementowania.');
        });
    }
}