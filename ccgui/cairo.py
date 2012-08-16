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
        
        l = ccgui.ui.add_label(self, "CPU core selector")
        ccgui.ui.add_wide_control(self,l)
        
        self.swap = ccgui.ui.add_check_button(self, "Enable swap usage monitor.")
        ccgui.ui.add_wide_control(self,self.swap)
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Clock")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        l = ccgui.ui.add_label(self, "Clock Mode:")
        modes = Gtk.ListStore(str)
        modes.append(["Disabled"])
        modes.append(["Cairo"])
        modes.append(["Big Cairo"])
        self.clock = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.clock.set_model(modes)
        self.clock.set_active(0)
        ccgui.ui.add_row(self, l, self.clock)
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Media Player Support")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)
        
        #Reuse options for each player.
        playermodes = Gtk.ListStore(str)
        playermodes.append(["Disabled"])
        playermodes.append(["Cairo"])
        playermodes.append(["Cairo-Case"])
        playermodes.append(["Cairo-CD"])
        playermodes.append(["Cairo-Glassy"])
        playermodes.append(["Lua"])
        
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
 

class Cairo():
    def __init__(self, assistant):
        self.cairo = CairoPage(assistant)
        
    def GetFirstPage(self):
        return self.cairo.page_number
        
    def GetLastPage(self):
        return self.cairo.page_number
        
    def GetOptions(self):
        ret = str()

        return ret
        
        
        
        
