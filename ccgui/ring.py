from gi.repository import Gtk
import ccgui.common
import ccgui.ui
from ccgui.ui import OptionsPage

class RingPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Ring Mode Options")
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "System")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        l = ccgui.ui.add_label(self, "CPU core selector")
        ccgui.ui.add_wide_control(self,l)
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Media Player Support")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        #Reuse options for each player.
        playermodes = Gtk.ListStore(str)
        playermodes.append(["Disabled"])
        playermodes.append(["Ring"])
        playermodes.append(["Ring-Case"])
        playermodes.append(["Ring-CD"])
        playermodes.append(["Ring-Glassy"])
        
        l = ccgui.ui.add_label(self, "Banshee:")
        self.banshee = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                        hexpand=True)
        self.banshee.set_model(playermodes)
        self.banshee.set_active(0)
        ccgui.ui.add_row(self, l, self.banshee)
        
        l = ccgui.ui.add_label(self, "Clementine:")
        self.clementine = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                           hexpand=True)
        self.clementine.set_model(playermodes)
        self.clementine.set_active(0)
        ccgui.ui.add_row(self, l, self.clementine)
        
        l = ccgui.ui.add_label(self, "Rhythmbox:")
        self.rhythmbox = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                         hexpand=True)
        self.rhythmbox.set_model(playermodes)
        self.rhythmbox.set_active(0)
        ccgui.ui.add_row(self, l, self.rhythmbox)
 

class Ring():
    def __init__(self, assistant):
        self.ring = RingPage(assistant)
        
    def GetFirstPage(self):
        return self.ring.page_number
        
    def GetLastPage(self):
        return self.ring.page_number
        
    def GetOptions(self):
        ret = str()

        return ret
        
        
        
        
