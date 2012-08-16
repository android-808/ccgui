from gi.repository import Gtk
import ccgui.common
import ccgui.ui
from ccgui.ui import OptionsPage

class SystemPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "System")
        
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        self.cpu = ccgui.ui.add_check_button(self, "Enable CPU usage monitor.")
        ccgui.ui.add_wide_control(self,self.cpu)
        
        l = ccgui.ui.add_label(self, "Number of CPU cores:")
        #l.set_margin_left(18)
        adjustment = Gtk.Adjustment(1, 1, 16, 1, 4, 0)
        self.cpucount = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        self.cpucount.set_adjustment(adjustment)
        ccgui.ui.add_row(self, l, self.cpucount)
        
        
        self.cputemp = ccgui.ui.add_check_button(self, "Enable CPU temperature monitoring.")
        ccgui.ui.add_wide_control(self,self.cputemp)
                
        self.swap = ccgui.ui.add_check_button(self, "Enable swap usage monitor.")
        ccgui.ui.add_wide_control(self,self.swap)
        
        self.battery = ccgui.ui.add_check_button(self, "Enable battery monitor.")
        ccgui.ui.add_wide_control(self,self.battery)
     
class GMailPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "GMail")
        
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)

        w = ccgui.ui.add_check_button(self, "Enable GMail support.") 
        ccgui.ui.add_wide_control(self,w)
        
        l = ccgui.ui.add_label(self, "Username:")
        w = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, w)
        
        l = ccgui.ui.add_label(self, "Password:")
        w = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, w)
        
class WeatherPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Weather")
        
        l = ccgui.ui.add_label(self, "Descriptive text.\n\nInclude some information on where to get the codes.")
        ccgui.ui.add_wide_control(self,l)

        w = ccgui.ui.add_check_button(self, "Enable weather support.") 
        ccgui.ui.add_wide_control(self,w)
        
        l = ccgui.ui.add_label(self, "Area code:")
        w = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, w)   

class Default():
    def __init__(self, assistant):
        self.system = SystemPage(assistant)
        
    def GetFirstPage(self):
        return self.system.page_number
        
    def GetLastPage(self):
        return self.system.page_number
        
    def GetOptions(self):
        ret = str()
        if self.system.cpu.get_active() == True:
            ret += " --cpu=" + str(self.system.cpucount.get_value_as_int())
        if self.system.cputemp.get_active() == True:
            ret += " --cputemp"
        if self.system.swap.get_active() == True:
            ret += " --swap"
        if self.system.battery.get_active() == True:
            ret += " --battery"
        return ret
        
        
        
        
