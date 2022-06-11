
class AlarmClock:
    def __init__(self):
        self.current_time = '2:30'
        self.alarm_time = '6:30'
        self.alarm_status = ''

    def set_current_time(self):
        self.current_time = input('Time: ')
        print(self.current_time)

#toggle alarm
    def toggle_alarm(self, alarm_toggle):
        if self.alarm_status == True:
            print('Alarm is active')
        else:
            print('Alarm is off')

#set alarm time
    def set_alarm_time(self):
        self.alarm_time = input('Time: ')
        print(self.alarm_time)