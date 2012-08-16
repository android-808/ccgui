from gi.repository import Gtk
import ccgui.common
import ccgui.ui
from ccgui.ui import OptionsPage

class SLSPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "SLS Mode Options")
        ccgui.ui.add_divider(self)
        ccgui.ui.add_section_title(self, "Appearance")
        
        self.nobg = ccgui.ui.add_check_button(self, "Remove background.") 
        ccgui.ui.add_wide_control(self,self.nobg)
        
        ccgui.ui.add_divider(self)
        
        ccgui.ui.add_section_title(self, "Weather")
        
        l = ccgui.ui.add_label(self, "Descriptive text.\n\nInclude some information on where to get the codes.")
        ccgui.ui.add_wide_control(self,l)

        l = ccgui.ui.add_label(self, "Area code:")
        self.area = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, self.area)
        
        ccgui.ui.add_divider(self)
        
        ccgui.ui.add_section_title(self, "GMail")
        
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)

        l = ccgui.ui.add_label(self, "Username:")
        self.gmailusername = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, self.gmailusername)
        
        l = ccgui.ui.add_label(self, "Password:")
        self.gmailpassword = ccgui.ui.add_entry(self)
        ccgui.ui.add_row(self, l, self.gmailpassword)

class SLS():
    def __init__(self, assistant):
        self.sls = SLSPage(assistant)
        
    def GetFirstPage(self):
        return self.sls.page_number
        
    def GetLastPage(self):
        return self.sls.page_number
        
    def GetOptions(self):
        ret = str(" --sls")
        if self.sls.nobg.get_active() == True:
            ret += " --nobg"
        if self.sls.area.get_text_length() > 0:
            ret += " --weather=" + self.sls.gmailusername.get_text()
        if self.sls.gmailusername.get_text_length() > 0:
            ret += " --user=" + self.sls.gmailusername.get_text()
        if self.sls.gmailpassword.get_text_length() > 0:
            ret += " --passwd=" + self.sls.gmailpassword.get_text()

        return ret
        
        
        
        
