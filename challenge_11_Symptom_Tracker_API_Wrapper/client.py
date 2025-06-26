# client.py

# Define your SymptomTrackerClient class here
import json
from datetime import datetime
from symptom_entry import SymptomEntry
# It should load JSON data, convert to SymptomEntry, and support filtering, exporting, etc.

class SymptomTrackerClient:
    def __init__(self, source_path='mock_api.json'):
        self.entries = []
        with open(source_path, 'r') as file:
            data = json.load(file)

        for item in data['results']:
            entry = SymptomEntry(
                date=datetime.strptime(item['date'], '%Y-%m-%d'),
                symptoms=item['symptoms'],
                severity=item['severity'],
                notes=item.get('notes'),
            )
            self.entries.append(entry)

    def get_by_date(self, date_str):
        target_date = datetime.strptime()

    def filter_by_severity(self, min_level):
        pass

    def to_dataframe(self):
        pass

    @property
    def entry_count(self):
        pass

    @property
    def latest_entry(self):
        pass
