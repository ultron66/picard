# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PluginsOptionsPage(object):
    def setupUi(self, PluginsOptionsPage):
        PluginsOptionsPage.setObjectName(_fromUtf8("PluginsOptionsPage"))
        PluginsOptionsPage.resize(513, 312)
        self.vboxlayout = QtGui.QVBoxLayout(PluginsOptionsPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.plugins_container = QtGui.QSplitter(PluginsOptionsPage)
        self.plugins_container.setEnabled(True)
        self.plugins_container.setOrientation(QtCore.Qt.Vertical)
        self.plugins_container.setHandleWidth(2)
        self.plugins_container.setObjectName(_fromUtf8("plugins_container"))
        self.groupBox_2 = QtGui.QGroupBox(self.plugins_container)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.plugins = QtGui.QTreeWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plugins.sizePolicy().hasHeightForWidth())
        self.plugins.setSizePolicy(sizePolicy)
        self.plugins.setAcceptDrops(True)
        self.plugins.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.plugins.setRootIsDecorated(False)
        self.plugins.setObjectName(_fromUtf8("plugins"))
        self.vboxlayout1.addWidget(self.plugins)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.install_plugin = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.install_plugin.sizePolicy().hasHeightForWidth())
        self.install_plugin.setSizePolicy(sizePolicy)
        self.install_plugin.setObjectName(_fromUtf8("install_plugin"))
        self.horizontalLayout.addWidget(self.install_plugin)
        self.folder_open = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_open.sizePolicy().hasHeightForWidth())
        self.folder_open.setSizePolicy(sizePolicy)
        self.folder_open.setObjectName(_fromUtf8("folder_open"))
        self.horizontalLayout.addWidget(self.folder_open)
        self.reload_list_of_plugins = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_list_of_plugins.sizePolicy().hasHeightForWidth())
        self.reload_list_of_plugins.setSizePolicy(sizePolicy)
        self.reload_list_of_plugins.setObjectName(_fromUtf8("reload_list_of_plugins"))
        self.horizontalLayout.addWidget(self.reload_list_of_plugins)
        self.vboxlayout1.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(self.plugins_container)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout2.setSpacing(0)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtGui.QFrame.HLine)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 76))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 6, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.details = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy)
        self.details.setMinimumSize(QtCore.QSize(0, 0))
        self.details.setFrameShape(QtGui.QFrame.Box)
        self.details.setLineWidth(0)
        self.details.setText(_fromUtf8(""))
        self.details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.details.setWordWrap(True)
        self.details.setIndent(0)
        self.details.setOpenExternalLinks(True)
        self.details.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.details.setObjectName(_fromUtf8("details"))
        self.verticalLayout.addWidget(self.details)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.vboxlayout2.addWidget(self.scrollArea)
        self.vboxlayout.addWidget(self.plugins_container)

        self.retranslateUi(PluginsOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(PluginsOptionsPage)

    def retranslateUi(self, PluginsOptionsPage):
        self.groupBox_2.setTitle(_("Plugins"))
        self.plugins.headerItem().setText(0, _("Name"))
        self.plugins.headerItem().setText(1, _("Version"))
        self.plugins.headerItem().setText(2, _("Status"))
        self.install_plugin.setText(_("Install plugin..."))
        self.folder_open.setText(_("Open plugin folder"))
        self.reload_list_of_plugins.setText(_("Reload List of Plugins"))
        self.groupBox.setTitle(_("Details"))

