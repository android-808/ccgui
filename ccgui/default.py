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
        
        self.processmonitor = ccgui.ui.add_check_button(self, "Enable process monitor.")
        ccgui.ui.add_wide_control(self,self.processmonitor)
        
        l = ccgui.ui.add_label(self, "Number of processes:")
        #l.set_margin_left(18)
        adjustment = Gtk.Adjustment(1, 1, 10, 1, 4, 0)
        self.processcount = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        self.processcount.set_adjustment(adjustment)
        ccgui.ui.add_row(self, l, self.processcount)
        
class DesktopPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Desktop")
        
        l = ccgui.ui.add_label(self, "This allows you to specify desktop specific options.")
        ccgui.ui.add_wide_control(self,l)
        
        self.replacelogo = ccgui.ui.add_check_button(self, "Replace monitor icon with distribution/desktop logo.")
        ccgui.ui.add_wide_control(self,self.replacelogo)
        
        l = ccgui.ui.add_label(self, "Distribution/Desktop:")
        self.icons = Gtk.ListStore(str, str)

        self.icons.append(["Arch", " --arch"])
        self.icons.append(["Debian", " --debian"])
        self.icons.append(["Fedora", " --fedora"])
        self.icons.append(["Gentoo", " --gentoo"])
        self.icons.append(["Gnome", " --gnome"])
        #self.icons.append(["KDE", "--kde"])
        self.icons.append(["OpenSUSE", " --opensuse"])
        self.icons.append(["Pardus", " --pardus"])
        self.icons.append(["Ubuntu", " --ubuntu"])
        self.icons.append(["XFCE", " --xfce"])
 
        
        self.icon = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                                   hexpand=True)
        self.icon.set_model(self.icons)
        self.icon.set_active(0)
        ccgui.ui.add_row(self, l, self.icon)

class DateTimePage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Date/Time Settings")
        
        l = ccgui.ui.add_wrapped_label(self, "This option will completely remove the \"Date\" section, removing all clocks, "
                                     "date and calendar displays.")
        ccgui.ui.add_wide_control(self,l)
        
        self.nodata = ccgui.ui.add_check_button(self, "Disable \"Date\" section.") 
        ccgui.ui.add_wide_control(self, self.nodata)
        
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Clock")
        l = ccgui.ui.add_label(self, "Disabling the clock will still show todays date.")
        ccgui.ui.add_wide_control(self,l)
        
        
        l = ccgui.ui.add_label(self, "Clock Mode:")
        self.clockstyles = Gtk.ListStore(str, str)
        self.clockstyles.append(["Disabled", "off"])
        self.clockstyles.append(["Classic", "classic"])
        self.clockstyles.append(["Default", "default"])
        self.clockstyles.append(["Digital", "digital"])
        self.clockstyles.append(["Lucky", "lucky"])
        self.clockstyles.append(["Modern", "modern"])
        self.clockstyles.append(["Slim", "slim"])
        self.clock = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.clock.set_model(self.clockstyles)
        self.clock.set_active(2)
        ccgui.ui.add_row(self, l, self.clock)
        
        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Calendar")
        l = ccgui.ui.add_label(self, "This feature will show a calendar displaying the current month.")
        ccgui.ui.add_wide_control(self,l)
        
        
        l = ccgui.ui.add_label(self, "Calendar Mode:")
        self.calendarstyles = Gtk.ListStore(str, str)
        self.calendarstyles.append(["Disabled", ""])
        self.calendarstyles.append(["Enabled", " --calendar"])
        self.calendarstyles.append(["Enabled with Monday as first day", " --calendarm"])
        self.calendarstyles.append(["Enabled with Zim support", " --calendarzim"])
        self.calendar = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.calendar.set_model(self.calendarstyles)
        self.calendar.set_active(0)
        ccgui.ui.add_row(self, l, self.calendar)


        ccgui.ui.add_divider(self)        
        ccgui.ui.add_section_title(self, "Task List")
        l = ccgui.ui.add_wrapped_label(self, "This feature allows you to display a basic to-do list within the conky display.\n"
                                             "Type \"ct help\" in to a terminal window for more information.")
        ccgui.ui.add_wide_control(self,l)   
        self.task = ccgui.ui.add_check_button(self, "Enable task list.") 
        ccgui.ui.add_wide_control(self, self.task)

class MediaPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Photo Display")
        l = ccgui.ui.add_label(self, "This feature will display an image. EXPAND.")
        ccgui.ui.add_wide_control(self,l)
        
        
        l = ccgui.ui.add_label(self, "Photo Mode:")
        self.photostyles = Gtk.ListStore(str, str)
        self.photostyles.append(["Disabled", ""])
        self.photostyles.append(["Enabled", " --photo"])
        self.photostyles.append(["Enabled in random mode", " --photord"])
        self.photo = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.photo.set_model(self.photostyles)
        self.photo.set_active(0)
        ccgui.ui.add_row(self, l, self.photo)

        ccgui.ui.add_divider(self)

        ccgui.ui.add_section_title(self, "Media Player Support")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)

        self.mpd = ccgui.ui.add_check_button(self, "Enable MPD support.") 
        ccgui.ui.add_wide_control(self, self.mpd)

        #Reuse options for each player.
        self.playerstyles = Gtk.ListStore(str, str)
        self.playerstyles.append(["Disabled", ""])
        self.playerstyles.append(["Case", "case"])
        self.playerstyles.append(["CD", "cd"])
        self.playerstyles.append(["Default", "default"])
        self.playerstyles.append(["Glassy", "glassy"])
        self.playerstyles.append(["Old Vinyl", "oldvinyl"])
        self.playerstyles.append(["Simple", "simple"])
        self.playerstyles.append(["Vinyl", "vinyl"])
        
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

        self.covergloobus = ccgui.ui.add_check_button(self, "Enable CoverGloobus support.") 
        ccgui.ui.add_wide_control(self, self.covergloobus)
     
     
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
        self.desktop = DesktopPage(assistant)
        self.datetime = DateTimePage(assistant)
        self.media = MediaPage(assistant)
        
    def GetFirstPage(self):
        return self.system.page_number
        
    def GetLastPage(self):
        return self.media.page_number
        
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
            
        # Desktop
        if self.desktop.replacelogo.get_active() != 0:
            tree_iter = self.desktop.icon.get_active_iter()
            ret += self.desktop.icons[tree_iter][1]
        
        return ret
        
        
        
        
