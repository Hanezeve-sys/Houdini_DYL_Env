# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'env_master.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EnvMaster(object):
    def setupUi(self, EnvMaster):
        if not EnvMaster.objectName():
            EnvMaster.setObjectName(u"EnvMaster")
        EnvMaster.resize(1056, 578)
        EnvMaster.setFocusPolicy(Qt.WheelFocus)
        self.horizontalLayout_4 = QHBoxLayout(EnvMaster)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(EnvMaster)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.env_manager_tab = QWidget()
        self.env_manager_tab.setObjectName(u"env_manager_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.env_manager_tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.env_manager_tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.horizontalLayout = QHBoxLayout(self.frame_11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.undoView_2 = QUndoView(self.frame_11)
        self.undoView_2.setObjectName(u"undoView_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.undoView_2.sizePolicy().hasHeightForWidth())
        self.undoView_2.setSizePolicy(sizePolicy1)
        self.undoView_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: None")

        self.horizontalLayout.addWidget(self.undoView_2)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.env_path_tree = QTreeWidget(self.groupBox)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Env Path");
        self.env_path_tree.setHeaderItem(__qtreewidgetitem)
        self.env_path_tree.setObjectName(u"env_path_tree")
        self.env_path_tree.setSortingEnabled(True)
        self.env_path_tree.setExpandsOnDoubleClick(False)
        self.env_path_tree.header().setCascadingSectionResizes(True)
        self.env_path_tree.header().setMinimumSectionSize(200)
        self.env_path_tree.header().setDefaultSectionSize(200)
        self.env_path_tree.header().setProperty("showSortIndicator", True)

        self.horizontalLayout_12.addWidget(self.env_path_tree)

        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.packages_tree = QTreeWidget(self.frame_8)
        self.packages_tree.setObjectName(u"packages_tree")
        self.packages_tree.setSortingEnabled(True)
        self.packages_tree.setExpandsOnDoubleClick(False)
        self.packages_tree.header().setMinimumSectionSize(200)
        self.packages_tree.header().setDefaultSectionSize(200)

        self.verticalLayout_4.addWidget(self.packages_tree)

        self.package_files_tree = QTreeWidget(self.frame_8)
        self.package_files_tree.setObjectName(u"package_files_tree")
        self.package_files_tree.setSortingEnabled(True)
        self.package_files_tree.setExpandsOnDoubleClick(False)
        self.package_files_tree.header().setMinimumSectionSize(200)
        self.package_files_tree.header().setDefaultSectionSize(200)

        self.verticalLayout_4.addWidget(self.package_files_tree)


        self.horizontalLayout_12.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.undoView_3 = QUndoView(self.frame_2)
        self.undoView_3.setObjectName(u"undoView_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.undoView_3.sizePolicy().hasHeightForWidth())
        self.undoView_3.setSizePolicy(sizePolicy3)
        self.undoView_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_7.addWidget(self.undoView_3)

        self.refresh_btn = QPushButton(self.frame_2)
        self.refresh_btn.setObjectName(u"refresh_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.refresh_btn)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.tabWidget.addTab(self.env_manager_tab, "")
        self.env_creator_tab = QWidget()
        self.env_creator_tab.setObjectName(u"env_creator_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.env_creator_tab)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.env_creator_tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.FolderPath = QLineEdit(self.frame_5)
        self.FolderPath.setObjectName(u"FolderPath")

        self.horizontalLayout_6.addWidget(self.FolderPath)

        self.toolButton = QToolButton(self.frame_5)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_6.addWidget(self.toolButton)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.custom_json_name = QCheckBox(self.frame_10)
        self.custom_json_name.setObjectName(u"custom_json_name")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.custom_json_name.sizePolicy().hasHeightForWidth())
        self.custom_json_name.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.custom_json_name)

        self.custom_name_frame = QFrame(self.frame_10)
        self.custom_name_frame.setObjectName(u"custom_name_frame")
        self.custom_name_frame.setEnabled(False)
        self.custom_name_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.custom_name_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.at_home = QLabel(self.custom_name_frame)
        self.at_home.setObjectName(u"at_home")

        self.horizontalLayout_9.addWidget(self.at_home)

        self.name_at_home = QLineEdit(self.custom_name_frame)
        self.name_at_home.setObjectName(u"name_at_home")

        self.horizontalLayout_9.addWidget(self.name_at_home)

        self.at_package = QLabel(self.custom_name_frame)
        self.at_package.setObjectName(u"at_package")

        self.horizontalLayout_9.addWidget(self.at_package)

        self.name_at_package = QLineEdit(self.custom_name_frame)
        self.name_at_package.setObjectName(u"name_at_package")

        self.horizontalLayout_9.addWidget(self.name_at_package)


        self.horizontalLayout_8.addWidget(self.custom_name_frame)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.edit_contents_home = QPushButton(self.frame_7)
        self.edit_contents_home.setObjectName(u"edit_contents_home")

        self.horizontalLayout_10.addWidget(self.edit_contents_home)

        self.edit_contents_package = QPushButton(self.frame_7)
        self.edit_contents_package.setObjectName(u"edit_contents_package")

        self.horizontalLayout_10.addWidget(self.edit_contents_package)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.otls = QCheckBox(self.frame_6)
        self.otls.setObjectName(u"otls")
        self.otls.setChecked(True)

        self.gridLayout.addWidget(self.otls, 2, 3, 1, 1)

        self.packages = QCheckBox(self.frame_6)
        self.packages.setObjectName(u"packages")
        self.packages.setEnabled(False)
        self.packages.setChecked(True)

        self.gridLayout.addWidget(self.packages, 2, 4, 1, 1)

        self.help = QCheckBox(self.frame_6)
        self.help.setObjectName(u"help")
        self.help.setAutoFillBackground(False)
        self.help.setChecked(True)

        self.gridLayout.addWidget(self.help, 2, 1, 1, 1)

        self.toolbar = QCheckBox(self.frame_6)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setChecked(True)

        self.gridLayout.addWidget(self.toolbar, 4, 2, 1, 1)

        self.scripts = QCheckBox(self.frame_6)
        self.scripts.setObjectName(u"scripts")
        self.scripts.setChecked(True)

        self.gridLayout.addWidget(self.scripts, 3, 0, 1, 1)

        self.viewer_handles = QCheckBox(self.frame_6)
        self.viewer_handles.setObjectName(u"viewer_handles")
        self.viewer_handles.setChecked(True)

        self.gridLayout.addWidget(self.viewer_handles, 4, 1, 1, 1)

        self.python_panels = QCheckBox(self.frame_6)
        self.python_panels.setObjectName(u"python_panels")
        self.python_panels.setChecked(True)

        self.gridLayout.addWidget(self.python_panels, 3, 4, 1, 1)

        self.examples = QCheckBox(self.frame_6)
        self.examples.setObjectName(u"examples")
        self.examples.setChecked(True)

        self.gridLayout.addWidget(self.examples, 2, 0, 1, 1)

        self.viewer_states = QCheckBox(self.frame_6)
        self.viewer_states.setObjectName(u"viewer_states")
        self.viewer_states.setChecked(True)

        self.gridLayout.addWidget(self.viewer_states, 4, 0, 1, 1)

        self.pythonlibs = QCheckBox(self.frame_6)
        self.pythonlibs.setObjectName(u"pythonlibs")
        self.pythonlibs.setChecked(True)

        self.gridLayout.addWidget(self.pythonlibs, 3, 3, 1, 1)

        self.vex = QCheckBox(self.frame_6)
        self.vex.setObjectName(u"vex")
        self.vex.setChecked(True)

        self.gridLayout.addWidget(self.vex, 3, 1, 1, 1)

        self.ocl = QCheckBox(self.frame_6)
        self.ocl.setObjectName(u"ocl")
        self.ocl.setChecked(True)

        self.gridLayout.addWidget(self.ocl, 2, 2, 1, 1)

        self.desktop = QCheckBox(self.frame_6)
        self.desktop.setObjectName(u"desktop")
        self.desktop.setChecked(True)

        self.gridLayout.addWidget(self.desktop, 3, 2, 1, 1)

        self.presets = QCheckBox(self.frame_6)
        self.presets.setObjectName(u"presets")
        self.presets.setChecked(True)

        self.gridLayout.addWidget(self.presets, 4, 3, 1, 1)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.env_create = QPushButton(self.frame_9)
        self.env_create.setObjectName(u"env_create")

        self.gridLayout_2.addWidget(self.env_create, 0, 1, 1, 1, Qt.AlignTop)

        self.undoView = QUndoView(self.frame_9)
        self.undoView.setObjectName(u"undoView")
        self.undoView.setEnabled(True)
        self.undoView.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: None")

        self.gridLayout_2.addWidget(self.undoView, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.tabWidget.addTab(self.env_creator_tab, "")
        self.options_tab = QWidget()
        self.options_tab.setObjectName(u"options_tab")
        self.verticalLayout_5 = QVBoxLayout(self.options_tab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.options_tab)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy6)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.external_editor = QLabel(self.frame_12)
        self.external_editor.setObjectName(u"external_editor")

        self.horizontalLayout_11.addWidget(self.external_editor)

        self.external_editor_dir = QLineEdit(self.frame_12)
        self.external_editor_dir.setObjectName(u"external_editor_dir")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.external_editor_dir.sizePolicy().hasHeightForWidth())
        self.external_editor_dir.setSizePolicy(sizePolicy7)

        self.horizontalLayout_11.addWidget(self.external_editor_dir)

        self.external_editor_choose = QToolButton(self.frame_12)
        self.external_editor_choose.setObjectName(u"external_editor_choose")

        self.horizontalLayout_11.addWidget(self.external_editor_choose)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.options_tab)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_13)

        self.tabWidget.addTab(self.options_tab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout_4.addWidget(self.frame)


        self.retranslateUi(EnvMaster)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EnvMaster)
    # setupUi

    def retranslateUi(self, EnvMaster):
        EnvMaster.setWindowTitle(QCoreApplication.translate("EnvMaster", u"Houdini Env Master", None))
        self.groupBox.setTitle(QCoreApplication.translate("EnvMaster", u"View Pad:", None))
        ___qtreewidgetitem = self.env_path_tree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("EnvMaster", u"Path", None));
        ___qtreewidgetitem1 = self.packages_tree.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("EnvMaster", u"Path", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("EnvMaster", u"Pakcages", None));
        ___qtreewidgetitem2 = self.package_files_tree.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("EnvMaster", u"Path", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("EnvMaster", u"Package Files", None));
        self.refresh_btn.setText(QCoreApplication.translate("EnvMaster", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.env_manager_tab), QCoreApplication.translate("EnvMaster", u"Env Manager", None))
        self.label.setText(QCoreApplication.translate("EnvMaster", u"Folder Path", None))
        self.toolButton.setText(QCoreApplication.translate("EnvMaster", u"...", None))
        self.custom_json_name.setText(QCoreApplication.translate("EnvMaster", u"Use Custom Json File Name:", None))
        self.at_home.setText(QCoreApplication.translate("EnvMaster", u" Home", None))
        self.at_package.setText(QCoreApplication.translate("EnvMaster", u"Package", None))
        self.edit_contents_home.setText(QCoreApplication.translate("EnvMaster", u"Edit Preset Contents To HOME", None))
        self.edit_contents_package.setText(QCoreApplication.translate("EnvMaster", u"Edit Preset Contents To Packages", None))
        self.otls.setText(QCoreApplication.translate("EnvMaster", u"otls", None))
        self.packages.setText(QCoreApplication.translate("EnvMaster", u"packages", None))
        self.help.setText(QCoreApplication.translate("EnvMaster", u"help", None))
        self.toolbar.setText(QCoreApplication.translate("EnvMaster", u"toolbar", None))
        self.scripts.setText(QCoreApplication.translate("EnvMaster", u"scripts", None))
        self.viewer_handles.setText(QCoreApplication.translate("EnvMaster", u"viewer_handles", None))
        self.python_panels.setText(QCoreApplication.translate("EnvMaster", u"python_panels", None))
        self.examples.setText(QCoreApplication.translate("EnvMaster", u"examples", None))
        self.viewer_states.setText(QCoreApplication.translate("EnvMaster", u"viewer_states", None))
        self.pythonlibs.setText(QCoreApplication.translate("EnvMaster", u"python3.7libs", None))
        self.vex.setText(QCoreApplication.translate("EnvMaster", u"vex", None))
        self.ocl.setText(QCoreApplication.translate("EnvMaster", u"ocl", None))
        self.desktop.setText(QCoreApplication.translate("EnvMaster", u"desktop", None))
        self.presets.setText(QCoreApplication.translate("EnvMaster", u"presets", None))
        self.label_2.setText(QCoreApplication.translate("EnvMaster", u"Sub  File To Create:", None))
        self.env_create.setText(QCoreApplication.translate("EnvMaster", u" Create", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.env_creator_tab), QCoreApplication.translate("EnvMaster", u"Env Creator", None))
        self.external_editor.setText(QCoreApplication.translate("EnvMaster", u"External Editor:", None))
        self.external_editor_choose.setText(QCoreApplication.translate("EnvMaster", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.options_tab), QCoreApplication.translate("EnvMaster", u"Options", None))
    # retranslateUi

