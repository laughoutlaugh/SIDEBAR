import time


class MockPlayer:
    def __init__(self, songs):
        self.songs = songs

        self.current_index = 0
        self.playing = False

        self.position = 0.0
        self.duration = 180.0

        self.last_update = time.monotonic()

    @property
    def current_song(self):
        return self.songs[self.current_index]

    def play(self):
        self.playing = True
        self.last_update = time.monotonic()

    def pause(self):
        self.update()
        self.playing = False

    def toggle_play(self):
        if self.playing:
            self.pause()
        else:
            self.play()

    def next(self):
        self.current_index += 1

        if self.current_index >= len(self.songs):
            self.current_index = 0

        self.position = 0.0
        self.play()

    def previous(self):
        if self.position < 2.0: # If less than 2

            self.current_index -= 1

            if self.current_index < 0:
                self.current_index = len(self.songs) - 1

            self.position = 0.0
            self.play()

        else:
            self.position = 0.0

    def update(self):
        now = time.monotonic()

        if self.playing:
            elapsed = now - self.last_update
            self.position += elapsed

            if self.position >= self.duration:
                self.next()

        self.last_update = now

    @property
    def progress(self):
        if self.duration <= 0:
            return 0

        return self.position / self.duration