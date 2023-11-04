class video:
    def __init__(
        self, URL, Channel, Subscribers, Title, Likes, Duration, Views, Comments
    ):
        self.URL = URL
        self.Channel = Channel
        self.Subscribers = Subscribers
        self.Title = Title
        self.Likes = Likes
        self.Duration = Duration
        self.Views = Views
        self.Comments = Comments

    def Validate(self):
        try:
            self.Comments = int(self.Comments)
        except ValueError:
            self.Comments = 0
        try:
            self.Likes = int(self.Likes)
        except ValueError:
            self.Likes = 0
        try:
            self.Views = int(self.Views)
        except ValueError:
            self.Views = 0
        try:
            self.Subscribers = int(self.Subscribers)
        except ValueError:
            self.Subscribers = 0
        self.Duration = "0:0" if self.Duration == "NA" else self.Duration
        self.Duration = self.Duration_conversion(self.Duration)

    def Duration_conversion(self, Duration):
        count = 0
        time = 0
        for i in Duration:
            if i == ":":
                count += 1
        if count > 0:
            Duration = Duration.split(":")
            if count == 2:
                time = (
                    int(Duration[0]) * 3600 + int(Duration[1]) * 60 + int(Duration[2])
                )
            else:
                time = int(Duration[0]) * 60 + int(Duration[1])
        return time
