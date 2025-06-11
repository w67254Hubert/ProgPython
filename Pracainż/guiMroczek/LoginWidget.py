from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
    QCheckBox, QSpacerItem, QSizePolicy, QApplication
)
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt, QSize

# Twoje zdefiniowane kolory
KOLOR_AKCENTUJACY_1 = "#35DFE1"
ZMNIEJSZONA_SATURACJA_AKCENTU_1 = "#4AB4B6"
# KOLOR_AKCENTUJACY_2 = "#A02222" # Nieużywany bezpośrednio na tym ekranie
# KOLOR_GLOWNY_1 = "#5F7D77" # Nieużywany bezpośrednio na tym ekranie
# TLO_2 = "#485251" # Panel logowania wydaje się używać Tlo3 jako głównego tła
TLO_3_CIEMNE = "#313636" # Tło całego panelu logowania
KOLOR_TEKSTU_BIALY = "#FFFFFF"
KOLOR_TEKSTU_W_POLACH = "#202020" # Ciemny tekst w białych polach
KOLOR_PLACEHOLDER = "#A0A0A0" # Kolor tekstu placeholder
KOLOR_TEKSTU_NA_PRZYCISKACH = TLO_3_CIEMNE # Ciemny tekst na jasnych przyciskach


class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LoginWidget")
        
        # Dodanie fontu Inter (zakładając, że plik .ttf jest w katalogu 'fonts')
        # Możesz to zrobić raz w głównej aplikacji
        # font_id = QFontDatabase.addApplicationFont("fonts/Inter-Regular.ttf")
        # font_id_bold = QFontDatabase.addApplicationFont("fonts/Inter-Bold.ttf")
        # if font_id != -1 and font_id_bold != -1:
        #     self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        #     self.font_family_bold = QFontDatabase.applicationFontFamilies(font_id_bold)[0]
        # else:
        #     print("Nie udało się załadować fontu Inter. Używam domyślnego.")
        self.font_family = "Inter" # Jeśli zainstalowany w systemie lub obsłużony globalnie
        self.font_family_bold = "Inter"


        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        # Główny layout pionowy, który będzie centrował formularz
        outer_layout = QVBoxLayout(self)
        outer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer_layout.setContentsMargins(20, 20, 20, 20)

        # Kontener dla formularza, aby móc kontrolować jego szerokość
        form_container = QWidget()
        form_container.setObjectName("formContainer")
        # form_container.setFixedWidth(400) # Możesz ustawić stałą szerokość
        form_container.setMaximumWidth(450) # Lub maksymalną

        layout = QVBoxLayout(form_container)
        layout.setSpacing(18) # Odstępy między głównymi elementami
        layout.setContentsMargins(0,0,0,0) # Brak dodatkowych marginesów w kontenerze formularza

        # Tytuł "Zaloguj"
        self.title_label = QLabel("Zaloguj")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)
        layout.addSpacerItem(QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)) # Odstęp pod tytułem

        # Pole Email
        self.email_label = QLabel("Email")
        self.email_label.setObjectName("formFieldLabel")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setObjectName("formLineEdit")
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))


        # Pole Hasło
        self.password_label = QLabel("Hasło")
        self.password_label.setObjectName("formFieldLabel")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Hasło")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("formLineEdit")
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        
        # Checkbox "Zapamiętaj mnie"
        self.remember_me_checkbox = QCheckBox("Zapamiętaj mnie")
        self.remember_me_checkbox.setObjectName("rememberMeCheckbox")
        # self.remember_me_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight) # Domyślnie
        layout.addWidget(self.remember_me_checkbox)
        layout.addSpacerItem(QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Przyciski "Zaloguj" i "Rejestruj" w poziomie
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15) 
        
        self.login_button = QPushButton("Zaloguj")
        self.login_button.setObjectName("accentButton")
        self.login_button.setMinimumHeight(45) # Ustawienie minimalnej wysokości przycisku
        
        self.register_button = QPushButton("Rejestruj")
        self.register_button.setObjectName("accentButton") # Ten sam styl co Zaloguj wg obrazka
        self.register_button.setMinimumHeight(45)

        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.register_button)
        layout.addLayout(buttons_layout)
        layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Link "Zapomniałeś hasła?"
        self.forgot_password_link = QLabel()
        self.forgot_password_link.setObjectName("forgotPasswordLink")
        # Używamy HTML do stylizacji linku i umożliwienia kliknięcia
        self.forgot_password_link.setText(f"<a href='#' style='color:{ZMNIEJSZONA_SATURACJA_AKCENTU_1}; text-decoration:underline;'>Zapomniałeś hasła?</a>")
        self.forgot_password_link.setTextFormat(Qt.TextFormat.RichText)
        self.forgot_password_link.setOpenExternalLinks(False) # Aby obsłużyć sygnał linkActivated
        self.forgot_password_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.forgot_password_link.linkActivated.connect(self.on_forgot_password_clicked) # Podłącz sygnał
        layout.addWidget(self.forgot_password_link)

        outer_layout.addWidget(form_container)

    def apply_styles(self):
        style_sheet = f"""
            QWidget#LoginWidget {{
                background-color: {TLO_3_CIEMNE};
            }}
            QWidget#formContainer {{
                background-color: transparent; /* Dziedziczy tło z LoginWidget */
            }}
            QLabel#titleLabel {{
                color: {KOLOR_TEKSTU_BIALY};
                font-family: "{self.font_family_bold}", Inter, sans-serif; /* Dodane rezerwowe fonty */
                font-size: 56px; /* Duży tytuł */
                font-weight: bold; /* Jeśli font Inter-Bold nie jest używany globalnie */
                padding-bottom: 10px;
            }}
            QLabel#formFieldLabel {{
                color: {KOLOR_TEKSTU_BIALY};
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 15px;
                padding-bottom: 6px; /* Odstęp od pola */
            }}
            QLineEdit#formLineEdit {{
                background-color: {KOLOR_TEKSTU_BIALY};
                color: {KOLOR_TEKSTU_W_POLACH};
                border: none;
                border-radius: 8px; /* Zaokrąglenie */
                padding: 12px;
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 16px;
                min-height: 22px; /* Zapewnia odpowiednią wysokość pola */
            }}
            QLineEdit#formLineEdit::placeholder {{
                color: {KOLOR_PLACEHOLDER};
            }}
            QCheckBox#rememberMeCheckbox {{
                color: {KOLOR_TEKSTU_BIALY};
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 15px;
                spacing: 10px; /* Odstęp między kwadracikiem a tekstem */
            }}
            QCheckBox#rememberMeCheckbox::indicator {{
                width: 18px;
                height: 18px;
                border: 1px solid {KOLOR_TEKSTU_BIALY}; /* Ramka, gdy nie jest zaznaczony */
                border-radius: 4px;
                background-color: transparent;
            }}
            QCheckBox#rememberMeCheckbox::indicator:checked {{
                background-color: {KOLOR_AKCENTUJACY_1};
                border: 1px solid {KOLOR_AKCENTUJACY_1};
                /* Możesz dodać obrazek ptaszka, jeśli domyślny nie wygląda dobrze */
                /* image: url(path/to/checkmark_icon_white.svg); */
            }}
            QCheckBox#rememberMeCheckbox::indicator:hover {{
                border: 1px solid {ZMNIEJSZONA_SATURACJA_AKCENTU_1};
            }}
            QPushButton#accentButton {{
                background-color: {KOLOR_AKCENTUJACY_1};
                color: {KOLOR_TEKSTU_NA_PRZYCISKACH};
                border: none;
                border-radius: 8px;
                padding: 10px 15px; /* Dopasuj padding do wyglądu */
                font-family: "{self.font_family}", Inter, sans-serif; /* Pogrubienie przez 'font-weight' */
                font-size: 17px;
                font-weight: 600; /* Semi-bold */
                min-height: 28px; /* Aby przycisk był odpowiednio wysoki */
            }}
            QPushButton#accentButton:hover {{
                background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1};
            }}
            QPushButton#accentButton:pressed {{
                background-color: {KOLOR_AKCENTUJACY_1}; /* Można dodać efekt wciśnięcia */
            }}
            QLabel#forgotPasswordLink a {{
                color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1};
                text-decoration: underline;
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 14px;
            }}
            QLabel#forgotPasswordLink a:hover {{
                color: {KOLOR_AKCENTUJACY_1}; /* Jaśniejszy kolor przy najechaniu */
            }}
        """
        self.setStyleSheet(style_sheet)

    # Przykład metody do podłączenia sygnału z linku
    # def on_forgot_password_clicked(self, link):
    #     print(f"Link '{link}' kliknięty! Tu obsługa 'Zapomniałeś hasła?'")

# --- Do testowania widgetu ---
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # ---- WAŻNE: Ładowanie fontu Inter ----
    # Upewnij się, że masz pliki fontu Inter (np. Inter-Regular.ttf, Inter-Bold.ttf)
    # w katalogu 'fonts' lub zainstalowane w systemie.
    # Poniższy kod ładuje fonty z plików.
    font_dir = "fonts" # Załóżmy, że jest taki katalog obok skryptu
    regular_loaded = QFontDatabase.addApplicationFont(f"{font_dir}/Inter-Regular.ttf")
    bold_loaded = QFontDatabase.addApplicationFont(f"{font_dir}/Inter-Bold.ttf")
    
    if regular_loaded == -1 or bold_loaded == -1:
        print("Ostrzeżenie: Nie udało się załadować fontów Inter z plików. Upewnij się, że są w katalogu 'fonts' lub zainstalowane systemowo.")
        print(f"Ścieżka regular: {font_dir}/Inter-Regular.ttf, loaded_id: {regular_loaded}")
        print(f"Ścieżka bold: {font_dir}/Inter-Bold.ttf, loaded_id: {bold_loaded}")
    else:
        print("Fonty Inter załadowane poprawnie.")
    # ------------------------------------

    login_screen = LoginWidget()
    login_screen.resize(800, 600) # Przykładowy rozmiar okna
    login_screen.show()
    sys.exit(app.exec())