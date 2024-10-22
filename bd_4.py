import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QTabWidget, QPushButton,
                             QTextEdit, QFileDialog, QListWidget,
                             QFormLayout, QLineEdit, QLabel, QMessageBox)


class FileScanner(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.button = QPushButton("Выбрать папку")
        self.button.clicked.connect(self.scan_folder)
        self.list_widget = QListWidget()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

    def scan_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            files = os.listdir(folder)
            self.list_widget.clear()
            self.list_widget.addItems(files)


class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.save_button = QPushButton("Сохранить файл")
        self.open_button = QPushButton("Открыть файл")

        self.save_button.clicked.connect(self.save_file)
        self.open_button.clicked.connect(self.open_file)

        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(self.text_edit.toPlainText())

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.text_edit.setPlainText(f.read())


class DataSaver(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.inputs = [QLineEdit() for _ in range(5)]
        self.save_button = QPushButton("Сохранить данные")

        self.save_button.clicked.connect(self.save_data)

        for i, input_field in enumerate(self.inputs):
            self.layout.addRow(QLabel(f"Поле {i + 1}:"), input_field)

        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

    def save_data(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл")
        if file_path:
            try:
                with open(file_path, 'a', encoding='utf-8') as f:
                    for i, input_field in enumerate(self.inputs):
                        key = f'Поле {i + 1}'
                        value = input_field.text()
                        f.write(f"{i + 1}; {key} ~ {value}\n")
                QMessageBox.information(self, 'Успех', 'Данные успешно сохранены!')
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка', f'Не удалось сохранить данные: {e}')


class ListReader(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.button = QPushButton("Загрузить файл")
        self.button.clicked.connect(self.load_file)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                self.list_widget.clear()
                for line in lines:
                    self.list_widget.addItem(line.strip())


class AdditionalDataSaver(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.inputs = [QLineEdit() for _ in range(5)]
        self.save_button = QPushButton("Сохранить дополнительные данные")

        self.save_button.clicked.connect(self.save_data)

        for i, input_field in enumerate(self.inputs):
            self.layout.addRow(QLabel(f"Доп. поле {i + 1}:"), input_field)

        self.layout.addWidget(self.save_button)
        self.setLayout(self.layout)

    def save_data(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл")
        if file_path:
            try:
                with open(file_path, 'a', encoding='utf-8') as f:
                    for i, input_field in enumerate(self.inputs):
                        key = f'Доп. поле {i + 1}'
                        value = input_field.text()
                        f.write(f"{i + 1}; {key} ~ {value}\n")
                QMessageBox.information(self, 'Успех', 'Дополнительные данные успешно сохранены!')
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка', f'Не удалось сохранить данные: {e}')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение на PyQt")
        self.setGeometry(100, 100, 600, 400)

        self.tabs = QTabWidget()
        self.tabs.addTab(FileScanner(), "Сканирование папки")
        self.tabs.addTab(TextEditor(), "Редактор текста")
        self.tabs.addTab(DataSaver(), "Сохранение данных")
        self.tabs.addTab(ListReader(), "Чтение списка")
        self.tabs.addTab(AdditionalDataSaver(), "Доп. сохранение данных")  # Пятая вкладка

        self.setCentralWidget(self.tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# Ссылка на GitHub: https://github.com/your-repo
