
class AlarmClock:
    def __init__(self):
        self.current_time = '2:30'
        self.alarm_time = '6:30'
        self.alarm_status = True
        self.alarm_toggle = ''

    def set_current_time(self):
        self.current_time = input('Time: ')
        print(self.current_time)

#toggle alarm
    def toggle_alarm(self, alarm_toggle_pass_in):
        self.alarm_toggle = alarm_toggle_pass_in
        if self.alarm_toggle == True:
            print('Alarm is active')
        else:
            print('Alarm is off')

#set alarm time
    def set_alarm_time(self):
        self.alarm_time = input('Time: ')
        print(self.alarm_time)