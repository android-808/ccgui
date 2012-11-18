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
        
        l = ccgui.ui.add_label(self, "Number of CPU cores:")
        #l.set_margin_left(18)
        adjustment = Gtk.Adjustment(1, 1, 16, 1, 4, 0)
        self.cpucount = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        self.cpucount.set_adjustment(adjustment)
        ccgui.ui.add_row(self, l, self.cpucount)

        self.network = ccgui.ui.add_check_button(self, "Enable network monitor.")
        ccgui.ui.add_wide_control(self,self.network)
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Media Player Support")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        #Reuse options for each player.
        self.playerstyles = Gtk.ListStore(str, str)
        self.playerstyles.append(["Disabled", ""])
        self.playerstyles.append(["Ring", "ring"])
        self.playerstyles.append(["Ring-Case", "ring-case"])
        self.playerstyles.append(["Ring-CD", "ring-cd"])
        self.playerstyles.append(["Ring-Glassy", "ring-glassy"])
        
        l = ccgui.ui.add_label(self, "Banshee:")
        self.banshee = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                        hexpand=True)
        self.banshee.set_model(self.playerstyles)
        self.banshee.set_active(0)
        ccgui.ui.add_row(self, l, self.banshee)
        
        l = ccgui.ui.add_label(self, "Clementine:")
        self.clementine = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                           hexpand=True)
        self.clementine.set_model(self.playerstyles)
        self.clementine.set_active(0)
        ccgui.ui.add_row(self, l, self.clementine)
        
        l = ccgui.ui.add_label(self, "Rhythmbox:")
        self.rhythmbox = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                         hexpand=True)
        self.rhythmbox.set_model(self.playerstyles)
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
        ret = str(" --ring")
        ret += " --cpu=" + str(self.ring.cpucount.get_value_as_int())
        
        if self.ring.network.get_active() == True:
            ret += " --network"
            
        if self.ring.banshee.get_active() != 0:
            tree_iter = self.ring.banshee.get_active_iter()
            ret += " --banshee=" + self.ring.playerstyles[tree_iter][1]
        
        if self.ring.clementine.get_active() != 0:
            tree_iter = self.ring.clementine.get_active_iter()
            ret += " --clementine=" + self.ring.playerstyles[tree_iter][1]

        if self.ring.rhythmbox.get_active() != 0:
            tree_iter = self.ring.rhythmbox.get_active_iter()
            ret += " --rhythmbox=" + self.ring.playerstyles[tree_iter][1]
        
        return ret

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

