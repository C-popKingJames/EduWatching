# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassroomWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Classroom(object):
    def setupUi(self, Form_Classroom):
        Form_Classroom.setObjectName("Form_Classroom")
        Form_Classroom.resize(340, 305)
        Form_Classroom.setMinimumSize(QtCore.QSize(340, 305))
        Form_Classroom.setMaximumSize(QtCore.QSize(340, 305))
        Form_Classroom.setStyleSheet("#Form_Classroom {\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(214, 214, 214);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form_Classroom)
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_img = QtWidgets.QLabel(Form_Classroom)
        self.label_img.setMinimumSize(QtCore.QSize(320, 180))
        self.label_img.setMaximumSize(QtCore.QSize(320, 180))
        self.label_img.setObjectName("label_img")
        self.verticalLayout_4.addWidget(self.label_img)
        self.widget = QtWidgets.QWidget(Form_Classroom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_arrdess = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_arrdess.sizePolicy().hasHeightForWidth())
        self.widget_arrdess.setSizePolicy(sizePolicy)
        self.widget_arrdess.setObjectName("widget_arrdess")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_arrdess)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_address_title = QtWidgets.QLabel(self.widget_arrdess)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_address_title.setFont(font)
        self.label_address_title.setObjectName("label_address_title")
        self.verticalLayout.addWidget(self.label_address_title, 0, QtCore.Qt.AlignHCenter)
        self.label_address = QtWidgets.QLabel(self.widget_arrdess)
        self.label_address.setObjectName("label_address")
        self.verticalLayout.addWidget(self.label_address, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.widget_arrdess)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.widget_teacher = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_teacher.sizePolicy().hasHeightForWidth())
        self.widget_teacher.setSizePolicy(sizePolicy)
        self.widget_teacher.setObjectName("widget_teacher")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_teacher)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_teacher_title = QtWidgets.QLabel(self.widget_teacher)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_teacher_title.setFont(font)
        self.label_teacher_title.setObjectName("label_teacher_title")
        self.verticalLayout_2.addWidget(self.label_teacher_title, 0, QtCore.Qt.AlignHCenter)
        self.label_teacher = QtWidgets.QLabel(self.widget_teacher)
        self.label_teacher.setObjectName("label_teacher")
        self.verticalLayout_2.addWidget(self.label_teacher, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.widget_teacher)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.widget_project = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_project.sizePolicy().hasHeightForWidth())
        self.widget_project.setSizePolicy(sizePolicy)
        self.widget_project.setObjectName("widget_project")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_project)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_project_title = QtWidgets.QLabel(self.widget_project)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_project_title.setFont(font)
        self.label_project_title.setObjectName("label_project_title")
        self.verticalLayout_3.addWidget(self.label_project_title, 0, QtCore.Qt.AlignHCenter)
        self.label_project = QtWidgets.QLabel(self.widget_project)
        self.label_project.setObjectName("label_project")
        self.verticalLayout_3.addWidget(self.label_project, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.widget_project)
        self.verticalLayout_4.addWidget(self.widget)
        self.widget_count = QtWidgets.QWidget(Form_Classroom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_count.sizePolicy().hasHeightForWidth())
        self.widget_count.setSizePolicy(sizePolicy)
        self.widget_count.setObjectName("widget_count")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_count)
        self.horizontalLayout_3.setContentsMargins(0, 8, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_amount = QtWidgets.QWidget(self.widget_count)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_amount.sizePolicy().hasHeightForWidth())
        self.widget_amount.setSizePolicy(sizePolicy)
        self.widget_amount.setObjectName("widget_amount")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_amount)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_amount = QtWidgets.QLabel(self.widget_amount)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        self.horizontalLayout.addWidget(self.label_amount)
        self.label_amount_no = QtWidgets.QLabel(self.widget_amount)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_amount_no.setFont(font)
        self.label_amount_no.setObjectName("label_amount_no")
        self.horizontalLayout.addWidget(self.label_amount_no)
        self.horizontalLayout_3.addWidget(self.widget_amount)
        self.line_3 = QtWidgets.QFrame(self.widget_count)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.widget_present = QtWidgets.QWidget(self.widget_count)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_present.sizePolicy().hasHeightForWidth())
        self.widget_present.setSizePolicy(sizePolicy)
        self.widget_present.setObjectName("widget_present")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_present)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_present = QtWidgets.QLabel(self.widget_present)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_present.setFont(font)
        self.label_present.setObjectName("label_present")
        self.horizontalLayout_2.addWidget(self.label_present)
        self.label_present_no = QtWidgets.QLabel(self.widget_present)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_present_no.setFont(font)
        self.label_present_no.setObjectName("label_present_no")
        self.horizontalLayout_2.addWidget(self.label_present_no)
        self.horizontalLayout_3.addWidget(self.widget_present)
        self.verticalLayout_4.addWidget(self.widget_count)

        self.retranslateUi(Form_Classroom)
        QtCore.QMetaObject.connectSlotsByName(Form_Classroom)

    def retranslateUi(self, Form_Classroom):
        _translate = QtCore.QCoreApplication.translate
        Form_Classroom.setWindowTitle(_translate("Form_Classroom", "Form"))
        self.label_img.setText(_translate("Form_Classroom", "图片"))
        self.label_address_title.setText(_translate("Form_Classroom", "<html><head/><body><p><span style=\" font-weight:600;\">地点</span></p></body></html>"))
        self.label_address.setText(_translate("Form_Classroom", "一教A503"))
        self.label_teacher_title.setText(_translate("Form_Classroom", "<html><head/><body><p><span style=\" font-weight:600;\">教师</span></p></body></html>"))
        self.label_teacher.setText(_translate("Form_Classroom", "王鹏"))
        self.label_project_title.setText(_translate("Form_Classroom", "<html><head/><body><p><span style=\" font-weight:600;\">科目</span></p></body></html>"))
        self.label_project.setText(_translate("Form_Classroom", "形式与政策3"))
        self.label_amount.setText(_translate("Form_Classroom", "<html><head/><body><p><span style=\" font-weight:600;\">总人数：</span></p></body></html>"))
        self.label_amount_no.setText(_translate("Form_Classroom", "32"))
        self.label_present.setText(_translate("Form_Classroom", "<html><head/><body><p><span style=\" font-weight:600;\">实到人数：</span></p></body></html>"))
        self.label_present_no.setText(_translate("Form_Classroom", "32"))
