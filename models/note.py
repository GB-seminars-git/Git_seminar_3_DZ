class Note:
    def __init__(self, title, message):
        self.id = None
        self.title = title
        self.message = message
        self.created_date = None
        self.updated_date = None

    def add_id(self, note_id):
        self.id = note_id

    def created_at_date(self, times_created):
        self.created_date = times_created

    def updated_at_date(self, time_updated):
        self.updated_date = time_updated

    def __str__(self):
        return f"{self.id}. {self.title}\n {self.message}\n дата создания: {self.created_date}\n " \
               f"дата последнего изменения: {self.updated_date}\n"
