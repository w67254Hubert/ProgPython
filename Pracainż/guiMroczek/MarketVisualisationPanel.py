
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
    QTableWidget, QTableWidgetItem, QComboBox, QFrame, QTextEdit,
    QSpacerItem, QSizePolicy, QHeaderView, QAbstractItemView, QApplication,
    QScrollArea, QGridLayout # Nowe widgety
)
from PyQt6.QtGui import QFont, QFontDatabase, QIcon, QPixmap, QColor, QPalette
from PyQt6.QtCore import Qt, QSize

# Import CardWidget i stałych kolorów (tak jak w PortfolioPanel)
# Załóżmy, że CardWidget jest w osobnym pliku np. common_widgets.py
# from common_widgets import CardWidget 

# Jeśli CardWidget jest zdefiniowany w tym samym pliku co PortfolioPanel:
# class CardWidget(QFrame): ... (definicja CardWidget)

# Stałe kolorów (jak wcześniej)
KOLOR_AKCENTUJACY_1 = "#35DFE1"
ZMNIEJSZONA_SATURACJA_AKCENTU_1 = "#4AB4B6"
KOLOR_AKCENTUJACY_2 = "#A02222" # Używany dla Wyloguj
KOLOR_GLOWNY_1 = "#5F7D77"
TLO_2_KARTY = "#485251" 
TLO_3_GLOWNE = "#313636"
KOLOR_TEKSTU_BIALY = "#FFFFFF"
KOLOR_TEKSTU_W_POLACH_CIEMNY = "#202020"
KOLOR_PLACEHOLDER = "#A0A0A0"
KOLOR_TEKSTU_NA_JASNYCH_PRZYCISKACH = TLO_3_GLOWNE # Ciemny tekst na jasnych przyciskach (np. Aktywny Tab)
KOLOR_LINII_TABELI = "#404847"

# Ścieżki do ikon
USER_ICON_PATH = "icons/user_default_icon.png"
LOGOUT_ICON_PATH = "icons/logout_icon.png"
# CHART_PLACEHOLDER_ICON_PATH = "icons/chart_placeholder.png" # Ikona dla placeholderu wykresu

# ---- Reużywalny CardWidget (taki sam jak w PortfolioPanel) ----
class CardWidget(QFrame):
    """Reużywalny widget karty z tytułem i obszarem na treść."""
    def __init__(self, title, parent=None, has_title_bar=True): # Dodano opcję has_title_bar
        super().__init__(parent)
        self.setObjectName("CardWidget")
        self.setFrameShape(QFrame.Shape.StyledPanel)

        card_layout = QVBoxLayout(self)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.setSpacing(0)

        self.title_bar = QWidget()
        self.title_bar.setObjectName("cardTitleBar")
        title_bar_layout = QHBoxLayout(self.title_bar)
        title_bar_layout.setContentsMargins(15, 10, 15, 10)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("cardTitleLabel")
        title_bar_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.header_button_layout = QHBoxLayout()
        title_bar_layout.addLayout(self.header_button_layout)
        
        card_layout.addWidget(self.title_bar)

        self.content_area = QWidget()
        self.content_area.setObjectName("cardContentArea")
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(15, 15, 15, 15)
        self.content_layout.setSpacing(10)
        card_layout.addWidget(self.content_area)

def set_content_layout(self, layout):
    if self.content_area.layout() is not None:
        QWidget().setLayout(self.content_area.layout())
    self.content_area.setLayout(layout)
    self.content_layout = layout
    layout.setContentsMargins(15, 15, 15, 15) 

def add_widget_to_header(self, widget):
    self.header_button_layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignRight)
# ---- Koniec CardWidget ----

# ---- Widget dla wykresu (placeholder) ----
class ChartPlaceholderWidget(QWidget):
    def __init__(self, title="Wykres Ceny kryptowaluty w czasie...", parent=None):
        super().__init__(parent)
        self.setObjectName("ChartPlaceholder")
        self.setMinimumSize(300, 200) # Minimalny rozmiar wykresu
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        # Można dodać QLabel z tytułem wykresu nad obrazkiem/wykresem
        title_label = QLabel(title)
        title_label.setObjectName("chartTitleLabel") # Można ostylować osobno
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout.addWidget(title_label) # Wyłączone, bo tytuł jest w rogu na obrazku

        # Placeholder - w rzeczywistości tu będzie Matplotlib/PyQtGraph widget
        self.placeholder_image_label = QLabel(f"[PLACEHOLDER DLA WYKRESU]\n{title}")
        self.placeholder_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.placeholder_image_label.setStyleSheet(
            f"background-color: {KOLOR_TEKSTU_BIALY}; color: {KOLOR_PLACEHOLDER}; border: 1px dashed {KOLOR_PLACEHOLDER}; font-size: 12px;"
        )
        layout.addWidget(self.placeholder_image_label)
        # chart_pixmap = QPixmap(CHART_PLACEHOLDER_ICON_PATH)
        # if not chart_pixmap.isNull():
        #     self.placeholder_image_label.setPixmap(chart_pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        # else:
        #     self.placeholder_image_label.setText("Wykres...")
# ---- Koniec ChartPlaceholderWidget ----


class MarketVisualisationPanel(QWidget):
    def __init__(self, username="User123123", parent=None):
        super().__init__(parent)
        self.setObjectName("MarketVisualisationPanel")
        self.username = username
        self.font_family = "Inter"

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        # 1. Pasek Nagłówkowy (taki sam jak w PortfolioPanel)
        # Można by go wydzielić do osobnej klasy, jeśli używamy w wielu miejscach
        main_layout.addWidget(self._create_header_bar())

        # 2. Główna zawartość (Lewa kolumna wyboru, Prawa kolumna analizy)
        content_container = QWidget()
        content_container.setObjectName("contentContainerVisualisation")
        self.content_layout = QHBoxLayout(content_container)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(20)

        # Lewa Kolumna (Wybór kryptowaluty i lista)
        self.left_column = QWidget()
        self.left_column_layout = QVBoxLayout(self.left_column)
        self.left_column_layout.setContentsMargins(0,0,0,0)
        self.left_column_layout.setSpacing(15)
        self._populate_left_column()

        # Prawa Kolumna (Statystyki i Wykresy) - będzie scrollowalna
        self.right_column_scroll_area = QScrollArea()
        self.right_column_scroll_area.setObjectName("rightColumnScrollArea")
        self.right_column_scroll_area.setWidgetResizable(True) # Ważne dla QScrollArea
        self.right_column_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) # Ukryj poziomy pasek

        self.right_column_content_widget = QWidget() # Widget, który faktycznie będzie scrollowany
        self.right_column_layout = QVBoxLayout(self.right_column_content_widget)
        self.right_column_layout.setContentsMargins(0,0,0,0) # Marginesy na kartach
        self.right_column_layout.setSpacing(20)
        self._populate_right_column() # Wypełniamy przed ustawieniem widgetu w scroll area
        
        self.right_column_scroll_area.setWidget(self.right_column_content_widget)

        self.content_layout.addWidget(self.left_column, 1)  # Mniejsza szerokość dla lewej kolumny
        self.content_layout.addWidget(self.right_column_scroll_area, 3) # Większa szerokość dla prawej

        main_layout.addWidget(content_container)
        self.apply_styles()

    def _create_header_bar(self): # Taka sama implementacja jak w PortfolioPanel
        header_widget = QWidget()
        header_widget.setObjectName("headerBar") # Ten sam objectName
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(20, 10, 20, 10)
        header_layout.setSpacing(15)

        user_info_widget = QWidget()
        user_info_layout = QHBoxLayout(user_info_widget)
        user_info_layout.setContentsMargins(0,0,0,0); user_info_layout.setSpacing(10)
        user_icon_label = QLabel()
        user_pixmap = QPixmap(USER_ICON_PATH)
        if not user_pixmap.isNull(): user_icon_label.setPixmap(user_pixmap.scaled(QSize(32,32), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else: user_icon_label.setText("👤"); user_icon_label.setFont(QFont(self.font_family, 18))
        username_label = QLabel(self.username)
        username_label.setObjectName("usernameLabel") # Ten sam objectName
        self.logout_button = QPushButton("Wyloguj")
        self.logout_button.setObjectName("logoutButton") # Ten sam objectName
        logout_icon = QIcon(LOGOUT_ICON_PATH)
        if not logout_icon.isNull(): self.logout_button.setIcon(logout_icon); self.logout_button.setIconSize(QSize(16,16))
        user_info_layout.addWidget(user_icon_label); user_info_layout.addWidget(username_label); user_info_layout.addWidget(self.logout_button)
        header_layout.addWidget(user_info_widget)
        header_layout.addStretch(1)

        self.portfolio_tab_button = QPushButton("Portfel Kryptowalut")
        self.portfolio_tab_button.setObjectName("navTabButton") # Ten sam objectName
        self.portfolio_tab_button.setProperty("active", False)
        self.market_view_tab_button = QPushButton("Wizualizacje Rynkowe")
        self.market_view_tab_button.setObjectName("navTabButton")
        self.market_view_tab_button.setProperty("active", True) # Aktywny ten tab

        header_layout.addWidget(self.portfolio_tab_button)
        header_layout.addWidget(self.market_view_tab_button)
        return header_widget

    def _create_input_field(self, label_text, placeholder_text, is_combobox=False, combo_items=None):
        widget = QWidget()
        layout = QVBoxLayout(widget); layout.setContentsMargins(0,0,0,0); layout.setSpacing(5)
        label = QLabel(label_text); label.setObjectName("formFieldLabelSmall")
        layout.addWidget(label)
        if is_combobox:
            input_field = QComboBox(); input_field.setObjectName("formComboBoxWhite") # Inny objectName dla ewentualnych różnic
            if combo_items: input_field.addItems(combo_items)
            input_field.setPlaceholderText(placeholder_text) 
            if not combo_items and placeholder_text: input_field.addItem(placeholder_text) # Hack
            input_field.setEditable(True) # Pozwalamy wpisywać
        else:
            input_field = QLineEdit(); input_field.setObjectName("formLineEditWhite")
            input_field.setPlaceholderText(placeholder_text)
        input_field.setFixedHeight(38)
        layout.addWidget(input_field)
        return widget, input_field

    def _populate_left_column(self):
        # 1. Karta "Wybierz kryptowalutę do analizy"
        # Użyjemy CardWidget bez paska tytułowego, aby pasowało do obrazka
        select_crypto_card = CardWidget("Wybierz kryptowalutę do analizy", has_title_bar=False)
        select_crypto_card.setObjectName("selectCryptoCardLeft") # Dla specyficznego stylu
        
        main_label = QLabel("Wybierz kryptowalutę do analizy")
        main_label.setObjectName("selectCryptoMainLabel")
        select_crypto_card.content_layout.addWidget(main_label)

        input_container = QWidget()
        input_layout = QHBoxLayout(input_container)
        input_layout.setContentsMargins(0,5,0,0) # Odstęp od etykiety
        input_layout.setSpacing(10)

        # Używamy _create_input_field bez zewnętrznej etykiety, bo mamy main_label
        # Nazwa pola z etykietą "wprowadź nazwę kryptowaluty"
        field_widget, self.crypto_select_combo = self._create_input_field(
            "wprowadź nazwę kryptowaluty", "Nazwa Kryptowaluty",
            is_combobox=True, 
            combo_items=["Bitcoin", "Ethereum", "Dogecoin", "Cardano", "Solana"] # Przykładowe dane
        )
        input_layout.addWidget(field_widget, 3) # Większa szerokość dla pola

        self.generate_button = QPushButton("Generuj")
        self.generate_button.setObjectName("accentButton1") # Zielony przycisk
        self.generate_button.setFixedHeight(38)
        self.generate_button.setFixedWidth(100)
        input_layout.addWidget(self.generate_button, 1, Qt.AlignmentFlag.AlignBottom)
        
        select_crypto_card.content_layout.addWidget(input_container)
        self.left_column_layout.addWidget(select_crypto_card)

        # 2. Tabela "Lista kryptowalut" (również jako karta bez tytułu)
        crypto_list_card = CardWidget("Lista kryptowalut", has_title_bar=False)
        crypto_list_card.setObjectName("cryptoListCardLeft")
        
        self.available_crypto_table = QTableWidget()
        self.available_crypto_table.setObjectName("dataTableSmall") # Inny objectName dla ewentualnie innego stylu
        self.available_crypto_table.setColumnCount(2)
        self.available_crypto_table.setHorizontalHeaderLabels(["Kryptowaluta", "cena $"])
        self.available_crypto_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch) # Nazwa rozciągnięta
        self.available_crypto_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents) # Cena do zawartości
        self.available_crypto_table.verticalHeader().setVisible(False)
        self.available_crypto_table.setAlternatingRowColors(True)
        self.available_crypto_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.available_crypto_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.available_crypto_table.setShowGrid(True) # Pokaż linie siatki
        
        # Przykładowe dane
        sample_data = [("BTC", "2,41"), ("Etereum", "300,99b"), ("DogeCoin", "34,00 b")]
        self.available_crypto_table.setRowCount(len(sample_data))
        for i, (name, price) in enumerate(sample_data):
            self.available_crypto_table.setItem(i, 0, QTableWidgetItem(name))
            self.available_crypto_table.setItem(i, 1, QTableWidgetItem(price))

        self.available_crypto_table.setMinimumHeight(200) # Wysokość tabeli
        self.available_crypto_table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        crypto_list_card.content_layout.addWidget(self.available_crypto_table)
        self.left_column_layout.addWidget(crypto_list_card, 1) # Nadajemy większą rozciągliwość tabeli
        self.left_column_layout.addStretch(0)


    def _create_stats_row(self, label_text, value_text):
        row_widget = QWidget()
        row_widget.setObjectName("statsRowWidget")
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0,0,0,0) # Marginesy będą na kontenerze

        label = QLabel(label_text)
        label.setObjectName("statsLabel")
        value = QLabel(value_text)
        value.setObjectName("statsValue")
        value.setAlignment(Qt.AlignmentFlag.AlignRight)

        row_layout.addWidget(label)
        row_layout.addWidget(value)
        return row_widget

    def _populate_right_column(self):
        # 1. Karta "Statystyki Rynku kryptowaluty:"
        stats_card = CardWidget("Statystyki Rynku kryptowaluty:")
        stats_card.setObjectName("statsCardRight")
        
        # "Kluczowe Statystyki | Wartość USD" - jako nagłówek wewnątrz karty
        header_stats = QWidget(); header_stats.setObjectName("statsInternalHeader")
        header_stats_layout = QHBoxLayout(header_stats)
        header_stats_layout.addWidget(QLabel("Kluczowe Statystyki"))
        lbl_wartosc_usd = QLabel("Wartość USD"); lbl_wartosc_usd.setAlignment(Qt.AlignmentFlag.AlignRight)
        header_stats_layout.addWidget(lbl_wartosc_usd)
        stats_card.content_layout.addWidget(header_stats)

        stats_card.content_layout.addWidget(self._create_stats_row("Kapitalizacja rynkowa:", "8.74B"))
        stats_card.content_layout.addWidget(self._create_stats_row("Wolumeny ostatnie 24h:", "300tys."))
        
        stats_card.content_layout.addSpacerItem(QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)) # Odstęp

        # "% zmiany cen w odniesieniu do ceny w czasie"
        change_header_label = QLabel("% zmiany cen w odniesieniu do ceny w czasie")
        change_header_label.setObjectName("changeHeaderLabel")
        stats_card.content_layout.addWidget(change_header_label)

        changes_container = QWidget(); changes_container.setObjectName("changesContainer")
        changes_layout = QHBoxLayout(changes_container)
        changes_layout.setSpacing(10)
        
        change_data = [("Zmiana ceny 24h", "+5.01%", KOLOR_AKCENTUJACY_1), 
                       ("zmiana 7 dni", "+10.10%", KOLOR_AKCENTUJACY_1), 
                       ("zmiana 1 miesiąc", "-10.00%", KOLOR_AKCENTUJACY_2)] # Użyjemy Akcentu2 dla negatywnej zmiany
        
        for label_txt, val_txt, color_val in change_data:
            change_box = QWidget(); change_box.setObjectName("changeBox")
            # Styl dla changeBox, aby miał tło i ramkę jak na obrazku
            change_box.setStyleSheet(f"background-color: transparent; border: 1px solid {KOLOR_GLOWNY_1}; border-radius: 4px; padding: 8px;")
            change_box_layout = QVBoxLayout(change_box)
            change_box_layout.setContentsMargins(0,0,0,0)
            change_box_layout.setSpacing(2)
            
            lbl = QLabel(label_txt); lbl.setObjectName("changeBoxLabel"); lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            val = QLabel(val_txt); val.setObjectName("changeBoxValue"); val.setAlignment(Qt.AlignmentFlag.AlignCenter)
            val.setStyleSheet(f"color: {'#4CAF50' if '-' not in val_txt else '#F44336'};") # Zielony dla plus, czerwony dla minus (zastąp swoimi kolorami akcentów)
            
            change_box_layout.addWidget(lbl)
            change_box_layout.addWidget(val)
            changes_layout.addWidget(change_box)
        stats_card.content_layout.addWidget(changes_container)

        self.right_column_layout.addWidget(stats_card)

        # 2. Sekcja Wykresów (użyjemy QGridLayout dla elastyczności)
        charts_section_title = QLabel("Wizualizacje z predykcjami")
        charts_section_title.setObjectName("chartsSectionTitle") # Styl dla tego tytułu
        self.right_column_layout.addWidget(charts_section_title)

        charts_grid_widget = QWidget()
        charts_grid_layout = QGridLayout(charts_grid_widget)
        charts_grid_layout.setSpacing(15)

        # Dodajemy 3 placeholdery wykresów
        chart1 = ChartPlaceholderWidget("Wykres Ceny kryptowaluty w czasie z predykcją jej wartości agl test")
        chart2 = ChartPlaceholderWidget("Wykres Ceny kryptowaluty w czasie z predykcją jej wartości agl test2")
        chart3 = ChartPlaceholderWidget("Wykres Ceny kryptowaluty w czasie z predykcją jej wartości agl test2") # Na obrazku są 3 podobne
        
        charts_grid_layout.addWidget(chart1, 0, 0) # Rząd 0, Kolumna 0
        charts_grid_layout.addWidget(chart2, 1, 0) # Rząd 1, Kolumna 0
        charts_grid_layout.addWidget(chart3, 1, 1) # Rząd 1, Kolumna 1 (jeśli chcemy 2 w jednym rzędzie)
        # Zgodnie z obrazkiem, jeden wykres jest szerszy, a dwa mniejsze pod nim.
        # Aby to osiągnąć, można użyć addWidget(widget, row, col, rowSpan, colSpan)
        # Jednak obrazek pokazuje 1 główny i 2 mniejsze poniżej, każdy zajmujący całą szerokość prawej kolumny.
        # W takim przypadku QVBoxLayout byłby prostszy. Przyjmijmy jednak na razie układ z obrazka, gdzie
        # główny wykres jest nad dwoma mniejszymi, które są obok siebie.
        # Jeśli główny wykres ma być sam na górze, a dwa poniżej obok siebie:
        # self.right_column_layout.addWidget(chart1)
        # lower_charts_container = QWidget()
        # lower_charts_layout = QHBoxLayout(lower_charts_container)
        # lower_charts_layout.addWidget(chart2)
        # lower_charts_layout.addWidget(chart3)
        # self.right_column_layout.addWidget(lower_charts_container)
        
        # Aktualny układ z obrazka (jeden duży na górze, potem rząd z dwoma mniejszymi) - to błędna interpretacja
        # Obrazek pokazuje jeden duży, pod nim drugi, pod nim trzeci. Więc zwykły QVBoxLayout dla wykresów.
        
        self.right_column_layout.addWidget(chart1)
        self.right_column_layout.addWidget(chart2)
        self.right_column_layout.addWidget(chart3)

        self.right_column_layout.addStretch(1) # Aby elementy grupowały się u góry, jeśli jest mało treści

    def apply_styles(self):
        # QSS będzie podobny do PortfolioPanel, ale z dodatkami dla nowych elementów
        stylesheet = f"""
            /* --- Ogólne --- */
            QWidget#MarketVisualisationPanel {{ background-color: {TLO_3_GLOWNE}; font-family: "{self.font_family}", Inter, sans-serif; }}
            QWidget#contentContainerVisualisation {{ background-color: transparent; }}
            
            /* --- Pasek Nagłówkowy (style jak w PortfolioPanel, jeśli są te same objectName) --- */
            QWidget#headerBar {{ background-color: {TLO_3_GLOWNE}; border-bottom: 1px solid {KOLOR_GLOWNY_1}; }}
            QLabel#usernameLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 28px; font-weight: 600; }}
            QPushButton#logoutButton {{ background-color: transparent; color: {KOLOR_AKCENTUJACY_2}; font-size: 14px; font-weight: bold; padding: 5px 10px; border: 1px solid {KOLOR_AKCENTUJACY_2}; border-radius: 5px; min-width: 90px; }}
            QPushButton#logoutButton:hover {{ background-color: {KOLOR_AKCENTUJACY_2}; color: {KOLOR_TEKSTU_BIALY}; }}
            QPushButton#navTabButton {{ background-color: {KOLOR_GLOWNY_1}; color: {KOLOR_TEKSTU_BIALY}; font-size: 15px; font-weight: 500; padding: 10px 20px; border: none; border-radius: 5px; min-height: 30px; }}
            QPushButton#navTabButton:hover {{ background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1}; }}
            QPushButton#navTabButton[active="true"] {{ background-color: {KOLOR_AKCENTUJACY_1}; color: {KOLOR_TEKSTU_NA_JASNYCH_PRZYCISKACH}; }}

            /* --- Lewa Kolumna --- */
            QFrame#selectCryptoCardLeft, QFrame#cryptoListCardLeft {{
                background-color: {TLO_2_KARTY};
                border-radius: 8px;
            }}
            QLabel#selectCryptoMainLabel {{
                color: {KOLOR_TEKSTU_BIALY};
                font-size: 16px;
                font-weight: 600;
                padding-bottom: 5px; /* Mały odstęp od pola input */
            }}
            QLabel#formFieldLabelSmall {{ /* Dla etykiety "wprowadź nazwę kryptowaluty" */
                color: {KOLOR_TEKSTU_BIALY};
                font-size: 13px; 
            }}
            QLineEdit#formLineEditWhite, QComboBox#formComboBoxWhite {{
                background-color: {KOLOR_TEKSTU_BIALY}; color: {KOLOR_TEKSTU_W_POLACH_CIEMNY};
                border: 1px solid #B0B0B0; border-radius: 5px; padding: 8px; font-size: 14px;
            }}
            QComboBox#formComboBoxWhite::drop-down {{ border: none; subcontrol-origin: padding; subcontrol-position: top right; width: 20px; }}
            QComboBox#formComboBoxWhite::down-arrow {{ image: url(icons/dropdown_arrow_dark.png); width: 12px; height: 12px; }}
            QComboBox QAbstractItemView {{ /* Lista rozwijana */
                background-color: {KOLOR_TEKSTU_BIALY}; color: {KOLOR_TEKSTU_W_POLACH_CIEMNY};
                selection-background-color: {KOLOR_AKCENTUJACY_1}; selection-color: {KOLOR_TEKSTU_W_POLACH_CIEMNY};
                border: 1px solid {KOLOR_GLOWNY_1}; border-radius: 4px; 
            }}

            QPushButton#accentButton1 {{ /* Przycisk "Generuj" */
                background-color: {KOLOR_AKCENTUJACY_1}; color: {TLO_3_GLOWNE};
                border: none; border-radius: 5px; font-size: 15px; font-weight: 600; padding: 8px 15px;
            }}
            QPushButton#accentButton1:hover {{ background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1}; }}
            
            QTableWidget#dataTableSmall {{ /* Tabela dostępnych krypto */
                background-color: {TLO_2_KARTY}; color: {KOLOR_TEKSTU_BIALY};
                gridline-color: {KOLOR_LINII_TABELI}; border: none; font-size: 13px;
            }}
            QHeaderView::section {{ /* Nagłówki tabeli (wspólne) */
                background-color: {KOLOR_GLOWNY_1}; color: {KOLOR_TEKSTU_BIALY};
                padding: 6px; border: none; font-size: 13px; font-weight: 600;
            }}
            QTableWidget#dataTableSmall::item {{ padding: 6px; border-bottom: 1px solid {KOLOR_LINII_TABELI}; }}
            QTableWidget#dataTableSmall::item:selected {{ background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1}; color: {TLO_3_GLOWNE}; }}
            QTableWidget#dataTableSmall::item:alternate {{ background-color: #404847; }}
            QTableWidget#dataTableSmall QScrollBar:vertical {{ border: none; background: {TLO_2_KARTY}; width: 8px; margin: 0px; }}
            QTableWidget#dataTableSmall QScrollBar::handle:vertical {{ background: {KOLOR_GLOWNY_1}; min-height: 20px; border-radius: 4px; }}
            QTableWidget#dataTableSmall QScrollBar::add-line:vertical, QTableWidget#dataTableSmall QScrollBar::sub-line:vertical {{ height: 0px; }}


            /* --- Prawa Kolumna --- */
            QScrollArea#rightColumnScrollArea {{ border: none; background-color: transparent; }}
            QWidget#rightColumnScrollArea > QWidget > QWidget {{ background-color: transparent; }} /* Dla content widget w QScrollArea */
            
            QFrame#statsCardRight {{
                background-color: {TLO_2_KARTY};
                border-radius: 8px;
            }}
            QWidget#statsCardRight QLabel#cardTitleLabel {{ /* Tytuł karty Statystyk */
                 color: {KOLOR_TEKSTU_BIALY}; font-size: 18px; font-weight: 600;
            }}
            QWidget#statsInternalHeader {{ 
                background-color: {KOLOR_GLOWNY_1}; border-radius: 4px; 
                padding: 8px 10px; margin-bottom: 8px;
            }}
            QWidget#statsInternalHeader QLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 14px; font-weight: 500; }}

            QWidget#statsRowWidget {{ padding: 4px 0px; border-bottom: 1px solid {KOLOR_LINII_TABELI}; }}
            QWidget#statsRowWidget:last-child {{ border-bottom: none; }} /* Usuń ostatnią linię */
            QLabel#statsLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 14px; }}
            QLabel#statsValue {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 14px; font-weight: 600; }}

            QLabel#changeHeaderLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 15px; font-weight: 500; margin-top: 10px; padding-bottom: 5px;}}
            QWidget#changesContainer {{ margin-top: 5px; }}
            QLabel#changeBoxLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 12px; opacity: 0.8; }}
            /* QLabel#changeBoxValue - stylizowany inline w kodzie python, można przenieść tu */

            QLabel#chartsSectionTitle {{
                color: {KOLOR_TEKSTU_BIALY}; font-size: 18px; font-weight: 600;
                padding-top: 15px; padding-bottom: 10px;
                border-top: 1px solid {KOLOR_GLOWNY_1}; /* Linia nad tytułem wykresów */
                margin-top: 15px; /* Odstęp od karty statystyk */
            }}
            QWidget#ChartPlaceholder {{ /* Ogólny styl dla kontenera wykresu */
                background-color: {TLO_2_KARTY}; /* Tło za wykresem, jeśli wykres nie wypełnia */
                border-radius: 6px;
                padding: 5px; /* Mały padding wokół placeholderu */
            }}
        """
        self.setStyleSheet(stylesheet)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    # Globalne ładowanie fontów
    regular_loaded = QFontDatabase.addApplicationFont("fonts/Inter-Regular.ttf")
    bold_loaded = QFontDatabase.addApplicationFont("fonts/Inter-Bold.ttf")
    if regular_loaded == -1 or bold_loaded == -1: print("Warning: Could not load Inter fonts.")
    else: print("Inter fonts loaded.")

    market_view = MarketVisualisationPanel(username="KryptoAnalityk")
    market_view.resize(1366, 768) # Rozdzielczość
    market_view.show()
    sys.exit(app.exec())