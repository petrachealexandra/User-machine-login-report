#event date for logins and logouts

def get_event_date(event):
  return event.date

#current users by addint logins and corresponding logouts
def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif (event.type == "logout"):
      try:
        machines[event.machine].remove(event.user)
      except KeyError:
        print("Current event - machine name '{}', type '{}', date '{}', user '{}' - has no corresponding login event.".format(event.machine, event.type, event.date, event.user))
        break
        #handling errors with logout only events and no corresponding logins
  return machines

#generate report with current logged in users
def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("Currently logged-in users are: '{}'' on these machines: '{}'.".format(user_list, machine))

#class for handling events:
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

#samples data:
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

#testing the function and error handling:

users = current_users(events)
print(users)

#generating report
generate_report(users)