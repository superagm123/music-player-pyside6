from tinytag import TinyTag
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtCore import QUrl, QTimer, Slot
from Model.Signals import MusicPlayerSignals


class MusicPlayer(QWidget):
    __playlist = []
    __audio_output =  QAudioOutput()
    __player = QMediaPlayer()
    __current_song = 0

    def __init__(self):
        super().__init__()
        self.__setup_player()
        self.__set_signals_connection()
        self.signals = MusicPlayerSignals()

    def __setup_player(self):
        self.__audio_output.setVolume(50)
        self.__player.setAudioOutput(self.__audio_output)

    def __set_signals_connection(self):
        self.__player.durationChanged.connect(self.__song_duration_changed)
        self.__player.positionChanged.connect(self.__song_position_changed)
        self.__player.mediaStatusChanged.connect(self.__song_status_changed)
        self.__player.errorOccurred.connect(lambda error: print(error))
    
    @Slot()
    def __song_duration_changed(self, duration):
        duration = duration // 1000
        self.signals.songDurationChanged.emit(duration)
    
    @Slot()
    def __song_position_changed(self, position):
        position = position // 1000
        self.signals.songPositionChanged.emit(position)

    def __song_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.__player.setPosition(0)
            QTimer.singleShot(100, self.play_next_song)

    @Slot()
    def __get_song_info(self):
        if TinyTag.is_supported(self.__playlist[self.__current_song]):
            tag = TinyTag.get(self.__playlist[self.__current_song], image=True)
            self.signals.songInfoChanged.emit(tag)
            

    def __show_error(self):
        QMessageBox.warning(self, "No music to play", "Please add a song to the playlist")

    def set_music_source(self, song: str):
        if song not in self.__playlist:
            self.__playlist.append(song)
        else:
            QMessageBox.warning(self, "Song already in the playlist", "You can't add a song to the playlist twice")
        if self.__player.source() == "":
            self.__player.setSource(QUrl.fromLocalFile(song))
            self.play()
            self.__player.setPosition(0)
    
    def play_previous_song(self):
        try:
            self.__current_song -= 1
            if self.__current_song < 0:
                self.__current_song = len(self.__playlist) - 1
            self.__player.setSource(QUrl.fromLocalFile(self.__playlist[self.__current_song]))
            self.play()
        except IndexError:
            self.__show_error()

    def play(self):
        if len(self.__playlist) > 0:
            if self.__player.isPlaying():
                self.__player.pause()
            else:
                self.__player.play()
                self.__get_song_info()
        else:
            self.__show_error()

    def play_next_song(self):
        try:
            self.__current_song += 1
            if self.__current_song > len(self.__playlist) -1:
                self.__current_song = 0
            self.__player.setSource(QUrl.fromLocalFile(self.__playlist[self.__current_song]))
            self.play()
        except IndexError:
            self.__show_error()

    def set_audio_output_volume(self, volume: float):
        self.__audio_output.setVolume(volume)

    def set_player_position(self, position: int):
        self.__player.setPosition(position)
    
    def get_player_state(self):
        return self.__player.playbackState()