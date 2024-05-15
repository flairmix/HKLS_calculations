import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QRectF, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton, 
    QTextEdit
)

import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from  boiler_hours import *

from widgets.description_field import PredefinedTextWidget, DescriptionField
from widgets.input_fields import InputFields
from widgets.action_button import ActionButton


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=10, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.x_data = consumption_1
        self.axes = fig.add_subplot(111)
        self.axes.plot(self.x_data)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setWindowTitle("Расчет бака-аккумулятора по часам")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Создаем виджеты для графика и полей ввода
        self.general_description = PredefinedTextWidget(self.central_widget)
        self.description_field = DescriptionField(self.central_widget)
        self.input_fields = InputFields(self.central_widget)
        self.input_fields.setFixedWidth(500)
        self.action_button = ActionButton(self.central_widget)
        self.mpl = MplCanvas(self.central_widget, width=5, height=4, dpi=100)

        # Создаем вертикальную сетку для размещения виджетов
        vbox = QVBoxLayout()
        vbox.addWidget(self.general_description)
        vbox.addWidget(self.description_field)
        vbox.addWidget(self.input_fields)
        vbox.addWidget(self.action_button)
        vbox.addWidget(self.mpl)
        
        # Применяем вертикальную сетку к центральному виджету
        self.central_widget.setLayout(vbox)


        self.input_fields.name_value.textChanged.connect(self.on_boiler_power_kW_value_changed)

        self.action_button.action_button.clicked.connect(self.on_boiler_power_kW_value_change)


    @Slot(str)
    def on_boiler_power_kW_value_changed(self, new_text):
        # watch
        print(f"Новое значение мощности бойлера: {new_text} - {type(new_text)}")  

    @Slot(str)
    def on_boiler_power_kW_value_change(self):
        # change
        boiler_1.name = self.input_fields.name_value.text() 
        boiler_1.boiler_power_kW = int( self.input_fields.boiler_power_kW_value.text() )
        boiler_1.power_recircle_kW = int( self.input_fields.power_recircle_kW_value.text() )
        boiler_1.boiler_volume_m3 = float( self.input_fields.boiler_volume_m3_value.text() )
        boiler_1.hw_reserve_init = float( self.input_fields.hw_reserve_init_value.text() )
        boiler_1.days = int( self.input_fields.days_value.text() )
        boiler_1.tw1 = int( self.input_fields.tw1_value.text() )
        boiler_1.t3 = int( self.input_fields.t3_value.text() )
        boiler_1.t4 = int( self.input_fields.t4_value.text() )
        boiler_1.t3_boiler = int( self.input_fields.t3_boiler_value.text() )

        boiler_1.calculate()
        # boiler_1.create_df()

        print(f" имя бойлера  : {boiler_1.name} ")  
        print(boiler_1.data)  



if __name__ == '__main__':

    consumption_1 = [-0.487, -0.487, -0.487, -0.487, -0.487,
                    -5.44, -13.869, -13.869, -5.44, -5.44,
                    -5.44, -4.65, -4.65, -4.65, -4.65,
                    -5.137, -5.44, -5.44, -13.869, -13.869,
                    -5.44, -5.44, -5.44, -5.44
                    ]

  
    boiler_1 = Boiler(
                    name ="расчет_1",
                    boiler_power_kW = 600,
                    power_recircle_kW = 193,
                    boiler_volume_m3 = 20,
                    hw_reserve_init = 20,
                    days = 3,
                    consumption_by_hours_24 = consumption_1,
                    tw1 = 10,
                    t3 = 65,
                    t4 = 55,
                    t3_boiler = 65)
    
    boiler_1.calculate()
    boiler_1.create_df()
    

    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())