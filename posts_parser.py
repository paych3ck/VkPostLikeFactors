import vk_api
import csv
from datetime import datetime

days = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday',
    6: 'sunday'
}

access_token = ''
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()
count = 100
offset = 0
all_posts = []

while True:
    response = vk.wall.get(owner_id=265870743, count=count, offset=offset)
    all_posts.extend(response['items'])

    if len(response['items']) < count:
        break

    offset += count

with open('Sobyanin_posts_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['post_id', 'time_of_day', 'day_of_week', 'full_date' 'likes_count'])

    for post in all_posts:
        post_id = post['id']
        date_timestamp = post['date']
        date = datetime.fromtimestamp(date_timestamp)
        time_of_day = "night" if date.hour < 6 else "morning" if date.hour < 12 else "day" if date.hour < 18 else "evening"
        day_of_week = days[date.weekday()]
        full_date = date.strftime('%Y-%m-%d %H:%M:%S')
        likes_count = post['likes']['count']

        writer.writerow([post_id, time_of_day, day_of_week, full_date, likes_count])