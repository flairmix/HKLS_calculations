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


consumption = [-0.487, -0.487, -0.487, -0.487, -0.487,
                -5.44, -13.869, -13.869, -5.44, -5.44,
                -5.44, -4.65, -4.65, -4.65, -4.65,
                -5.137, -5.44, -5.44, -13.869, -13.869,
                -5.44, -5.44, -5.44, -5.44
                ]

boiler_inputs = {"name" : "calculation_name",
                "boiler_power_kW" : 450,
                "power_recircle_kW" : 193,
                "boiler_volume_m3" : 20,
                "hw_reserve_init" : 20,
                "days" : 3,
                "tw1" : 5,
                "t3" : 65,
                "t4" : 55,
                "t3_boiler" : 65, 
                "consumption_by_hours_24" : consumption
                }


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=24, height=8, dpi=100, hours=24, boiler=Boiler(**boiler_inputs), consumption='decrease'):
        '''
        consumption = 'decrease' / 'increase'
        '''
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        
        hours_x = [i for i in range(0, hours)]

        self.axes = fig.add_subplot(111)

        for i in range(0, len(hours_x), 1):
            print(i)
            print(boiler.hw_reserve_and_boil[i])
            if (i == 0):
                plt.text(hours_x[i], boiler.hw_reserve_and_boil[i]+0.2, f"{round(boiler.hw_reserve_and_boil[i], 1)} м3/ч")
            elif (i != 0 and abs(boiler.hw_reserve_and_boil[i] - boiler.hw_reserve_and_boil[i-1]) > 0.5):
                plt.text(hours_x[i]+0.5, boiler.hw_reserve_and_boil[i]+0.2, f"{round(boiler.hw_reserve_and_boil[i], 1)} м3/ч")
        
        for i in range(0, len(hours_x), 1):
            if (i == 0):
                plt.text(hours_x[i], boiler.consumption_by_hours_24[i]-0.8, f"{round(boiler.consumption_by_hours_24[i], 1)} м3/ч")
            elif (i != 0 and abs(boiler.consumption_by_hours_24[i] - boiler.consumption_by_hours_24[i-1]) > 0.5):
                plt.text(hours_x[i], boiler.consumption_by_hours_24[i]-0.8, f"{round(boiler.consumption_by_hours_24[i], 1)} м3/ч")


        self.axes.plot(hours_x, [0] * len(hours_x), "r-")
        self.axes.plot(hours_x, boiler.consumption_by_hours_24, "b.-", label=f'Расход горячей воды из бойлера {boiler.t3_boiler} гр')
        self.axes.plot(hours_x, boiler.hw_reserve_and_boil, "g.-", label=f'Запас воды в бойлере {boiler.t3_boiler} гр')
        self.axes.plot(hours_x, boiler.boiler_heating_G_list, ".-", label=f'Нагрев воды бойлере до {boiler.t3_boiler} гр')
        
        plt.title("Запас горячей воды в бойлере")
        plt.xlabel('hours')
        plt.ylabel('consumption')
        plt.grid(True)
        plt.legend()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        
        # FigureCanvas.updateGeometry(self)


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setWindowTitle("Расчет бака-аккумулятора по часам")
        self.central_widget = QWidget()
        # self.central_widget.setMinimumWidth(500)
        self.setCentralWidget(self.central_widget)
        
        # Создаем виджеты для графика и полей ввода
        self.general_description = PredefinedTextWidget(self.central_widget)
        self.description_field = DescriptionField(self.central_widget)
        self.input_fields = InputFields(self.central_widget)
        self.input_fields.setFixedWidth(500)
        self.action_button = ActionButton(self.central_widget)
        self.action_button.setFixedWidth(500)
        self.mpl = MplCanvas(self.central_widget, width=24, height=12, dpi=60, boiler=boiler, hours=boiler.days*24)

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
        boiler_inputs["name"] = self.input_fields.name_value.text() 
        boiler_inputs["boiler_power_kW"] = int( self.input_fields.boiler_power_kW_value.text() )
        boiler_inputs["power_recircle_kW"] = int( self.input_fields.power_recircle_kW_value.text() )
        boiler_inputs["boiler_volume_m3"] = float( self.input_fields.boiler_volume_m3_value.text() )
        boiler_inputs["hw_reserve_init"] = float( self.input_fields.hw_reserve_init_value.text() )
        boiler_inputs["days"] = int( self.input_fields.days_value.text() )
        boiler_inputs["tw1"] = int( self.input_fields.tw1_value.text() )
        boiler_inputs["t3"] = int( self.input_fields.t3_value.text() )
        boiler_inputs["t4"] = int( self.input_fields.t4_value.text() )
        boiler_inputs["t3_boiler"] = int( self.input_fields.t3_boiler_value.text() )

        boiler = Boiler(**boiler_inputs)
        
        boiler.calculate()
        boiler.create_df()

        print(f" имя бойлера  : {boiler.name} ")  
        print(boiler.data.head(5))  


if __name__ == '__main__':

    consumption_init = [-0.487, -0.487, -0.487, -0.487, -0.487,
                    -5.44, -13.869, -13.869, -5.44, -5.44,
                    -5.44, -4.65, -4.65, -4.65, -4.65,
                    -5.137, -5.44, -5.44, -13.869, -13.869,
                    -5.44, -5.44, -5.44, -5.44
                    ]
  
    boiler = Boiler(
                    name ="расчет_1",
                    boiler_power_kW = 450,
                    power_recircle_kW = 193,
                    boiler_volume_m3 = 20,
                    hw_reserve_init = 20,
                    days = 3,
                    consumption_by_hours_24 = consumption_init,
                    tw1 = 10,
                    t3 = 65,
                    t4 = 55,
                    t3_boiler = 65)
    
    boiler.calculate()
    boiler.create_df()

    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())