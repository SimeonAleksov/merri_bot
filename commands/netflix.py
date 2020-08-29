from commands.base_command import BaseCommand
import json
import random
from utils import get_emoji


def filter_mv(n):
    with open("C:\\Users\\Simeon\\PycharmProjects\\scraper\\netflix\\final\\new_releases.json", 'r',
              encoding='utf-8') as f:
        data = json.load(f)
    return list(filter(lambda x: True if x["is_movie"] == n else False, data))


def filter_by_genre(genre):
    with open("C:\\Users\\Simeon\\PycharmProjects\\scraper\\data\\scraped_json\\netflix\\netflix.json", 'r',
              encoding='utf-8') as f:
        data = json.load(f)
    return list(filter(lambda x: True if genre in x["genre"].lower() else False, data))


class flix(BaseCommand):
    def __init__(self):
        description = "New netflix releases today"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        if params[0] == 'today':
            with open("C:\\Users\\Simeon\\PycharmProjects\\scraper\\netflix\\final\\new_releases.json", 'r',
                      encoding='utf-8') as f:
                data = json.load(f)
            final_data = {each['series_source_id']: each for each in data}.values()
            msg = ""
            final_data = filter_mv(1)
            for obj in final_data:
                msg += f"Title: {obj['series_title']} \n" \
                       f"Movie? {'Nah' if obj['is_movie'] == 0 else 'Yeh'} \n" \
                       f"Genres: {obj['genre']}" \
                       f"" \
                       f"Link: <{obj['series_url'] if not obj['is_movie'] else obj['program_url']}> \n" \
                       f"--------------------------------------------\n"

            final_data = filter_mv(0)
            final_data = {each['series_source_id']: each for each in final_data}.values()
            for obj in final_data:
                msg += f"Title: {obj['series_title']} \n" \
                       f"Movie? {'Nah' if obj['is_movie'] == 0 else 'Yeh'} \n" \
                       f"Genres: {obj['genre']} \n" \
                       f"" \
                       f"Link: <{obj['series_url'] if not obj['is_movie'] else obj['program_url']}> \n" \
                       f"--------------------------------------------\n"
            await message.channel.send(msg)
        elif params[0] != 'today':
            comedies = filter_by_genre(params[0])
            random_title = random.choice(comedies)
            msg = f"Title: {random_title['series_title']} \n" \
                  f"Movie? {'Nah' if random_title['is_movie'] == 0 else 'Yeh'} \n" \
                  f"Link: <{random_title['series_url'] if not random_title['is_movie'] else random_title['program_url']}> \n" \
                  f"Genres: {random_title['genre']} \n" \
                  f"{get_emoji(':face_with_monocle:')}"
            await message.channel.send(msg)
