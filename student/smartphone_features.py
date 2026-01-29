class Camera:
    def camera_feature(self):
        print("Camera: 48MP")


class MusicPlayer:
    def music_feature(self):
        print("Music Player: Stereo Sound")


class Smartphone(Camera, MusicPlayer):
    def display(self):
        self.camera_feature()
        self.music_feature()


p = Smartphone()
p.display()
