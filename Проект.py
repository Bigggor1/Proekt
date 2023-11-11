import sys
import io
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>825</width>
    <height>464</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Редактор текстовых файлов</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(250, 231, 165);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>10</y>
      <width>271</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>8</pointsize>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="textFormat">
     <enum>Qt::AutoText</enum>
    </property>
    <property name="indent">
     <number>-1</number>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>100</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(249, 184, 114);</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>80</y>
      <width>91</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Путь к файлу:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>710</x>
      <y>90</y>
      <width>41</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(182, 225, 231);</string>
    </property>
    <property name="text">
     <string>✓</string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>140</y>
      <width>266</width>
      <height>271</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Размер шрифта:</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QSlider" name="horizontalSlider">
       <property name="mouseTracking">
        <bool>false</bool>
       </property>
       <property name="tabletTracking">
        <bool>false</bool>
       </property>
       <property name="minimum">
        <number>6</number>
       </property>
       <property name="maximum">
        <number>28</number>
       </property>
       <property name="singleStep">
        <number>2</number>
       </property>
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
      </widget>
     </item>
     <item>
      <layout class="QGridLayout" name="gridLayout">
       <item row="0" column="0">
        <widget class="QPushButton" name="pushButton_2">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
         <property name="text">
          <string>Стереть всё</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QPushButton" name="pushButton_3">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
         <property name="text">
          <string>Отменить всё</string>
         </property>
        </widget>
       </item>
       <item row="2" column="0">
        <widget class="QPushButton" name="pushButton_7">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
         <property name="text">
          <string>Стиль шрифта</string>
         </property>
        </widget>
       </item>
       <item row="1" column="1">
        <widget class="QPushButton" name="pushButton_4">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
         <property name="text">
          <string>Транскрипция
(ш -&gt; sh)</string>
         </property>
        </widget>
       </item>
       <item row="1" column="0">
        <widget class="QPushButton" name="pushButton_6">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
         <property name="text">
          <string>Транскрипция
(n -&gt; н)</string>
         </property>
        </widget>
       </item>
       <item row="2" column="1">
        <widget class="QPushButton" name="pushButton_8">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
         <property name="text">
          <string>Сохранить</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QLineEdit" name="lineEdit_3">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_4">
         <property name="text">
          <string>-&gt;</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="lineEdit">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(249, 184, 114);</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="pushButton_5">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(182, 225, 231);</string>
         </property>
         <property name="text">
          <string>✓</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton">
       <property name="text">
        <string>Тёмная тема</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>501</width>
      <height>401</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(249, 184, 114);</string>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:22px; margin-bottom:26px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:26px; &quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>825</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
font_template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>815</width>
    <height>324</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Изменить шрифт</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(250, 231, 165);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>791</width>
      <height>271</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="1" column="1">
      <widget class="QPushButton" name="pushButton_7">
       <property name="font">
        <font>
         <family>Candara</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Candara</string>
       </property>
      </widget>
     </item>
     <item row="3" column="1">
      <widget class="QPushButton" name="pushButton_14">
       <property name="font">
        <font>
         <family>Roman</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Roman</string>
       </property>
      </widget>
     </item>
     <item row="1" column="3">
      <widget class="QPushButton" name="pushButton_11">
       <property name="font">
        <font>
         <family>Comic Sans MS</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Comic Sans MS</string>
       </property>
      </widget>
     </item>
     <item row="4" column="1">
      <widget class="QPushButton" name="pushButton_18">
       <property name="font">
        <font>
         <family>System</family>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>System</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QPushButton" name="pushButton_4">
       <property name="font">
        <font>
         <family>Bahnschrift</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Bahnschrift</string>
       </property>
      </widget>
     </item>
     <item row="0" column="3">
      <widget class="QPushButton" name="pushButton_6">
       <property name="font">
        <font>
         <family>Calibri</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Calibri</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QPushButton" name="pushButton_3">
       <property name="font">
        <font>
         <family>Consolas</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Consolas</string>
       </property>
      </widget>
     </item>
     <item row="2" column="3">
      <widget class="QPushButton" name="pushButton_12">
       <property name="font">
        <font>
         <family>Georgia</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Georgia</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QPushButton" name="pushButton_2">
       <property name="font">
        <font>
         <family>Cambria</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Cambria</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QPushButton" name="pushButton_8">
       <property name="font">
        <font>
         <family>Courier</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Courier</string>
       </property>
      </widget>
     </item>
     <item row="1" column="2">
      <widget class="QPushButton" name="pushButton_9">
       <property name="font">
        <font>
         <family>Century</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Century</string>
       </property>
      </widget>
     </item>
     <item row="4" column="0">
      <widget class="QPushButton" name="pushButton_17">
       <property name="font">
        <font>
         <family>Sitka</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Sitka</string>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QPushButton" name="pushButton">
       <property name="font">
        <font>
         <family>Arial</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Arial</string>
       </property>
      </widget>
     </item>
     <item row="4" column="2">
      <widget class="QPushButton" name="pushButton_19">
       <property name="font">
        <font>
         <family>Terminal</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Terminal</string>
       </property>
      </widget>
     </item>
     <item row="2" column="2">
      <widget class="QPushButton" name="pushButton_10">
       <property name="font">
        <font>
         <family>Gabriola</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Gabriola</string>
       </property>
      </widget>
     </item>
     <item row="3" column="2">
      <widget class="QPushButton" name="pushButton_15">
       <property name="font">
        <font>
         <family>Script</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Script</string>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QPushButton" name="pushButton_13">
       <property name="font">
        <font>
         <family>Impact</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Impact</string>
       </property>
      </widget>
     </item>
     <item row="0" column="2">
      <widget class="QPushButton" name="pushButton_5">
       <property name="font">
        <font>
         <family>Book Antiqua</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Book Antiqua</string>
       </property>
      </widget>
     </item>
     <item row="3" column="3">
      <widget class="QPushButton" name="pushButton_16">
       <property name="font">
        <font>
         <family>Segoe Print</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Segoe Print</string>
       </property>
      </widget>
     </item>
     <item row="4" column="3">
      <widget class="QPushButton" name="pushButton_20">
       <property name="font">
        <font>
         <family>Times New Roman</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(249, 184, 114);</string>
       </property>
       <property name="text">
        <string>Times New Roman</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>815</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''
file = ''
file_txt = ''
letters = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n\
", "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#", "ф\
": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r", "о": "o\
", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya", "ч": "ch", "с\
": "s", "м": "m", "и": "i", "т": "t", "ь": "'", "б": "b", "ю": "ju\
", "ё": "jo"}
letters_2 = {'a': 'а','b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф\
', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м\
', 'n': 'н', 'о': 'о', 'p': 'п', 'q': 'ку', 'r': 'р', 's': 'с', 't': 'т\
', 'u': 'ю', 'v': 'в', 'w': 'ув', 'x': 'кс', 'y': 'и', 'z': 'з', "'": "ь"}


class FontEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(font_template)
        uic.loadUi(f, self)
        
        self.pushButton_13.clicked.connect(self.Impact)
        self.pushButton.clicked.connect(self.Arial)
        self.pushButton_4.clicked.connect(self.Bahnschrift)
        self.pushButton_5.clicked.connect(self.Book_Antiqua)
        self.pushButton_6.clicked.connect(self.Calibri)
        self.pushButton_2.clicked.connect(self.Cambria)
        self.pushButton_7.clicked.connect(self.Candara)
        self.pushButton_9.clicked.connect(self.Century)
        self.pushButton_11.clicked.connect(self.Comic_Sans_MS)
        self.pushButton_3.clicked.connect(self.Consolas)
        self.pushButton_8.clicked.connect(self.Courier)
        self.pushButton_10.clicked.connect(self.Gabriola)
        self.pushButton_12.clicked.connect(self.Georgia)
        self.pushButton_14.clicked.connect(self.Roman)
        self.pushButton_15.clicked.connect(self.Script)
        self.pushButton_16.clicked.connect(self.Segoe_Print)
        self.pushButton_17.clicked.connect(self.Sitka)
        self.pushButton_18.clicked.connect(self.System)
        self.pushButton_19.clicked.connect(self.Terminal)
        self.pushButton_20.clicked.connect(self.Times_New_Roman)
        
    def Impact(self):
        font = QtGui.QFont('Impact', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)        
        
    def Arial(self):
        font = QtGui.QFont('Arial', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Bahnschrift(self):
        font = QtGui.QFont('Bahnschrift', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Book_Antiqua(self):
        font = QtGui.QFont('Book Antiqua', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Calibri(self):
        font = QtGui.QFont('Calibri', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Cambria(self):
        font = QtGui.QFont('Cambria', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Candara(self):
        font = QtGui.QFont('Candara', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Century(self):
        font = QtGui.QFont('Century', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Comic_Sans_MS(self):
        font = QtGui.QFont('Comic Sans MS', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Consolas(self):
        font = QtGui.QFont('Consolas', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Courier(self):
        font = QtGui.QFont('Courier', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Gabriola(self):
        font = QtGui.QFont('Gabriola', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Georgia(self):
        font = QtGui.QFont('Georgia', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Roman(self):
        font = QtGui.QFont('Roman', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Script(self):
        font = QtGui.QFont('Script', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Segoe_Print(self):
        font = QtGui.QFont('Segoe Print', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
        
    def Sitka(self):
        font = QtGui.QFont('Sitka', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
    
    def System(self):
        font = QtGui.QFont('System', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
    
    def Terminal(self):
        font = QtGui.QFont('Terminal', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)
    
    def Times_New_Roman(self):
        font = QtGui.QFont('Times New Roman', ex.textEdit.currentFont().pointSize())
        ex.textEdit.setFont(font)


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        
        self.pushButton.clicked.connect(self.start)
        self.horizontalSlider.valueChanged.connect(self.font_size)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.restart)
        self.pushButton_5.clicked.connect(self.change)
        self.pushButton_4.clicked.connect(self.ruseng)
        self.pushButton_6.clicked.connect(self.engrus)
        self.pushButton_8.clicked.connect(self.save)
        self.pushButton_7.clicked.connect(self.font_style)
        self.radioButton.toggled.connect(self.onClicked)
        
    def start(self):
        global file
        global file_txt
        try:
            file = open(self.lineEdit_2.text(), mode="r+", encoding="utf8")
            print(type(file))
            file_txt = file.read()
            self.textEdit.setText(file_txt)
            self.lineEdit_2.setText('')
            self.label.setText('')
        except FileNotFoundError:
            self.lineEdit_2.setText('')
            self.textEdit.setText('')
            self.label.setText('Несуществующий файл')
    
    def font_size(self):
        font = QtGui.QFont(self.textEdit.currentFont().family(), self.horizontalSlider.value())
        self.textEdit.setFont(font)
    
    def clear(self):
        self.textEdit.setText('')
    
    def restart(self):
        self.textEdit.setText(file_txt)
    
    def change(self):
        self.textEdit.setText(self.textEdit.toPlainText().replace(self.lineEdit_3.text(), self.lineEdit.text()))
    
    def ruseng(self):
        x = self.textEdit.toPlainText()
        for i in letters:
                x = x.replace(i, letters[i])
                x = x.replace(i.upper(), letters[i].capitalize())
        self.textEdit.setText(x)
    
    def engrus(self):
        x = self.textEdit.toPlainText()
        for i in letters_2:
                x = x.replace(i, letters_2[i])
                x = x.replace(i.upper(), letters_2[i].capitalize())
        self.textEdit.setText(x)        
        
    def save(self):
        try:
            global file
            file.truncate(0)
            file.seek(0)
            file.write(self.textEdit.toPlainText())
        except:
            self.label.setText('Введите путь к файлу')
    
    def font_style(self):
        font.show()
        
    def to_light(self):
        self.setStyleSheet("QMainWindow {background-color: #FAE7A5;}")
        self.radioButton.setStyleSheet("QRadioButton {color: #000000;}")
        self.label.setStyleSheet("QLabel {color: #000000;}")
        self.label_2.setStyleSheet("QLabel {color: #000000;}")
        self.label_3.setStyleSheet("QLabel {color: #000000;}")
        self.label_4.setStyleSheet("QLabel {color: #000000;}")
        self.textEdit.setStyleSheet("QTextEdit {background-color: #F9B872;}")
        self.lineEdit_2.setStyleSheet("QLineEdit {background-color: #F9B872;}")
        self.lineEdit_3.setStyleSheet("QLineEdit {background-color: #F9B872;}")
        self.lineEdit.setStyleSheet("QLineEdit {background-color: #F9B872;}")
        self.pushButton_5.setStyleSheet("QPushButton {background-color: #B6E1E7; color: #000000;}")
        self.pushButton.setStyleSheet("QPushButton {background-color: #B6E1E7; color: #000000;}")            
        self.pushButton_4.setStyleSheet("QPushButton {background-color: #F9B872;}")
        self.pushButton_3.setStyleSheet("QPushButton {background-color: #F9B872;}")
        self.pushButton_2.setStyleSheet("QPushButton {background-color: #F9B872;}")
        self.pushButton_6.setStyleSheet("QPushButton {background-color: #F9B872;}")
        self.pushButton_7.setStyleSheet("QPushButton {background-color: #F9B872;}")   
        self.pushButton_8.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_2.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_3.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_4.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_5.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_6.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_7.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_8.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_9.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_10.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_11.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_12.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_13.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_14.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_15.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_16.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_17.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_18.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_19.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.pushButton_20.setStyleSheet("QPushButton {background-color: #F9B872;}")
        font.setStyleSheet("QMainWindow {background-color: #FAE7A5;}")
        
    def to_black(self):
        self.setStyleSheet("QMainWindow {background-color: #0C1A1A;}")
        self.radioButton.setStyleSheet("QRadioButton {color: #FFFFFF;}")
        self.label.setStyleSheet("QLabel {color: #FFFFFF;}")
        self.label_2.setStyleSheet("QLabel {color: #FFFFFF;}")
        self.label_3.setStyleSheet("QLabel {color: #FFFFFF;}")
        self.label_4.setStyleSheet("QLabel {color: #FFFFFF;}")
        self.textEdit.setStyleSheet("QTextEdit {background-color: #152d2d; color: #FFFFFF;}")
        self.lineEdit_2.setStyleSheet("QLineEdit {background-color: #152d2d; color: #FFFFFF;}")
        self.lineEdit_3.setStyleSheet("QLineEdit {background-color: #152d2d; color: #FFFFFF;}")
        self.lineEdit.setStyleSheet("QLineEdit {background-color: #152d2d; color: #FFFFFF;}")
        self.pushButton_5.setStyleSheet("QPushButton {background-color: #6ACFC7; color: #FFFFFF;}")
        self.pushButton.setStyleSheet("QPushButton {background-color: #6ACFC7; color: #FFFFFF;}")
        self.pushButton_4.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        self.pushButton_3.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        self.pushButton_2.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        self.pushButton_6.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        self.pushButton_7.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        self.pushButton_8.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        self.pushButton_8.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_2.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_2.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_3.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_4.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_5.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_6.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_7.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_8.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_9.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_10.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_11.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_12.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_13.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_14.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_15.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_16.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_17.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_18.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_19.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.pushButton_20.setStyleSheet("QPushButton {background-color: #152d2d; color: #FFFFFF;}")
        font.setStyleSheet("QMainWindow {background-color: #0C1A1A;}")
        
    def onClicked(self, button):
        if self.radioButton.isChecked() == True:
            self.to_black()
            self.set_settings('black')
            
        if self.radioButton.isChecked() == False:
            self.to_light()
            self.set_settings('light')
    
    def get_settings(self):
        result = cur.execute("SELECT * FROM data WHERE name = 'tema';").fetchall()
        return result[0][2]
    
    def set_settings(self, tema_color):
        cur.execute(f"UPDATE data SET value = '{tema_color}' WHERE name = 'tema'")
        con.commit()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextEditor()
    font = FontEditor()
    con = sqlite3.connect("bd.sqlite")
    cur = con.cursor()    
    if ex.get_settings() == 'black':
        ex.to_black()
        ex.radioButton.setChecked(True)
    cur.execute("UPDATE data SET value = 'red' WHERE name = 'tema'")
    ex.show()
    sys.exit(app.exec_())