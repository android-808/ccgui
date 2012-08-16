from gi.repository import Gtk
import ccgui.common
import ccgui.ui
from ccgui.ui import OptionsPage

"""
Board Mode
"""
class BoardPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Board/SLIM Mode Options")
        ccgui.ui.add_divider(self)
        ccgui.ui.add_section_title(self, "Appearance")
        
        l = ccgui.ui.add_label(self, "Screen width:")
        self.screenwidth = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, self.screenwidth)
        
        l = ccgui.ui.add_label(self, "Screen height:")
        self.screenheight = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, self.screenheight)
        
        self.nobg = ccgui.ui.add_check_button(self, "Remove background.") 
        ccgui.ui.add_wide_control(self, self.nobg)
        
        l = ccgui.ui.add_label(self, "Fix ring position:")
        self.ringpos = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, self.ringpos)
        
        ccgui.ui.add_divider(self)
        
        ccgui.ui.add_section_title(self, "Weather")
        
        l = ccgui.ui.add_label(self, "Descriptive text.\n\nInclude some information on where to get the codes.")
        ccgui.ui.add_wide_control(self,l)

        w = ccgui.ui.add_check_button(self, "Enable weather support.") 
        ccgui.ui.add_wide_control(self,w)
        
        l = ccgui.ui.add_label(self, "Area code:")
        w = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, w)

class Board():
    def __init__(self, assistant):
        self.board = BoardPage(assistant)
        
    def GetFirstPage(self):
        return self.board.page_number
        
    def GetLastPage(self):
        return self.board.page_number
        
    def GetOptions(self):
        ret = str()
        ret += " --w=" + self.system.board.screenwidth.get_value()
        #if self.system.cputemp.get_active() == True:
        #    ret += " --cputemp"
        #if self.system.swap.get_active() == True:
        #    ret += " --swap"
        #if self.system.battery.get_active() == True:
        #    ret += " --battery"
        return ret
        
        
        
        
