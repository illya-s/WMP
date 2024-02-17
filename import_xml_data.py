import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WMP.settings")
django.setup()

import json
from django.utils import timezone
from index.models import Song

date = timezone.now().date()

def import_data_from_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for item in data:
            Song.objects.create(
                name = item['name'],
                text = item['text'],
                key = item['key'],
                created = date,
                updated = date
            )

if __name__ == "__main__":
    xml_file_path = r'C:\Users\Ilya\Desktop\employee.json'
    import_data_from_xml(xml_file_path)
