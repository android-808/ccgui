from gi.repository import Gtk
import ccgui.common
import ccgui.ui
from ccgui.ui import OptionsPage

class CairoPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Cairo Mode Options")
        
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
        
        self.swap = ccgui.ui.add_check_button(self, "Enable swap usage monitor.")
        ccgui.ui.add_wide_control(self,self.swap)
        
        self.network = ccgui.ui.add_check_button(self, "Enable network monitor.")
        ccgui.ui.add_wide_control(self,self.network)
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Clock")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        l = ccgui.ui.add_label(self, "Clock Mode:")
        self.clockstyles = Gtk.ListStore(str, str)
        self.clockstyles.append(["Disabled", ""])
        self.clockstyles.append(["Cairo", "cairo"])
        self.clockstyles.append(["Big Cairo", "bigcairo"])
        self.clock = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.clock.set_model(self.clockstyles)
        self.clock.set_active(0)
        ccgui.ui.add_row(self, l, self.clock)
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Media Player Support")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        #Reuse options for each player.
        self.playerstyles = Gtk.ListStore(str,str)
        self.playerstyles.append(["Disabled",""])
        self.playerstyles.append(["Cairo", "cairo"])
        self.playerstyles.append(["Cairo-Case", "cairo-case"])
        self.playerstyles.append(["Cairo-CD", "cairo-cd"])
        self.playerstyles.append(["Cairo-Glassy", "cairo-glassy"])
        self.playerstyles.append(["Lua", "lua"])
        
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
 

class Cairo():
    def __init__(self, assistant):
        self.cairo = CairoPage(assistant)
        
    def GetFirstPage(self):
        return self.cairo.page_number
        
    def GetLastPage(self):
        return self.cairo.page_number
        
    def GetOptions(self):
        ret = str(" --cairo")
        ret += " --cpu=" + str(self.cairo.cpucount.get_value_as_int())
        if self.cairo.swap.get_active() == True:
            ret += " --swap"

        if self.cairo.network.get_active() == True:
            ret += " --network"
            
        if self.cairo.clock.get_active() != 0:
            tree_iter = self.cairo.clock.get_active_iter()
            ret += " --clock=" + self.cairo.clockstyles[tree_iter][1]
            
        if self.cairo.banshee.get_active() != 0:
            tree_iter = self.cairo.banshee.get_active_iter()
            ret += " --banshee=" + self.cairo.playerstyles[tree_iter][1]
        
        if self.cairo.clementine.get_active() != 0:
            tree_iter = self.cairo.clementine.get_active_iter()
            ret += " --clementine=" + self.cairo.playerstyles[tree_iter][1]

        if self.cairo.rhythmbox.get_active() != 0:
            tree_iter = self.cairo.rhythmbox.get_active_iter()
            ret += " --rhythmbox=" + self.cairo.playerstyles[tree_iter][1]
        

        return ret
        
        
        
        
