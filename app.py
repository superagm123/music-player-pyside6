import sys 
import platform
import time
from pathlib import Path
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import QTimer
from View.MainWindow import Ui_MainWindow
from Model.MusicPlayer import MusicPlayer


MUSIC_DIRECTORY = f"{Path.home()}{"/" if platform.system() == "Darwin" else "\\"}Music"
DEFAULT_ALBUM_IMAGE = "Resources/Album.png"


class MainWindow(QMainWindow, Ui_MainWindow):
    is_muted = False
    previous_volume = 0 
    duration = 0
    is_song_progress_pressed = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(800, 400)
        self.music_player = MusicPlayer()
        self.open_button.setMaximumWidth(200)
        self.set_signals_connection()
        self.set_volume_slider()

    def set_signals_connection(self):
        self.open_button.clicked.connect(self.load_file)
        self.previous_button.clicked.connect(partial(QTimer.singleShot, 100, self.play_previous))
        self.play_button.clicked.connect(self.play)
        self.next_button.clicked.connect(partial(QTimer.singleShot, 100, self.play_next))
        self.music_player.signals.songInfoChanged.connect(self.update_song_info)
        self.music_player.signals.songDurationChanged.connect(self.update_song_duration)
        self.music_player.signals.songPositionChanged.connect(self.update_song_position)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.mute_button.clicked.connect(self.mute)
        self.song_progress.sliderPressed.connect(self.song_progress_pressed)
        self.song_progress.sliderReleased.connect(self.song_progress_released)

    def set_volume_slider(self):
        self.volume_slider.setValue(50)
        self.volume_slider.setRange(0, 100)

    def check_player_state(self):
        state = self.music_player.get_player_state()
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.play_button.setIcon(QIcon("Resources/Pause.png"))
        else:
            self.play_button.setIcon(QIcon("Resources/Play.png"))


    def load_file(self):
        song_file = QFileDialog.getOpenFileName(self, "Open a music file", MUSIC_DIRECTORY, 
                                                "All Files(*) *.mp3 *.flac *wav *alac *.m4a") [0]
        if song_file:
            self.music_player.set_music_source(song_file)
            self.check_player_state()

    def update_song_info(self, tag: object):
        if tag:
            image_data = QImage.fromData(tag.get_image())
            cover_image = QPixmap(image_data) if image_data else QPixmap(DEFAULT_ALBUM_IMAGE)
            self.song_cover.setPixmap(cover_image.scaled(500, 500))
            self.song_mini_cover.setPixmap(cover_image.scaled(100, 100))
            self.song_name_label.setText(tag.title)
            self.song_name_controls_label.setText(f"{tag.albumartist}: {tag.title}")
            self.song_album_label.setText(f"{tag.albumartist}: {tag.album}")
            self.song_quality_label.setText(f"{tag.bitdepth}bit/{round(tag.bitrate)}kbps")

    def update_song_duration(self, duration):
        self.duration = duration
        self.song_progress.setRange(0, duration)

    def update_song_position(self, position):
        self.song_length_label.setText(time.strftime("%M:%S", time.gmtime(self.duration - position)))
        self.song_progress_label.setText(time.strftime("%M:%S", time.gmtime(position)))
        if not self.is_song_progress_pressed:
            self.song_progress.setValue(position)

    def play_previous(self):
        self.music_player.play_previous_song()

    def play(self):
       self.music_player.play()
       self.check_player_state()

    def play_next(self):
        self.music_player.play_next_song()
    
    def mute(self):
        if self.is_muted:
            self.volume_slider.setValue(self.previous_volume)
        else:
            self.previous_volume = self.volume_slider.value()
            self.volume_slider.setValue(0)

    def set_volume(self, volume):
        volume = volume / 100
        self.music_player.set_audio_output_volume(volume)
        if volume == 0:
            self.mute_button.setIcon(QIcon("Resources/Unmute.png"))
            self.is_muted = True
        else:
            self.mute_button.setIcon(QIcon("Resources/Mute.png"))
            self.is_muted = False

    def song_progress_pressed(self):
        self.is_song_progress_pressed = True

    def song_progress_released(self):
        self.is_song_progress_pressed = False
        self.music_player.set_player_position(self.song_progress.value() * 1000)


def main():
    app = QApplication(sys.argv)
    with open("Styles/styles.qss") as styles:
        app.setStyleSheet(styles.read())
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()