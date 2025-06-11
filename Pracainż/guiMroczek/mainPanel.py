import sys
import os
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
    QTableWidget, QTableWidgetItem, QComboBox, QFrame, QTextEdit,
    QSpacerItem, QSizePolicy, QHeaderView, QAbstractItemView, QApplication, QMainWindow, QStackedWidget
)
from PyQt6.QtGui import QFont, QFontDatabase, QIcon, QPixmap, QColor, QPalette
from PyQt6.QtCore import Qt, QSize

# Stałe kolorów
KOLOR_AKCENTUJACY_1 = "#35DFE1"
ZMNIEJSZONA_SATURACJA_AKCENTU_1 = "#4AB4B6"
KOLOR_AKCENTUJACY_2 = "#A02222"
KOLOR_GLOWNY_1 = "#5F7D77"
TLO_2_KARTY = "#485251"
TLO_3_GLOWNE = "#313636"
KOLOR_TEKSTU_BIALY = "#FFFFFF"
KOLOR_TEKSTU_W_POLACH_CIEMNY = "#202020"
KOLOR_PLACEHOLDER = "#A0A0A0"
KOLOR_TEKSTU_NA_JASNYCH_PRZYCISKACH = TLO_3_GLOWNE
KOLOR_LINII_TABELI = "#404847"

# Ścieżki do ikon
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_ICON_PATH = os.path.join(BASE_DIR, "icons/user_default_icon.png")
LOGOUT_ICON_PATH = os.path.join(BASE_DIR, "icons/logout_icon.png")
# USUNIĘTO: DROPDOWN_ICON_PATH


class CardWidget(QFrame):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setObjectName("CardWidget")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        card_layout = QVBoxLayout(self)
        card_layout.setContentsMargins(0, 0, 0, 0); card_layout.setSpacing(0)
        self.title_bar = QWidget(); self.title_bar.setObjectName("cardTitleBar")
        title_bar_layout = QHBoxLayout(self.title_bar)
        title_bar_layout.setContentsMargins(15, 10, 15, 10)
        self.title_label = QLabel(title); self.title_label.setObjectName("cardTitleLabel")
        title_bar_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignLeft)
        self.header_button_layout = QHBoxLayout()
        title_bar_layout.addLayout(self.header_button_layout)
        card_layout.addWidget(self.title_bar)
        self.content_area = QWidget(); self.content_area.setObjectName("cardContentArea")
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(15, 15, 15, 15); self.content_layout.setSpacing(10)
        card_layout.addWidget(self.content_area)
    def set_content_layout(self, layout):
        if self.content_area.layout() is not None: QWidget().setLayout(self.content_area.layout())
        self.content_area.setLayout(layout); self.content_layout = layout
        layout.setContentsMargins(15, 15, 15, 15) 
    def add_widget_to_header(self, widget): self.header_button_layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignRight)

class PortfolioPanel(QWidget):
    def __init__(self, username="User123123", parent=None):
        super().__init__(parent)
        self.setObjectName("PortfolioPanel"); self.username = username
        main_layout = QVBoxLayout(self); main_layout.setContentsMargins(0,0,0,0); main_layout.setSpacing(0)
        main_layout.addWidget(self._create_header_bar())
        content_container = QWidget(); content_container.setObjectName("contentContainer")
        self.content_layout = QHBoxLayout(content_container)
        self.content_layout.setContentsMargins(20, 20, 20, 20); self.content_layout.setSpacing(20)
        self.left_column = QWidget(); self.left_column_layout = QVBoxLayout(self.left_column)
        self.left_column_layout.setContentsMargins(0,0,0,0); self.left_column_layout.setSpacing(20)
        self.right_column = QWidget(); self.right_column_layout = QVBoxLayout(self.right_column)
        self.right_column_layout.setContentsMargins(0,0,0,0); self.right_column_layout.setSpacing(20)
        self._populate_left_column(); self._populate_right_column()
        self.content_layout.addWidget(self.left_column, 1); self.content_layout.addWidget(self.right_column, 1)
        main_layout.addWidget(content_container)
    def _create_header_bar(self):
        header_widget = QWidget(); header_widget.setObjectName("headerBar")
        header_layout = QHBoxLayout(header_widget); header_layout.setContentsMargins(20, 10, 20, 10); header_layout.setSpacing(15)
        user_info_widget = QWidget(); user_info_layout = QHBoxLayout(user_info_widget)
        user_info_layout.setContentsMargins(0,0,0,0); user_info_layout.setSpacing(10)
        user_icon_label = QLabel()
        user_pixmap = QPixmap(USER_ICON_PATH)
        if not user_pixmap.isNull(): user_icon_label.setPixmap(user_pixmap.scaled(QSize(32,32), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else: user_icon_label.setText("👤")
        user_info_layout.addWidget(user_icon_label)
        username_label = QLabel(self.username); username_label.setObjectName("usernameLabel")
        user_info_layout.addWidget(username_label)
        self.logout_button = QPushButton("Wyloguj"); self.logout_button.setObjectName("logoutButton")
        logout_icon = QIcon(LOGOUT_ICON_PATH)
        if not logout_icon.isNull(): self.logout_button.setIcon(logout_icon); self.logout_button.setIconSize(QSize(16,16))
        user_info_layout.addWidget(self.logout_button); header_layout.addWidget(user_info_widget); header_layout.addStretch(1)
        self.portfolio_tab_button = QPushButton("Portfel Kryptowalut"); self.portfolio_tab_button.setObjectName("navTabButton"); self.portfolio_tab_button.setProperty("active", True)
        self.market_view_tab_button = QPushButton("Wizualizacje Rynkowe"); self.market_view_tab_button.setObjectName("navTabButton"); self.market_view_tab_button.setProperty("active", False)
        header_layout.addWidget(self.portfolio_tab_button); header_layout.addWidget(self.market_view_tab_button)
        return header_widget
    def _create_input_field(self, label_text, placeholder_text, is_password=False, is_combobox=False, combo_items=None):
        widget = QWidget(); layout = QVBoxLayout(widget); layout.setContentsMargins(0,0,0,0); layout.setSpacing(5)
        label = QLabel(label_text); label.setObjectName("formFieldLabelSmall"); layout.addWidget(label)
        if is_combobox:
            input_field = QComboBox(); input_field.setObjectName("formComboBox")
            if combo_items: input_field.addItems(combo_items)
            if not combo_items and placeholder_text: input_field.addItem(placeholder_text); input_field.setCurrentIndex(0)
            elif combo_items and placeholder_text: input_field.insertItem(0, placeholder_text); input_field.setCurrentIndex(0)
        else:
            input_field = QLineEdit(); input_field.setObjectName("formLineEditWhite"); input_field.setPlaceholderText(placeholder_text)
            if is_password: input_field.setEchoMode(QLineEdit.EchoMode.Password)
        input_field.setFixedHeight(38); layout.addWidget(input_field)
        return widget, input_field
    def _populate_left_column(self):
        add_asset_card = CardWidget("Dodanie aktywów"); add_asset_content_layout = QHBoxLayout(); add_asset_content_layout.setSpacing(10)
        name_widget, self.add_asset_name_combo = self._create_input_field("Nazwa kryptowaluty", "Wybierz lub wpisz...", is_combobox=True, combo_items=["Bitcoin (BTC)", "Ethereum (ETH)", "Cardano (ADA)"])
        self.add_asset_name_combo.setEditable(True)
        qty_widget, self.add_asset_qty_input = self._create_input_field("Ilość aktywów", "Liczba")
        self.add_asset_button = QPushButton("Dodaj"); self.add_asset_button.setObjectName("accentButton1"); self.add_asset_button.setFixedHeight(38); self.add_asset_button.setFixedWidth(100)
        add_asset_content_layout.addWidget(name_widget, 2); add_asset_content_layout.addWidget(qty_widget, 1); add_asset_content_layout.addWidget(self.add_asset_button, 0, Qt.AlignmentFlag.AlignBottom)
        add_asset_card.set_content_layout(add_asset_content_layout); self.left_column_layout.addWidget(add_asset_card)
        portfolio_table_card = CardWidget("Aktywa w portfelu"); self.portfolio_table = QTableWidget(); self.portfolio_table.setObjectName("dataTable"); self.portfolio_table.setColumnCount(4)
        self.portfolio_table.setHorizontalHeaderLabels(["Kryptowaluta", "Ilość Aktywów", "Cena", "Wartość"]); self.portfolio_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.portfolio_table.verticalHeader().setVisible(False); self.portfolio_table.setAlternatingRowColors(True); self.portfolio_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.portfolio_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows); self.portfolio_table.setShowGrid(True); self.portfolio_table.setRowCount(10)
        self.portfolio_table.setItem(0,0, QTableWidgetItem("Bitcoin (BTC)")); self.portfolio_table.setItem(0,1, QTableWidgetItem("2.0")); self.portfolio_table.setItem(0,2, QTableWidgetItem("123.22 PLN")); self.portfolio_table.setItem(0,3, QTableWidgetItem("246.44 PLN"))
        self.portfolio_table.setMinimumHeight(300); self.portfolio_table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        portfolio_table_card.content_layout.addWidget(self.portfolio_table); self.left_column_layout.addWidget(portfolio_table_card, 1); self.left_column_layout.addStretch(0)
    def _populate_right_column(self):
        sell_asset_card = CardWidget("Sprzedaż aktywów"); sell_asset_content_layout = QHBoxLayout(); sell_asset_content_layout.setSpacing(10)
        name_widget_sell, self.sell_asset_name_combo = self._create_input_field("Nazwa kryptowaluty", "Wybierz z portfela...", is_combobox=True, combo_items=[])
        self.sell_asset_name_combo.setEditable(False)
        qty_widget_sell, self.sell_asset_qty_input = self._create_input_field("Ilość aktywów", "Liczba")
        self.sell_asset_button = QPushButton("Sprzedaj"); self.sell_asset_button.setObjectName("accentButton2"); self.sell_asset_button.setFixedHeight(38); self.sell_asset_button.setFixedWidth(100)
        sell_asset_content_layout.addWidget(name_widget_sell, 2); sell_asset_content_layout.addWidget(qty_widget_sell, 1); sell_asset_content_layout.addWidget(self.sell_asset_button, 0, Qt.AlignmentFlag.AlignBottom)
        sell_asset_card.set_content_layout(sell_asset_content_layout); self.right_column_layout.addWidget(sell_asset_card)
        sold_table_card = CardWidget("Lista ostatnio sprzedanych aktywów"); self.sold_table = QTableWidget(); self.sold_table.setObjectName("dataTable"); self.sold_table.setColumnCount(4); self.sold_table.setHorizontalHeaderLabels(["Kryptowaluta", "Ilość Aktywów", "Cena zakupu", "Cena sprzedaży"])
        self.sold_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch); self.sold_table.verticalHeader().setVisible(False); self.sold_table.setAlternatingRowColors(True)
        self.sold_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers); self.sold_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows); self.sold_table.setShowGrid(True); self.sold_table.setRowCount(5)
        self.sold_table.setItem(0,0, QTableWidgetItem("Ethereum (ETH)")); self.sold_table.setItem(0,1, QTableWidgetItem("1.0")); self.sold_table.setItem(0,2, QTableWidgetItem("111.00 PLN")); self.sold_table.setItem(0,3, QTableWidgetItem("120.00 PLN"))
        self.sold_table.setFixedHeight(180); sold_table_card.content_layout.addWidget(self.sold_table); self.right_column_layout.addWidget(sold_table_card)
        prediction_card = CardWidget("Predykcja wartości portfela"); self.update_prediction_button = QPushButton("Aktualizuj Prognozy"); self.update_prediction_button.setObjectName("accentButton1Small")
        self.update_prediction_button.setFixedHeight(30); prediction_card.add_widget_to_header(self.update_prediction_button)
        prediction_results_area = QWidget(); prediction_results_area.setObjectName("predictionResultsArea"); prediction_results_layout = QHBoxLayout(prediction_results_area)
        prediction_results_layout.setContentsMargins(10,10,10,10); prediction_results_layout.setSpacing(10)
        prediction_values = [("Aktualna wartość", "100.00"), ("za 7 dni", "98.80"), ("za 14 dni", "105.02"), ("za 30 dni", "120.00")]
        for label_text, value_text in prediction_values:
            value_box = QWidget(); value_box_layout = QVBoxLayout(value_box); value_box_layout.setContentsMargins(0,0,0,0); value_box_layout.setSpacing(3)
            val_label = QLabel(label_text); val_label.setObjectName("predictionLabel"); val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            val_data = QLabel(value_text); val_data.setObjectName("predictionData"); val_data.setAlignment(Qt.AlignmentFlag.AlignCenter)
            value_box_layout.addWidget(val_label); value_box_layout.addWidget(val_data); prediction_results_layout.addWidget(value_box)
        prediction_card.content_layout.addWidget(prediction_results_area); self.right_column_layout.addWidget(prediction_card)
        optimization_card = CardWidget("Optymalizacja portfela"); self.optimize_button = QPushButton("Optymalizuj"); self.optimize_button.setObjectName("accentButton1Small")
        self.optimize_button.setFixedHeight(30); optimization_card.add_widget_to_header(self.optimize_button)
        self.optimization_results_text = QTextEdit(); self.optimization_results_text.setObjectName("optimizationResultsText"); self.optimization_results_text.setReadOnly(True); self.optimization_results_text.setPlaceholderText("Oczekiwanie na wynik optymalizacji...")
        self.optimization_results_text.setMinimumHeight(100); optimization_card.content_layout.addWidget(self.optimization_results_text); self.right_column_layout.addWidget(optimization_card); self.right_column_layout.addStretch(1)
    def get_main_stylesheet(self): return f"""QWidget#PortfolioPanel {{ background-color: transparent; }} QWidget#contentContainer {{ background-color: transparent; }}"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analizator Portfela Kryptowalut"); self.setGeometry(100, 100, 1280, 800)
        self.font_family_name = self.load_fonts()
        self.main_widget = QWidget(); self.setCentralWidget(self.main_widget)
        self.apply_global_stylesheet() 
        self.portfolio_panel = PortfolioPanel(username="TesterAplikacji")
        main_layout = QVBoxLayout(self.main_widget); main_layout.setContentsMargins(0,0,0,0)
        main_layout.addWidget(self.portfolio_panel)
    def load_fonts(self):
        font_family_name_to_use = "Arial"
        font_definitions = {"Regular": "fonts/Inter-Regular.ttf", "SemiBold": "fonts/Inter-SemiBold.ttf", "Bold": "fonts/Inter-Bold.ttf"}
        loaded_font_families_set = set()
        for weight_name, relative_path in font_definitions.items():
            font_path = os.path.join(BASE_DIR, relative_path)
            if not os.path.exists(font_path): print(f"OSTRZEŻENIE: Plik fontu nie istnieje: '{font_path}'"); continue
            font_id = QFontDatabase.addApplicationFont(font_path) 
            if font_id == -1: print(f"OSTRZEŻENIE: Nie udało się załadować fontu Inter {weight_name} z '{font_path}'.")
            else:
                families = QFontDatabase.applicationFontFamilies(font_id) 
                if families: print(f"Font Inter {weight_name} (rodzina: {families[0]}) załadowany poprawnie z '{font_path}'."); loaded_font_families_set.add(families[0])
                else: print(f"INFO: Font załadowany z '{font_path}', ale nie udało się odczytać rodziny fontu.")
        if "Inter" in loaded_font_families_set: font_family_name_to_use = "Inter"; print(f"INFO: Będzie używana rodzina fontu: '{font_family_name_to_use}'")
        elif loaded_font_families_set: font_family_name_to_use = list(loaded_font_families_set)[0]; print(f"INFO: Rodzina 'Inter' nie została załadowana. Używam pierwszej dostępnej: '{font_family_name_to_use}'")
        else: print(f"OSTRZEŻENIE: Żaden font Inter nie został załadowany. Aplikacja użyje fontu systemowego '{font_family_name_to_use}'.")
        if font_family_name_to_use == "Inter": # Poprawka: powinno być `if loaded_font_families_set and font_family_name_to_use != "Arial":` lub podobnie, aby ustawić font tylko jeśli faktycznie Inter (lub jego wariant) został załadowany
            default_app_font = QFont(font_family_name_to_use, 10) # Używamy faktycznie załadowanej nazwy
            app_instance = QApplication.instance()
            if app_instance: app_instance.setFont(default_app_font); print(f"Domyślny font aplikacji ustawiony na '{font_family_name_to_use}'.")
            else: print("OSTRZEŻENIE: QApplication.instance() jest None. Nie można ustawić domyślnego fontu.")
        return font_family_name_to_use
    def apply_global_stylesheet(self):
        font_to_use_in_css = self.font_family_name 
        stylesheet = f"""
            QMainWindow {{ background-color: {TLO_3_GLOWNE}; }}
            QWidget {{ font-family: "{font_to_use_in_css}", Arial, sans-serif; }}
            QWidget#headerBar {{ background-color: {TLO_3_GLOWNE}; border-bottom: 1px solid {KOLOR_GLOWNY_1}; }}
            QLabel#usernameLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 28px; font-weight: 600; }}
            QPushButton#logoutButton {{ background-color: transparent; color: {KOLOR_AKCENTUJACY_2}; font-size: 14px; font-weight: bold; padding: 5px 10px; border: 1px solid {KOLOR_AKCENTUJACY_2}; border-radius: 5px; min-width: 90px; }}
            QPushButton#logoutButton:hover {{ background-color: {KOLOR_AKCENTUJACY_2}; color: {KOLOR_TEKSTU_BIALY}; }}
            QPushButton#logoutButton:pressed {{ background-color: #801111; }}
            QPushButton#navTabButton {{ background-color: {KOLOR_GLOWNY_1}; color: {KOLOR_TEKSTU_BIALY}; font-size: 15px; font-weight: 500; padding: 10px 20px; border: none; border-radius: 5px; min-height: 30px; }}
            QPushButton#navTabButton:hover {{ background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1}; }}
            QPushButton#navTabButton[active="true"] {{ background-color: {KOLOR_AKCENTUJACY_1}; color: {KOLOR_TEKSTU_NA_JASNYCH_PRZYCISKACH}; }}
            QFrame#CardWidget {{ background-color: {TLO_2_KARTY}; border-radius: 8px; }}
            QWidget#cardTitleBar {{ background-color: {KOLOR_GLOWNY_1}; border-top-left-radius: 8px; border-top-right-radius: 8px; }}
            QLabel#cardTitleLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 18px; font-weight: 600; }}
            QWidget#cardContentArea {{ background-color: transparent; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px; }}
            QLabel#formFieldLabelSmall {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 13px; font-weight: 500; }}
            QLineEdit#formLineEditWhite, QComboBox#formComboBox {{ background-color: {KOLOR_TEKSTU_BIALY}; color: {KOLOR_TEKSTU_W_POLACH_CIEMNY}; border: 1px solid #B0B0B0; border-radius: 5px; padding: 8px; font-size: 14px; }}
            
            QComboBox#formComboBox::drop-down {{ /* Styl dla przycisku strzałki */
                /* border: none; */ /* Można zostawić domyślną ramkę lub usunąć */
                /* background-color: transparent; */ /* Opcjonalnie */
                /* subcontrol-origin: padding; */
                /* subcontrol-position: top right; */
                /* width: 20px; */ /* Domyślna szerokość jest zwykle OK */
            }}
            /* USUNIĘTO lub ZAKOMENTOWANO: QComboBox#formComboBox::down-arrow {{ ... }} */

            QComboBox QAbstractItemView {{ background-color: {KOLOR_TEKSTU_BIALY}; color: {KOLOR_TEKSTU_W_POLACH_CIEMNY}; selection-background-color: {KOLOR_AKCENTUJACY_1}; selection-color: {KOLOR_TEKSTU_W_POLACH_CIEMNY}; border: 1px solid {KOLOR_GLOWNY_1}; border-radius: 4px; }}
            QLineEdit#formLineEditWhite::placeholder {{ color: {KOLOR_PLACEHOLDER}; }}
            QPushButton#accentButton1 {{ background-color: {KOLOR_AKCENTUJACY_1}; color: {KOLOR_TEKSTU_NA_JASNYCH_PRZYCISKACH}; border: none; border-radius: 5px; font-size: 15px; font-weight: 600; padding: 8px 15px; }}
            QPushButton#accentButton1:hover {{ background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1}; }}
            QPushButton#accentButton1Small {{ background-color: {KOLOR_AKCENTUJACY_1}; color: {KOLOR_TEKSTU_NA_JASNYCH_PRZYCISKACH}; border: none; border-radius: 5px; font-size: 13px; font-weight: 600; padding: 6px 12px; }}
            QPushButton#accentButton1Small:hover {{ background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1}; }}
            QPushButton#accentButton2 {{ background-color: {KOLOR_AKCENTUJACY_2}; color: {KOLOR_TEKSTU_BIALY}; border: none; border-radius: 5px; font-size: 15px; font-weight: 600; padding: 8px 15px; }}
            QPushButton#accentButton2:hover {{ background-color: #C03030; }}
            QTableWidget#dataTable {{ background-color: {TLO_2_KARTY}; color: {KOLOR_TEKSTU_BIALY}; gridline-color: {KOLOR_LINII_TABELI}; border: none; font-size: 14px; }}
            QHeaderView::section {{ background-color: {KOLOR_GLOWNY_1}; color: {KOLOR_TEKSTU_BIALY}; padding: 8px; border: none; font-size: 14px; font-weight: 600; }}
            QTableWidget#dataTable::item {{ padding: 8px; border-bottom: 1px solid {KOLOR_LINII_TABELI}; }}
            QTableWidget#dataTable::item:selected {{ background-color: {ZMNIEJSZONA_SATURACJA_AKCENTU_1}; color: {TLO_3_GLOWNE}; }}
            QTableWidget#dataTable QScrollBar:vertical {{ border: none; background: {TLO_2_KARTY}; width: 10px; margin: 0px 0px 0px 0px; }}
            QTableWidget#dataTable QScrollBar::handle:vertical {{ background: {KOLOR_GLOWNY_1}; min-height: 20px; border-radius: 5px; }}
            QTableWidget#dataTable QScrollBar::add-line:vertical, QTableWidget#dataTable QScrollBar::sub-line:vertical {{ height: 0px; }}
            QTableWidget#dataTable::item:alternate {{ background-color: #404847; }}
            QWidget#predictionResultsArea {{ background-color: {KOLOR_AKCENTUJACY_1}; border-radius: 6px; padding: 10px; }}
            QLabel#predictionLabel {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 13px; font-weight: 500; opacity: 0.8; }}
            QLabel#predictionData {{ color: {KOLOR_TEKSTU_BIALY}; font-size: 18px; font-weight: 600; }}
            QTextEdit#optimizationResultsText {{ background-color: {KOLOR_TEKSTU_BIALY}; color: {KOLOR_TEKSTU_W_POLACH_CIEMNY}; border: 1px solid #B0B0B0; border-radius: 5px; padding: 8px; font-size: 14px; }}
        """
        self.setStyleSheet(stylesheet)
        print("Globalny styl QSS został zastosowany.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not os.path.exists(os.path.join(BASE_DIR, "fonts")):
        os.makedirs(os.path.join(BASE_DIR, "fonts"))
        print(f"Utworzono katalog: {os.path.join(BASE_DIR, 'fonts')}. Upewnij się, że umieściłeś w nim pliki fontów Inter.")
    if not os.path.exists(os.path.join(BASE_DIR, "icons")):
        os.makedirs(os.path.join(BASE_DIR, "icons"))
        print(f"Utworzono katalog: {os.path.join(BASE_DIR, 'icons')}. Upewnij się, że umieściłeś w nim pliki ikon.")
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())