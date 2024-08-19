import sys 
import platform
import time
from pathlib import Path
from functools import partial
from tinytag import TinyTag
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtCore import QUrl, QTimer
from View.MainWindow import Ui_MainWindow


MUSIC_DIRECTORY = f"{Path.home()}{"/" if platform.system() == "Darwin" else "\\"}Music"
DEFAULT_ALBUM_IMAGE = "Resources/Album.png"


class MainWindow(QMainWindow, Ui_MainWindow):
    playlist = []
    audio_output = QAudioOutput()
    player = QMediaPlayer()
    duration = 0
    is_muted = False
    previous_volume = 0
    current_song = 0
    slider_pressed = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(800, 400)
        self.open_button.setMaximumWidth(200)
        self.set_volume_slider()
        self.set_player_audio_output()
        self.signals_connetion()

    def set_volume_slider(self):
        self.volume_slider.setValue(50)
        self.volume_slider.setRange(0, 100)

    def set_player_audio_output(self):
        self.audio_output.setVolume(self.volume_slider.value() / 100)
        self.player.setAudioOutput(self.audio_output)

    def signals_connetion(self):
        self.open_button.clicked.connect(self.open_file)
        self.previous_button.clicked.connect(partial(QTimer.singleShot, 100, self.previous_song))
        self.play_button.clicked.connect(self.play)
        self.next_button.clicked.connect(partial(QTimer.singleShot, 100, self.next_song))
        self.volume_slider.valueChanged.connect(self.set_audio_output_volume)
        self.song_progress.sliderPressed.connect(self.slider_pressed_handler)
        self.song_progress.sliderReleased.connect(self.slider_released_handler)
        self.mute_button.clicked.connect(self.mute)
        self.player.durationChanged.connect(self.set_song_progress)
        self.player.positionChanged.connect(self.update_song_progress)
        self.player.mediaStatusChanged.connect(self.song_status_changed)

    def slider_pressed_handler(self):
        self.slider_pressed = True

    def slider_released_handler(self):
        self.slider_pressed = False
        self.player.setPosition(self.song_progress.value() * 1000)


    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open a music file", MUSIC_DIRECTORY, 
                                                "(All Songs) *.mp3 *.flac *wav *alac *.m4a")[0]
        if file_name:
            self.playlist.append(file_name)
            if self.player.source() == "":
                self.player.setSource(QUrl.fromLocalFile(file_name))
                self.play()

    def update_song_info(self):
        if TinyTag.is_supported(self.playlist[self.current_song]):
            tag = TinyTag.get(self.playlist[self.current_song], image=True)
            image = QImage()
            image_data = image.fromData(tag.get_image())
            cover_image = QPixmap.fromImage(image_data) if image_data else QPixmap(DEFAULT_ALBUM_IMAGE)
            self.song_cover.setPixmap(cover_image.scaled(500, 500))
            self.song_mini_cover.setPixmap(cover_image.scaled(100, 100))
            self.song_name_label.setText(tag.title)
            self.song_name_controls_label.setText(f"{tag.albumartist}: {tag.title}")
            self.song_album_label.setText(f"{tag.albumartist}: {tag.album}")
            self.song_quality_label.setText(f"{tag.bitdepth}bit/{round(tag.bitrate)}kbps")

    def set_audio_output_volume(self, value):
        volume = value / 100
        self.audio_output.setVolume(volume)
        if volume == 0:
            self.mute_button.setIcon(QIcon("Resources/Unmute.png"))
            self.is_muted = True
        else:
            self.mute_button.setIcon(QIcon("Resources/Mute.png"))
            self.is_muted = False

    def set_song_progress(self, duration):
        self.duration = duration // 1000
        self.song_progress.setRange(0, self.duration)

    def update_song_progress(self, position):
        position = position // 1000
        self.song_length_label.setText(time.strftime("%M:%S", time.gmtime(self.duration - position)))
        self.song_progress_label.setText(time.strftime("%M:%S", time.gmtime(position)))
        if not self.slider_pressed:
            self.song_progress.setValue(position)

    def song_status_changed(self, status):
        if status == self.player.MediaStatus.EndOfMedia:
            self.player.setPosition(self.duration)
            self.play_button.setIcon(QIcon("Resources/Play.png"))
            self.song_length_label.setText("00:00")
            QTimer.singleShot(200, self.next_song)
            

    def previous_song(self):
        try:
            self.current_song -= 1 
            if self.current_song < 0:
                self.current_song = len(self.playlist) -1
            self.player.setSource(QUrl.fromLocalFile(self.playlist[self.current_song]))
            self.play()
        except IndexError:
            QMessageBox.critical(self, "No music to play", "Please add more songs to the playlist.")

    def next_song(self):
        try:
            self.current_song += 1
            if self.current_song > len(self.playlist) -1:
                self.current_song = 0
            self.player.setSource(QUrl.fromLocalFile(self.playlist[self.current_song]))
            self.play()
        except IndexError:
            QMessageBox.critical(self, "No music to play", "Please add more songs to the playlist")

    def mute(self):
        if self.is_muted:
            self.volume_slider.setValue(self.previous_volume)
        else:
            self.previous_volume = self.volume_slider.value()
            self.volume_slider.setValue(0)
    
    def play_song(self):
        if self.player.isPlaying():
            self.player.pause()
            self.play_button.setIcon(QIcon("Resources/Play.png"))
        else:
            self.play_button.setIcon(QIcon("Resources/Pause.png"))
            self.player.play()

    def play(self):
        if len(self.playlist) > 0:
            self.play_song()
            self.update_song_info()
        else:
            QMessageBox.warning(self, "No music to play", "Please add a song to the playlist")

        

def main():
    app = QApplication(sys.argv)
    with open("Styles/styles.qss") as styles:
        app.setStyleSheet(styles.read())
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()