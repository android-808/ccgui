from gi.repository import Gtk
import ccgui.common
import ccgui.ui
from ccgui.ui import OptionsPage

class SystemPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "System Information")
        
        l = ccgui.ui.add_label(self, "Configures system usage reporting.")
        ccgui.ui.add_wide_control(self,l)
        
        self.cpu = ccgui.ui.add_check_button(self, "Enable CPU usage monitor.")
        self.cpu.connect("toggled", self.on_cpu_toggled)        
        ccgui.ui.add_wide_control(self,self.cpu)
        
        l = ccgui.ui.add_label(self, "Number of CPU cores:")
        adjustment = Gtk.Adjustment(1, 1, 16, 1, 4, 0)
        self.cpucount = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        self.cpucount.set_adjustment(adjustment)
        self.cpucount.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.cpucount)
                
        self.cputemp = ccgui.ui.add_check_button(self, "Enable CPU temperature monitoring.")
        ccgui.ui.add_wide_control(self,self.cputemp)
                
        self.swap = ccgui.ui.add_check_button(self, "Enable swap usage monitor.")
        ccgui.ui.add_wide_control(self,self.swap)
        
        self.processmonitor = ccgui.ui.add_check_button(self, "Enable process monitor.")
        self.processmonitor.connect("toggled", self.on_process_toggled) 
        ccgui.ui.add_wide_control(self,self.processmonitor)
        
        l = ccgui.ui.add_label(self, "Number of processes:")
        #l.set_margin_left(18)
        adjustment = Gtk.Adjustment(1, 1, 10, 1, 4, 0)
        self.processcount = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        self.processcount.set_adjustment(adjustment)
        self.processcount.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.processcount)

        ccgui.ui.add_divider(self)
        ccgui.ui.add_section_title(self, "Battery Information")

        l = ccgui.ui.add_label(self, "Reports battery status using /sys/class/power_supply/BAT#")
        ccgui.ui.add_wide_control(self,l)

        self.battery = ccgui.ui.add_check_button(self, "Enable battery monitor.")
        self.battery.connect("toggled", self.on_battery_toggled) 
        ccgui.ui.add_wide_control(self,self.battery)

        l = ccgui.ui.add_label(self, "Battery to monitor:")
        self.batteryx = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        batadjustment = Gtk.Adjustment(0, 0, 10, 1, 4, 0)        
        self.batteryx.set_adjustment(batadjustment)
        self.batteryx.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.batteryx)

        ccgui.ui.add_divider(self)
        ccgui.ui.add_section_title(self, "NVidia GPU Information")
        l = ccgui.ui.add_label(self, "Displays temperature, frequency, memory and driver version.")
        ccgui.ui.add_wide_control(self,l)        
        self.nvidia = ccgui.ui.add_check_button(self, "Enable NVidia GPU information.")
        ccgui.ui.add_wide_control(self, self.nvidia)

    def on_cpu_toggled(self, button):
        self.cpucount.set_sensitive(button.get_active())

    def on_process_toggled(self, button):
        self.processcount.set_sensitive(button.get_active())

    def on_battery_toggled(self, button):
        self.batteryx.set_sensitive(button.get_active())

class DesktopPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Appearance")
        
        l = ccgui.ui.add_label(self, "This allows you to specify desktop specific options.")
        ccgui.ui.add_wide_control(self,l)

        l = ccgui.ui.add_label(self, "Side of the screen to display Conky:")
        self.sides = Gtk.ListStore(str, str)

        self.sides.append(["Left", "left"])
        self.sides.append(["Right", "right"])
        self.side = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                                   hexpand=True)
        self.side.set_model(self.sides)
        self.side.set_active(1)
        ccgui.ui.add_row(self, l, self.side)
        
        self.replacelogo = ccgui.ui.add_check_button(self, "Replace monitor icon with distribution/desktop logo.")
        self.replacelogo.connect("toggled", self.on_logo_toggled) 
        ccgui.ui.add_wide_control(self,self.replacelogo)
        
        l = ccgui.ui.add_label(self, "Distribution/Desktop:")
        self.icons = Gtk.ListStore(str, str)

        self.icons.append(["Arch", " --arch"])
        self.icons.append(["Debian", " --debian"])
        self.icons.append(["Fedora", " --fedora"])
        self.icons.append(["Gentoo", " --gentoo"])
        self.icons.append(["Gnome", " --gnome"])
        self.icons.append(["KDE", "--kde"])
        self.icons.append(["OpenSUSE", " --opensuse"])
        self.icons.append(["Pardus", " --pardus"])
        self.icons.append(["Ubuntu", " --ubuntu"])
        self.icons.append(["XFCE", " --xfce"])
 
        
        self.icon = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                                   hexpand=True)
        self.icon.set_model(self.icons)
        self.icon.set_active(0)
        self.icon.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.icon)

        ccgui.ui.add_divider(self)
        ccgui.ui.add_section_title(self, "Updates")
        l = ccgui.ui.add_label(self, "Displays the total number of updates available to be installed.")
        ccgui.ui.add_wide_control(self,l)   
        
        l = ccgui.ui.add_label(self, "<b>Note:</b> only currently only supports apt-get based systems (Debian/Ubuntu).")
        ccgui.ui.add_wide_control(self,l)  

        self.updates = ccgui.ui.add_check_button(self, "Show number of available updates.")
        ccgui.ui.add_wide_control(self,self.updates) 

    def on_logo_toggled(self, button):
        self.icon.set_sensitive(button.get_active())

class DateTimePage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Date/Time Settings")
        
        l = ccgui.ui.add_wrapped_label(self, "This option will completely remove the \"Date\" section, removing all clocks, "
                                     "date and calendar displays.")
        ccgui.ui.add_wide_control(self,l)
        
        self.nodata = ccgui.ui.add_check_button(self, "Disable \"Date\" section.")
        self.nodata.connect("toggled", self.on_date_toggled)
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
        l = ccgui.ui.add_wrapped_label(self, "This feature allows you to display a basic to-do list within the Conky display.\n"
                                             "Type \"ct help\" in to a terminal window for more information.")
        ccgui.ui.add_wide_control(self,l)   
        self.task = ccgui.ui.add_check_button(self, "Enable task list.") 
        ccgui.ui.add_wide_control(self, self.task)

    def on_date_toggled(self, button):
        if button.get_active() == True:
            state = False
        else:
            state = True
        self.clock.set_sensitive(state)
        self.calendar.set_sensitive(state)
        self.task.set_sensitive(state)

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

        self.mpd = ccgui.ui.add_check_button(self, "Enable MPD support.") 
        ccgui.ui.add_wide_control(self, self.mpd)

        self.covergloobus = ccgui.ui.add_check_button(self, "Enable CoverGloobus support.") 
        ccgui.ui.add_wide_control(self, self.covergloobus)

class HDDPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)

        ccgui.ui.add_section_title(self, "HDD Usage Monitoring")
        l = ccgui.ui.add_label(self, "Feature explanation")
        ccgui.ui.add_wide_control(self,l)

        l = ccgui.ui.add_label(self, "HDD Mode:")
        self.hddstyles = Gtk.ListStore(str, str)
        self.hddstyles.append(["Disabled", ""])
        self.hddstyles.append(["Default", "default"])
        self.hddstyles.append(["Meerkat", "meerkat"])
        self.hddstyles.append(["Mix", "mix"])
        self.hddstyles.append(["Simple", "simple"])
        self.hdd = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.hdd.set_model(self.hddstyles)
        self.hdd.set_active(0)
        self.hdd.connect("changed", self.on_hdd_changed)
        ccgui.ui.add_row(self, l, self.hdd)

        ccgui.ui.add_divider(self)
        ccgui.ui.add_section_title(self, "HDD Temperature Monitoring")
        l = ccgui.ui.add_label(self, "Feature explanation (NOT IMPLEMENTED)")
        ccgui.ui.add_wide_control(self,l)

        self.hddtemp = ccgui.ui.add_check_button(self, "Enable HDD temperature monitoring.")
        self.hddtemp.connect("toggled", self.on_hddtemp_toggled)
        self.hddtemp.set_sensitive(False)
        ccgui.ui.add_wide_control(self,self.hddtemp)

        l = ccgui.ui.add_label(self, "HDD Temperature 1:")
        self.hdtemp1 = ccgui.ui.add_entry(self)
        self.hdtemp1.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.hdtemp1)
        l = ccgui.ui.add_label(self, "HDD Temperature 2:")
        self.hdtemp2 = ccgui.ui.add_entry(self)
        self.hdtemp2.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.hdtemp2)
        l = ccgui.ui.add_label(self, "HDD Temperature 3:")
        self.hdtemp3 = ccgui.ui.add_entry(self)
        self.hdtemp3.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.hdtemp3)
        l = ccgui.ui.add_label(self, "HDD Temperature 4:")
        self.hdtemp4 = ccgui.ui.add_entry(self)
        self.hdtemp4.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.hdtemp4)

    def on_hdd_changed(self, button):
        if self.hdd.get_active() != 0:
            self.hddtemp.set_sensitive(True)
            state = self.hddtemp.get_active()
            self.hdtemp1.set_sensitive(state)
            self.hdtemp2.set_sensitive(state)
            self.hdtemp3.set_sensitive(state)
            self.hdtemp4.set_sensitive(state)
        else:
            self.hddtemp.set_sensitive(False)
            self.hdtemp1.set_sensitive(False)
            self.hdtemp2.set_sensitive(False)
            self.hdtemp3.set_sensitive(False)
            self.hdtemp4.set_sensitive(False)

    def on_hddtemp_toggled(self, button):
        state = button.get_active()
        self.hdtemp1.set_sensitive(state)
        self.hdtemp2.set_sensitive(state)
        self.hdtemp3.set_sensitive(state)
        self.hdtemp4.set_sensitive(state)
         
class NetworkPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Network Monitoring")
        l = ccgui.ui.add_label(self, "Descriptive text")
        ccgui.ui.add_wide_control(self,l)

        self.network = ccgui.ui.add_check_button(self, "Enable network monitoring.") 
        self.network.connect("toggled", self.on_network_toggled)
        ccgui.ui.add_wide_control(self, self.network)

        l = ccgui.ui.add_label(self, "Change default device number:")
        ccgui.ui.add_wide_control(self,l)

        
        l = ccgui.ui.add_label(self, "Ethernet (/dev/ethX):")
        self.ethx = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        ethadjustment = Gtk.Adjustment(0, 0, 10, 1, 4, 0)        
        self.ethx.set_adjustment(ethadjustment)
        self.ethx.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.ethx)

        l = ccgui.ui.add_label(self, "Wireless (/dev/wlanX):")
        self.wlanx = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        wlanadjustment = Gtk.Adjustment(0, 0, 10, 1, 4, 0)
        self.wlanx.set_adjustment(wlanadjustment)
        self.wlanx.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.wlanx)

        l = ccgui.ui.add_label(self, "PPP/3G Modem (/dev/pppX):")
        self.pppx = Gtk.SpinButton(halign = Gtk.Align.START, hexpand = True)
        pppadjustment = Gtk.Adjustment(0, 0, 10, 1, 4, 0)
        self.pppx.set_adjustment(pppadjustment)
        self.pppx.set_sensitive(False)        
        ccgui.ui.add_row(self, l, self.pppx)        

        ccgui.ui.add_divider(self)
        ccgui.ui.add_section_title(self, "GMail")
        
        l = ccgui.ui.add_label(self, "Reports the number of new messages in the specified account.\n\n<b>Warning:</b> Details are stored in plain text!")
        ccgui.ui.add_wide_control(self,l)

        self.gmail = ccgui.ui.add_check_button(self, "Enable GMail support.")
        self.gmail.connect("toggled", self.on_gmail_toggled)
        ccgui.ui.add_wide_control(self, self.gmail)
        
        l = ccgui.ui.add_label(self, "Username:")
        self.username = ccgui.ui.add_entry(self)
        self.username.set_sensitive(False)        
        ccgui.ui.add_row(self, l, self.username)
        
        l = ccgui.ui.add_label(self, "Password:")
        self.password = ccgui.ui.add_entry(self)
        self.password.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.password)

    def on_network_toggled(self, button):
        state = button.get_active()
        self.ethx.set_sensitive(state)
        self.wlanx.set_sensitive(state)
        self.pppx.set_sensitive(state)

    def on_gmail_toggled(self, button):
        state = button.get_active()
        self.username.set_sensitive(state)
        self.password.set_sensitive(state)
        
class WeatherPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Weather")
        
        l = ccgui.ui.add_label(self, "Descriptive text.\n\nInclude some information on where to get the codes.")
        ccgui.ui.add_wide_control(self,l)

        l = ccgui.ui.add_label(self, "Weather Mode:")
        self.weatherprovider = Gtk.ListStore(str, str)
        self.weatherprovider.append(["Disabled", ""])
        self.weatherprovider.append(["BBC Weather", " --bbcweather"])
        self.weatherprovider.append(["Yahoo Weather", " --weather"])
        self.weather = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.weather.set_model(self.weatherprovider)
        self.weather.set_active(0)
        self.weather.connect("changed", self.on_weather_changed)
        ccgui.ui.add_row(self, l, self.weather)
        
        l = ccgui.ui.add_label(self, "Area code:")
        self.area = ccgui.ui.add_entry(self)
        self.area.set_sensitive(False)
        ccgui.ui.add_row(self, l, self.area)

    def on_weather_changed(self, button):
        if self.weather.get_active() != 0:
            self.area.set_sensitive(True)
        else:
            self.area.set_sensitive(False)

class Default():
    def __init__(self, assistant):
        self.system   = SystemPage(assistant)
        self.desktop  = DesktopPage(assistant)
        self.datetime = DateTimePage(assistant)
        self.media    = MediaPage(assistant)
        self.hdd      = HDDPage(assistant)
        self.network  = NetworkPage(assistant)
        self.weather  = WeatherPage(assistant)
        
    def GetFirstPage(self):
        return self.system.page_number
        
    def GetLastPage(self):
        return self.weather.page_number
        
    def GetOptions(self):
        ret = str()
        # System Information
        if self.system.cpu.get_active() == True:
            ret += " --cpu=" + str(self.system.cpucount.get_value_as_int())
        if self.system.cputemp.get_active() == True:
            ret += " --cputemp"
        if self.system.swap.get_active() == True:
            ret += " --swap"
        if self.system.processmonitor.get_active() == True:
            ret += " --proc=" + str(self.system.processcount.get_value_as_int())
        # Battery Information        
        if self.system.battery.get_active() == True:
            ret += " --battery"
            ret += " --battery-value=" + str(self.system.batteryx.get_value_as_int())
        # Nvidia
        if self.system.nvidia.get_active() == True:
            ret += " --nvidia"   
        
        # Desktop
        tree_iter = self.desktop.side.get_active_iter()
        ret += " --side=" + self.desktop.sides[tree_iter][1]

        if self.desktop.replacelogo.get_active() != 0:
            tree_iter = self.desktop.icon.get_active_iter()
            ret += self.desktop.icons[tree_iter][1]

        if self.desktop.updates.get_active() == True:
            ret += " --updates"
        
        # Date/Time
        if self.datetime.nodata.get_active() == True:
            ret += " --nodata"
        else:
            tree_iter = self.datetime.clock.get_active_iter()
            ret += " --clock=" + self.datetime.clockstyles[tree_iter][1]        
            
            if self.datetime.calendar.get_active() != 0:
                tree_iter = self.datetime.calendar.get_active_iter()
                ret += self.datetime.calendarstyles[tree_iter][1]
            if self.datetime.task.get_active() == True:
                ret += " --task"

        # Media Support
        tree_iter = self.media.photo.get_active_iter()
        ret += self.media.photostyles[tree_iter][1]  

        if self.media.banshee.get_active() != 0:
            tree_iter = self.media.banshee.get_active_iter()
            ret += " --banshee=" + self.media.playerstyles[tree_iter][1]
        if self.media.clementine.get_active() != 0:
            tree_iter = self.media.clementine.get_active_iter()
            ret += " --clementine=" + self.media.playerstyles[tree_iter][1]
        if self.media.rhythmbox.get_active() != 0:
            tree_iter = self.media.rhythmbox.get_active_iter()
            ret += " --banshee=" + self.media.playerstyles[tree_iter][1]
        if self.media.mpd.get_active() == True:
            ret += " --mpd" 
        if self.media.covergloobus.get_active() == True:
            ret += " --covergloobus" 

        # HDD
        if self.hdd.hdd.get_active() == True:
            tree_iter = self.hdd.hdd.get_active_iter()
            ret += " --hdd=" + self.hdd.hddstyles[tree_iter][1]

        # Network
        if self.network.network.get_active() == True:
            ret += " --network"
            ret += " --ethx=" + str(self.network.ethx.get_value_as_int())
            ret += " --wlanx=" + str(self.network.wlanx.get_value_as_int())
            ret += " --pppx=" + str(self.network.pppx.get_value_as_int())

        if self.network.gmail.get_active() == True:
            ret += " --gmail"            
            ret += " --username=" + self.network.username.get_text()
            ret += " --password=" + self.network.password.get_text()

        # Finally, Weather
        if self.weather.weather.get_active() != 0:
            tree_iter = self.weather.weather.get_active_iter()
            ret += self.weather.weatherprovider[tree_iter][1] + "=" + self.weather.area.get_text()

        return ret
        
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
