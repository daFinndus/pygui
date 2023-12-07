import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Importiere die generierte UI-Klasse
from gui import Ui_PyGUI


class MainWindow(QMainWindow, Ui_PyGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Verbinde die Schaltflächen mit Funktionen
        self.button_update.clicked.connect(self.update_clicked)
        self.button_start.clicked.connect(self.start_clicked)
        self.button_stop.clicked.connect(self.stop_clicked)

    def update_clicked(self):
        print("Update button clicked")

    def start_clicked(self):
        print("Start button clicked")

    def stop_clicked(self):
        print("Stop button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
