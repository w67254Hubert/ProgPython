from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
    QSpacerItem, QSizePolicy, QApplication
)
from PyQt6.QtGui import QFontDatabase # Usunięto QFont, QSize - nieużywane bezpośrednio tu
from PyQt6.QtCore import Qt

# Twoje zdefiniowane kolory (te same co w LoginWidget)
KOLOR_AKCENTUJACY_1 = "#35DFE1"
ZMNIEJSZONA_SATURACJA_AKCENTU_1 = "#4AB4B6"
TLO_3_CIEMNE = "#313636" # Tło całego panelu
KOLOR_TEKSTU_BIALY = "#FFFFFF"
KOLOR_TEKSTU_W_POLACH = "#202020" # Ciemny tekst w białych polach
KOLOR_PLACEHOLDER = "#A0A0A0" # Kolor tekstu placeholder
KOLOR_TEKSTU_NA_PRZYCISKACH = TLO_3_CIEMNE


class RegisterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("RegisterWidget")
        
        # Zakładamy, że font Inter jest już załadowany globalnie lub jest dostępny
        self.font_family = "Inter" 
        self.font_family_bold = "Inter" # Używane dla tytułu

        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        outer_layout = QVBoxLayout(self)
        outer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer_layout.setContentsMargins(20, 20, 20, 20)

        form_container = QWidget()
        form_container.setObjectName("formContainer")
        form_container.setMaximumWidth(450) # Taka sama szerokość jak panel logowania

        layout = QVBoxLayout(form_container)
        layout.setSpacing(18) 
        layout.setContentsMargins(0,0,0,0)

        # Tytuł "Rejestracja"
        self.title_label = QLabel("Rejestracja")
        self.title_label.setObjectName("titleLabel") # Ten sam objectName dla spójnego stylu
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)
        layout.addSpacerItem(QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Pole Nazwa użytkownika
        self.username_label = QLabel("Nazwa użytkownika")
        self.username_label.setObjectName("formFieldLabel")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nazwa")
        self.username_input.setObjectName("formLineEdit")
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addSpacerItem(QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

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
        layout.addSpacerItem(QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)) # Większy odstęp przed przyciskiem

        # Przycisk "Zaloguj" (wg obrazka, mimo że to formularz rejestracji)
        # Sugerowana nazwa dla funkcjonalności to "Zarejestruj" lub "Utwórz konto"
        # ale trzymamy się prototypu.
        
        # Kontener do centrowania przycisku
        button_container_layout = QHBoxLayout()
        button_container_layout.addStretch() # Dodaje elastyczny odstęp po lewej
        
        self.submit_button = QPushButton("Zaloguj") 
        self.submit_button.setObjectName("accentButton") # Ten sam styl co przycisk logowania
        self.submit_button.setMinimumHeight(45)
        # Można ustawić stałą szerokość, jeśli jest to potrzebne do dokładnego odwzorowania
        self.submit_button.setFixedWidth(180) # Przykładowa szerokość, dostosuj wg potrzeby
        
        button_container_layout.addWidget(self.submit_button)
        button_container_layout.addStretch() # Dodaje elastyczny odstęp po prawej
        layout.addLayout(button_container_layout)

        # Można dodać link "Masz już konto? Zaloguj się" tutaj, jeśli jest potrzebny
        # self.login_link = QLabel("<a href='#' style='color:{ZMNIEJSZONA_SATURACJA_AKCENTU_1};'>Masz już konto? Zaloguj się</a>")
        # self.login_link.setObjectName("navigationLink") # Można zdefiniować nowy styl
        # self.login_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.login_link.setTextFormat(Qt.TextFormat.RichText)
        # layout.addSpacerItem(QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        # layout.addWidget(self.login_link)

        outer_layout.addWidget(form_container)

    def apply_styles(self):
        # Style są bardzo podobne do LoginWidget, więc można je reużyć.
        # Różnica może być w nazwie głównego widgetu RegisterWidget zamiast LoginWidget,
        # ale jeśli formContainer i wewnętrzne elementy mają te same objectName,
        # większość stylów zadziała.
        style_sheet = f"""
            QWidget#RegisterWidget {{
                background-color: {TLO_3_CIEMNE};
            }}
            QWidget#formContainer {{ /* Bez zmian w stosunku do logowania */
                background-color: transparent; 
            }}
            QLabel#titleLabel {{ /* Bez zmian */
                color: {KOLOR_TEKSTU_BIALY};
                font-family: "{self.font_family_bold}", Inter, sans-serif;
                font-size: 56px; 
                font-weight: bold; 
                padding-bottom: 10px;
            }}
            QLabel#formFieldLabel {{ /* Bez zmian */
                color: {KOLOR_TEKSTU_BIALY};
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 15px;
                padding-bottom: 6px; 
            }}
            QLineEdit#formLineEdit {{ /* Bez zmian */
                background-color: {KOLOR_TEKSTU_BIALY};
                color: {KOLOR_TEKSTU_W_POLACH};
                border: none;
                border-radius: 8px; 
                padding: 12px;
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 16px;
                min-height: 22px; 
            }}
            QLineEdit#formLineEdit::placeholder {{ /* Bez zmian */
                color: {KOLOR_PLACEHOLDER};
            }}
            QPushButton#accentButton {{ /* Bez zmian */
                background-color: {KOLOR_AKCENTUJACY_1};
                color: {KOLOR_TEKSTU_NA_PRZYCISKACH};
                border: none;
                border-radius: 8px;
                padding: 10px 15px; 
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 17px;
                font-weight: 600;
                min-height: 28px;
            }}
            QPushButton#accentButton:hover {{ /* Bez zmian */
                background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1};
            }}
            QPushButton#accentButton:pressed {{ /* Bez zmian */
                background-color: {KOLOR_AKCENTUJACY_1}; 
            }}
            /* Opcjonalny styl dla linku "Masz już konto?" */
            /*
            QLabel#navigationLink a {{
                color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1};
                text-decoration: none; /* Można usunąć podkreślenie jeśli wolimy */
                font-family: "{self.font_family}", Inter, sans-serif;
                font-size: 14px;
            }}
            QLabel#navigationLink a:hover {{
                color: {KOLOR_AKCENTUJACY_1}; 
                text-decoration: underline;
            }}
            */
        """
        self.setStyleSheet(style_sheet)

# --- Do testowania widgetu ---
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # --- WAŻNE: Ładowanie fontu Inter (tak jak w LoginWidget) ---
    font_dir = "fonts" 
    regular_loaded = QFontDatabase.addApplicationFont(f"{font_dir}/Inter-Regular.ttf")
    bold_loaded = QFontDatabase.addApplicationFont(f"{font_dir}/Inter-Bold.ttf")
    
    if regular_loaded == -1 or bold_loaded == -1:
        print("Ostrzeżenie: Nie udało się załadować fontów Inter.")
    else:
        print("Fonty Inter załadowane poprawnie.")
    # ------------------------------------

    register_screen = RegisterWidget()
    register_screen.resize(800, 600) 
    register_screen.show()
    sys.exit(app.exec())