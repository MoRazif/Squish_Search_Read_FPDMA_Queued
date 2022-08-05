## Example test case GUI Automation using Squish - Open Example Trace File, search specific ATA Command - Read FPDMA Queued ##
## M.Razif 2021 ##

# -*- coding: utf-8 -*-

import names
import folder_config as fc
import os
import time

def main():
    # Handling of crash which locks the AUT from the previous test run
    try:
        os.system("taskkill /f /im SASx.exe")
    except:
        ""
    time.sleep(1)
    startApplication("SASx", "", -1, 120) # 2 minutes timeout
    #Handling of minimized SAS4 windows
    try:
        setWindowState(waitForObject(names.sASMainWindow_CSASMainWindow), WindowState.Maximize)
    except:
        ""
    clickButton(waitForObject(names.sASMainWindow_Preferences_QToolButton))
    clickButton(waitForObject(names.preferencesDialog_RestoreBtn_QPushButton))
    clickButton(waitForObject(names.sAS4_Protocol_Suite_OK_QPushButton))
    clickButton(waitForObject(names.preferencesDialog_OKBtn_QPushButton))
    clickButton(waitForObject(names.sASMainWindow_OpenFile_QToolButton))
    type(waitForObject(names.fileNameEdit_QLineEdit), fc.getExampleFolder() + r"\Traces\ATA Read_Write With SAS_STP.sxt")
    clickButton(waitForObject(names.qFileDialog_Open_QPushButton))
    clickButton(waitForObject(names.sASMainWindow_MenuButtonWidgetInToolbar_QPushButton))
    clickButton(waitForObject(names.o_AutoSuggestionSearchFilterButton_QPushButton_2))
    try:
        sendEvent("QMoveEvent", waitForObject(names.cFilterDialog_CSASFilterDialog), 246, 265, 876, 278)
    except:
        ""
    time.sleep(0.5)
    mouseClick(waitForObjectItem(names.mainWindowSplitter_FilterLineEdit_CMatchTreeView, "ATA Command"), 40, 9, Qt.NoModifier, Qt.LeftButton)
    time.sleep(0.2)
    type(waitForObject(names.mainWindowSplitter_FilterLineEdit_CMatchTreeView), "<Right>") #Per Dev. Request
    time.sleep(0.2)
    doubleClick(waitForObjectItem(names.mainWindowSplitter_FilterLineEdit_CTrafficSummaryTreeView, "ATA Command.Read FPDMA Queued"), 65, 11, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObjectItem(names.cFilterDialog_CFieldsMatchTreeView, "ATA Command.Read FPDMA Queued"), 49, 12, Qt.NoModifier, Qt.LeftButton)
    time.sleep(0.5)
    try:
        sendEvent("QMoveEvent", waitForObject(names.cSASPatternFramesDlg_CSASPatternFramesDlg), 60, 245, 469, 266)
        sendEvent("QResizeEvent", waitForObject(names.cSASPatternFramesDlg_CSASPatternFramesDlg), 1163, 436, 1237, 492)
        sendEvent("QResizeEvent", waitForObject(names.cSASPatternFramesDlg_CSASPatternFramesDlg), 1174, 436, 1248, 494)
    except:
        ""
    time.sleep(0.5)
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_19"), 44, 6, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.pSGLineEdit_CPSGLineEdit), "0008")
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_20"), 33, 7, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.pSGLineEdit_CPSGLineEdit), "0")
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_22"), 40, 7, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_25"), 65, 7, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 53, 53, 0, "5", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 57, 57, 0, "9", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 52, 52, 0, "4", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 57, 57, 0, "9", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 65, 97, 0, "a", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 51, 51, 0, "3", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 66, 98, 0, "b", False, 1)
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_26"), 42, 7, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_28"), 41, 5, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_31"), 36, 9, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_33"), 29, 8, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 49, 49, 0, "1", False, 1)
    doubleClick(waitForObjectItem(names.fieldviewtab_CSASPSGTreeView, "_34"), 31, 5, Qt.NoModifier, Qt.LeftButton)
    sendEvent("QKeyEvent", waitForObject(names.pSGLineEdit_CPSGLineEdit), QEvent.KeyPress, 48, 48, 0, "0", False, 1)
    mouseClick(waitForObject(names.fieldviewtab_CSASPSGTreeView), 165, 233, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.cSASPatternFramesDlg_OkBtn_QPushButton))
    clickButton(waitForObject(names.groupBoxType_radioButtonShow_QRadioButton))
    clickButton(waitForObject(names.cFilterDialog_RoundedPushButton_QPushButton))
    scrollTo(waitForObject(names.table_View_TableWidget_CListViewScrollBar), 194)
    openContextMenu(waitForObject(names.table_View_TableWidget_CListViewScrollBar), 6, 189, Qt.NoModifier)
    activateItem(waitForObjectItem(names.o_QMenu, "Top"))
    mouseClick(waitForObjectItem(names.table_View_TableWidget_CSASSpreadSheetWidget, "0/5"), 34, 5, Qt.NoModifier, Qt.LeftButton)
    time.sleep(0.5)
    test.compare(waitForObjectExists(names.tableWidget_0_9_QModelIndex).text, "0x60:Read FPDMA Queued ; LBA=0x000005949A3B ; Status=Incomplete ; Protocol Error=CStatusErr")
    test.compare(waitForObjectExists(names.tableWidget_0_9_QModelIndex).row, 0)
    test.compare(waitForObjectExists(names.tableWidget_0_9_QModelIndex).column, 9)
    
    # activateItem(waitForObjectItem(names.sASMainWindow_menuBar_QMenuBar, "File")) #for Jenkins
    # activateItem(waitForObjectItem(names.sASMainWindow_menuFile_QMenu, "Close Trace")) #for Jenkins
