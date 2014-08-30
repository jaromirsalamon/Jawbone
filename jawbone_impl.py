from jawbone import Jawbone
import csv
import datetime
import urllib


code = 'aV1SI82xvTp7yNo9mcqXNzAMdEzLI7j65MDz9woxiPz7xAtMk3eVufj10-ItJz4R9WnvKI-GaClbU4JadEd7yCHvFlpwU6ifgf1sDnoQ8zQXdB24evV0_J9g7lSkKu4wpmp8xnxzsxVNWa81PUm-HX1RJ4nRH1zRl5cyeb8zhWTk8lNHm2EhXTlQUbAogm-8'

jb = Jawbone()

url = jb.doAuth()
print(url)

access_token = jb.getAccessToken(code)
print(access_token)

#me = jb.api_call(access_token, '/nudge/api/users/@me')
#print(me)

#xid = jb.getUserId(access_token)
#print(xid)

moves = jb.doApiCall(access_token, '/nudge/api/users/@me/moves')

move_items = moves['data']['items']
move_counts = moves['data']['size']

x = []

print(move_counts)
for move in move_items: 
    for day_hour_id in move['details']['hourly_totals']:
        x.append({'time_updated': datetime.datetime.fromtimestamp(move['time_updated']).strftime('%Y-%m-%d %H:%M:%S'),
              'xid': move['xid'],
              'title': move['title'],
              'type': move['type'],
              'time_created': datetime.datetime.fromtimestamp(move['time_created']).strftime('%Y-%m-%d %H:%M:%S'),
              'time_completed': datetime.datetime.fromtimestamp(move['time_completed']).strftime('%Y-%m-%d %H:%M:%S'),
              'date': move['date'],
              'snapshot_image':move['snapshot_image'],
              'distance': move['details']['distance'],
              'wo_active_time': move['details']['wo_active_time'], #datetime.datetime.fromtimestamp(move['details']['wo_active_time']).strftime('%H:%M:%S'),
              'tz': move['details']['tz'],
              'active_time': datetime.datetime.fromtimestamp(move['details']['active_time']).strftime('%H:%M:%S'),
              'inactive_time': datetime.datetime.fromtimestamp(move['details']['inactive_time']).strftime('%H:%M:%S'),
              'longest_idle': datetime.datetime.fromtimestamp(move['details']['longest_idle']).strftime('%H:%M:%S'),
              'calories': move['details']['calories'],
              'wo_count': move['details']['wo_count'],
              'wo_longest': move['details']['wo_longest'],
              'bmr': move['details']['bmr'],
              'bg_calories': move['details']['bg_calories'],
              'steps': move['details']['steps'],
              'km': move['details']['km'],
              'wo_calories': move['details']['wo_calories'],
              'bmr_day': move['details']['bmr_day'],
              'day_hour_id': day_hour_id,
              'hourly_distance': move['details']['hourly_totals'][day_hour_id]['distance'],
              'hourly_active_time': datetime.datetime.fromtimestamp(move['details']['hourly_totals'][day_hour_id]['active_time']).strftime('%H:%M:%S'),
              'hourly_calories': move['details']['hourly_totals'][day_hour_id]['calories'],
              'hourly_steps': move['details']['hourly_totals'][day_hour_id]['steps'],
              'hourly_longest_idle_time': datetime.datetime.fromtimestamp(move['details']['hourly_totals'][day_hour_id]['longest_idle_time']).strftime('%H:%M:%S'),
              'hourly_inactive_time': datetime.datetime.fromtimestamp(move['details']['hourly_totals'][day_hour_id]['inactive_time']).strftime('%H:%M:%S'),
              'hourly_longest_active_time': datetime.datetime.fromtimestamp(move['details']['hourly_totals'][day_hour_id]['longest_active_time']).strftime('%H:%M:%S')
              }
             )

f = csv.writer(open('data/csv/moves.csv', 'wb+'))

f.writerow(x[0].keys())
x = sorted(x)

print(x[0].keys())
for item in x:
    f.writerow(item.values())
    print(item.values())
    urllib.urlretrieve('https://jawbone.com/' + item['snapshot_image'], 'images/'+str(item['date'])+'.png')

#moves_detail = jb.api_call(j['access_token'], '/nudge/api/moves/q2ECdXazI-46Lmf4bhJQGA')
#print(moves_detail)

#moves_graph =  jb.api_call(j['access_token'], '/nudge/api/moves/q2ECdXazI-46Lmf4bhJQGA/image')
#print(moves_graph)

#moves_ticks =  jb.api_call(j['access_token'], '/nudge/api/moves/q2ECdXazI-46Lmf4bhJQGA/ticks')
#print(moves_ticks)