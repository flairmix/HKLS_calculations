from PySide6 import QtCore
from PySide6.QtWidgets import (
    QLineEdit,
    QGridLayout,
    QLabel,
    QWidget
)


class InputFieldsConsumption(QWidget):
    def __init__(self, parent=None):
        super(InputFieldsConsumption, self).__init__(parent)

        self.heading = QLabel("Расход по часам, м3/ч", self)
        # self.heading.setFixedWidth(200)
        self.hour_0 = QLabel("00 : 00", self)
        # self.hour_0.setFixedWidth(150)
        # self.hour_0.setAlignment(QtCore.Qt.AlignRight)

        self.hour_0_value = QLineEdit("0.487", self)
        self.hour_1 = QLabel("01 : 00", self)
        self.hour_1_value = QLineEdit("0.487", self)
        self.hour_2 = QLabel("02 : 00", self)
        self.hour_2_value = QLineEdit("0.487", self)
        self.hour_3 = QLabel("03 : 00", self)
        self.hour_3_value = QLineEdit("0.487", self)
        self.hour_4 = QLabel("04 : 00", self)
        self.hour_4_value = QLineEdit("0.487", self)
        self.hour_5 = QLabel("05 : 00", self)
        self.hour_5_value = QLineEdit("5.44", self)
        self.hour_6 = QLabel("06 : 00", self)
        self.hour_6_value = QLineEdit("13.869", self)
        self.hour_7 = QLabel("07 : 00", self)
        self.hour_7_value = QLineEdit("13.869", self)
        self.hour_8 = QLabel("08 : 00", self)
        self.hour_8_value = QLineEdit("5.44", self)
        self.hour_9 = QLabel("09 : 00", self)
        self.hour_9_value = QLineEdit("5.44", self)
        self.hour_10 = QLabel("10 : 00", self)
        self.hour_10_value = QLineEdit("5.44", self)
        self.hour_11 = QLabel("11 : 00", self)
        self.hour_11_value = QLineEdit("4.65", self)

        self.hour_12 = QLabel("12 : 00", self)
        self.hour_12_value = QLineEdit("4.65", self)
        self.hour_13 = QLabel("13 : 00", self)
        self.hour_13_value = QLineEdit("4.65", self)
        self.hour_14 = QLabel("14 : 00", self)
        self.hour_14_value = QLineEdit("4.65", self)
        self.hour_15 = QLabel("15 : 00", self)
        self.hour_15_value = QLineEdit("5.137", self)
        self.hour_16 = QLabel("16 : 00", self)
        self.hour_16_value = QLineEdit("5.44", self)
        self.hour_17 = QLabel("17 : 00", self)
        self.hour_17_value = QLineEdit("5.44", self)
        self.hour_18 = QLabel("18 : 00", self)
        self.hour_18_value = QLineEdit("13.869", self)
        self.hour_19 = QLabel("19 : 00", self)
        self.hour_19_value = QLineEdit("13.869", self)
        self.hour_20 = QLabel("20 : 00", self)
        self.hour_20_value = QLineEdit("5.44", self)
        self.hour_21 = QLabel("21 : 00", self)
        self.hour_21_value = QLineEdit("5.44", self)
        self.hour_22 = QLabel("22 : 00", self)
        self.hour_22_value = QLineEdit("5.44", self)
        self.hour_23 = QLabel("23 : 00", self)
        self.hour_23_value = QLineEdit("5.44", self)



        # Создаем сетку для размещения виджетов
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.heading, 0, 1)

        grid_layout.addWidget(self.hour_0, 2, 0)
        grid_layout.addWidget(self.hour_0_value, 2, 1)
        grid_layout.addWidget(self.hour_1, 3, 0)
        grid_layout.addWidget(self.hour_1_value, 3, 1)
        grid_layout.addWidget(self.hour_2, 4, 0)
        grid_layout.addWidget(self.hour_2_value, 4, 1)
        grid_layout.addWidget(self.hour_3, 5, 0)
        grid_layout.addWidget(self.hour_3_value, 5, 1)
        grid_layout.addWidget(self.hour_4, 6, 0)
        grid_layout.addWidget(self.hour_4_value, 6, 1)
        grid_layout.addWidget(self.hour_5, 7, 0)
        grid_layout.addWidget(self.hour_5_value, 7, 1)
        grid_layout.addWidget(self.hour_6, 8, 0)
        grid_layout.addWidget(self.hour_6_value, 8, 1)
        grid_layout.addWidget(self.hour_7, 9, 0)
        grid_layout.addWidget(self.hour_7_value, 9, 1)
        grid_layout.addWidget(self.hour_8, 10, 0)
        grid_layout.addWidget(self.hour_8_value, 10, 1)
        grid_layout.addWidget(self.hour_9, 11, 0)
        grid_layout.addWidget(self.hour_9_value, 11, 1)
        grid_layout.addWidget(self.hour_10, 12, 0)
        grid_layout.addWidget(self.hour_10_value, 12, 1)
        grid_layout.addWidget(self.hour_11, 13, 0)
        grid_layout.addWidget(self.hour_11_value, 13, 1)

        grid_layout.addWidget(self.hour_12, 2, 2)
        grid_layout.addWidget(self.hour_12_value, 2, 3)
        grid_layout.addWidget(self.hour_13, 3, 2)
        grid_layout.addWidget(self.hour_13_value, 3, 3)
        grid_layout.addWidget(self.hour_14, 4, 2)
        grid_layout.addWidget(self.hour_14_value, 4, 3)
        grid_layout.addWidget(self.hour_15, 5, 2)
        grid_layout.addWidget(self.hour_15_value, 5, 3)
        grid_layout.addWidget(self.hour_16, 6, 2)
        grid_layout.addWidget(self.hour_16_value, 6, 3)
        grid_layout.addWidget(self.hour_17, 7, 2)
        grid_layout.addWidget(self.hour_17_value, 7, 3)
        grid_layout.addWidget(self.hour_18, 8, 2)
        grid_layout.addWidget(self.hour_18_value, 8, 3)
        grid_layout.addWidget(self.hour_19, 9, 2)
        grid_layout.addWidget(self.hour_19_value, 9, 3)
        grid_layout.addWidget(self.hour_20, 10, 2)
        grid_layout.addWidget(self.hour_20_value, 10, 3)
        grid_layout.addWidget(self.hour_21, 11, 2)
        grid_layout.addWidget(self.hour_21_value, 11, 3)
        grid_layout.addWidget(self.hour_22, 12, 2)
        grid_layout.addWidget(self.hour_22_value, 12, 3)
        grid_layout.addWidget(self.hour_23, 13, 2)
        grid_layout.addWidget(self.hour_23_value, 13, 3)

        # Применяем сетку к виджетам
        self.setLayout(grid_layout)
  
        self.list_of_consumption_values = [
            self.hour_0_value,
            self.hour_1_value,
            self.hour_2_value,
            self.hour_3_value,
            self.hour_4_value,
            self.hour_5_value,
            self.hour_6_value,
            self.hour_7_value,
            self.hour_8_value,
            self.hour_9_value,
            self.hour_10_value,
            self.hour_11_value,
            self.hour_12_value,
            self.hour_13_value,
            self.hour_14_value,
            self.hour_15_value,
            self.hour_16_value,
            self.hour_17_value,
            self.hour_18_value,
            self.hour_19_value,
            self.hour_20_value,
            self.hour_21_value,
            self.hour_22_value,
            self.hour_23_value
        ]

            
