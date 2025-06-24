# client.py

# Define your SymptomTrackerClient class here
# It should load JSON data, convert to SymptomEntry, and support filtering, exporting, etc.

class SymptomTrackerClient:
    def __init__(self, source_path='mock_api.json'):
        pass

    def get_by_date(self, date_str):
        pass

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
