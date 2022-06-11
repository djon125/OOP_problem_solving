from alarm import AlarmClock


DionAlarm =AlarmClock()
print(DionAlarm.current_time)
#DionAlarm.set_current_time()
DionAlarm.toggle_alarm(False)
DionAlarm.set_alarm_time()