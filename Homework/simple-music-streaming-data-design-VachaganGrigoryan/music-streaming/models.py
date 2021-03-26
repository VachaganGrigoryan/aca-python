from datetime import datetime
from pathlib import Path
from random import randint


class User:
    USER_ID = 0
    file_path = './data/users.txt'

    def __init__(self, first_name: str, last_name: str, email: str, password: str,
                 profile_pic: str = None, birth_date: datetime = None, level: int = 0):
        self.id = User.USER_ID
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.profile_pic = profile_pic
        self.birth_date = birth_date
        self.level = level
        User.USER_ID += 1

    def validate_user(self):
        # method which should check if not optional fields are not None and email is valid email,\
        #  and password at least has:
        #  at least 8 characters,
        #  both uppercase and lowercase letters, numbers
        #  at least one special character, e.g., ! @ # ? ]
        pass

    def create_playlist(self, name):
        Playlist(name, datetime.now(), self.id, self.profile_pic).save()

    def delete_playlist(self, name):
        with open(Path(Playlist.file_path), 'r+') as file:
            file_lines = []
            for play_list in file:
                data = eval(play_list)
                if name != data.get('name'):
                    file_lines.append(play_list)
            file.writelines(file_lines)

    def save(self):
        with open(Path(self.file_path), 'w') as file:
            file.write(f'{self.__dict__}\n')


class Artist(User):
    file_path = './data/artists.txt'

    def __init__(self, first_name: str, last_name: str, email: str, password: str, about: str, listeners_count: int,
                 profile_pic: str = None, birth_date: datetime = None, level: int = 0):
        super(User, self).__init__(first_name, last_name, email, password, profile_pic, birth_date, level)
        self.about = about
        self.listeners_count = listeners_count

    def add_song(self, title: str, artist_name: str, file: str):
        # for now file argument should be just file's path on your computer
        Song(title, artist_name, randint(1, 10), "genre", datetime.year, self.id, self.listeners_count, f'Album<{title}>').save()

    def delete_song(self, song_id):
        with open(Path(Song.file_path), 'r+') as file:
            file_lines = []
            for song_list in file:
                data = eval(song_list)
                if song_id != data.get('id'):
                    file_lines.append(song_list)
            file.writelines(file_lines)

    def create_album(self, title, label, year, list_of_song_url=[]):
        Album(title, datetime.now(), self.id, self.profile_pic, label, year).save()

    def delete_album(self, album_id):
        with open(Path(Album.file_path), 'r+') as file:
            file_lines = []
            for album_list in file:
                data = eval(album_list)
                if album_id != data.get('id'):
                    file_lines.append(album_list)
            file.writelines(file_lines)

    def save(self):
        with open(Path(self.file_path), 'w') as file:
            file.write(f'{self.__dict__}\n')


class Song:
    SONG_ID = 0
    file_path = './data/songs.txt'

    # duration: int  # seconds
    # album: album if no album created default create album with same nam as song ( for singles)

    def __init__(self, title: str, artist: str, duration: int, genre: str, year: int,
                 created_by: Artist, streams_count: int,
                 album: "album if no album created default create album with same name as song (for singles)"):
        self.id = Song.SONG_ID
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.year = year
        self.created_by = created_by
        self.streams_count = streams_count
        self.album = album
        Song.SONG_ID += 1

    def validate(self):
        # if created_by is not an Artist objects raise Exception('Access denied.')
        pass

    def add_to_playlist(self, playlist, user):
        PlaylistSong(playlist, self, datetime.now())

    def remove_from_playlist(self, playlist, user):
        pass

    def play(self, user):  # if already exists stop previous track
        pass

    def stop(self, user):  # increment sream count if played 30 seconds at least
        pass

    def download(self):  # returns song path for now
        pass

    def save(self):
        with open(Path(self.file_path), 'w') as file:
            file.write(f'{self.__dict__}\n')


class Playlist:
    PLAYLIST_ID = 0
    file_path = './data/play_lists.txt'

    def __init__(self, name: str, date_added: datetime, created_by: User, picture_url: "picture_url"):
        self.id = Playlist.PLAYLIST_ID
        self.name = name
        self.date_added = date_added
        self.created_by = created_by
        self.picture_url = picture_url
        Playlist.PLAYLIST_ID += 1

    @property
    def count_of_songs(self):
        return

    @property
    def duration_of_playlist(self):
        return

    @property
    def genre_list(self):
        return

    def play(self):  # play all tracks in playlist in order added_date
        pass

    def stop(self):
        pass

    def save(self):
        with open(Path(self.file_path), 'w') as file:
            file.write(f'{self.__dict__}\n')


class Album(Playlist):
    file_path = './data/albums.txt'

    def __init__(self, name: str, date_added: datetime, created_by: User, picture_url: "picture_url", label: str,
                 year: str):
        super(Playlist, self).__init__(name, date_added, created_by, picture_url)
        self.label = label
        self.year = year

    def validate(self):
        # if created_by is not Artist object raise Exception('Access denied.')
        pass

    def save(self):
        with open(Path(self.file_path), 'w') as file:
            file.write(f'{self.__dict__}\n')


class SongPlays:
    SONG_PLAYS_ID = 0
    file_path = './data/song_plays.txt'

    def __init__(self, user: User, song: Song, start_timestamp: float):
        self.id = SongPlays.SONG_PLAYS_ID
        self.user = user
        self.song = song
        self.start_timestamp = start_timestamp

    def save(self):
        with open(Path(self.file_path), 'w') as file:
            file.write(f'{self.__dict__}\n')


class PlaylistSong:
    file_path = './data/play_list_songs.txt'
    # (this class should help to find out song's playlists and playlist's songs)

    def __init__(self, playlist: Playlist, song: Song, date_added: datetime):
        self.playlist = playlist
        self.song = song
        self.date_added = date_added

    def save(self):
        with open(Path(self.file_path), 'w') as file:
            file.write(f'{self.__dict__}\n')

# Change classes I decribe above as follows: all classes should have
#
# file_path: file where you should save your onjects.__ dict__ info
# save all objects in ./data/classname.txt files
#
# methods:
# --save(self) should save __ dict__ of objects in file_path as one line
#
# --update(self, ** kwargs): update fields from kwargs if there is any keyword that object cass doesn't have raise
# Exceptions('{class name} does't have field_1, field_2, ...., use fields from {list of available fields name}) and
# dict in file_path
#
# --delete(self) should delete current onjects from file_path if exist else raise Exception('No {class name} objects
# founded')
#
# --@staticmethod --filter(** kwargs) should find all "dict" in file_path which have all key values from kwargs and
# return corresponding objects
#
# example: Song.filter(title='Over and over', genre='Alternative') should return all song objects that hase title
# 'Over and over' and genre 'Alternative'
#
# --@staticmethod --get(** kwargs) should find a "dict" in file_path which have all key values from kwargs and return
# corresponding object, if there is multiple objects raise Exception('Multiple {class name} objects founded') if
# there is no dict in file raise Exception('No {class name} objects founded')
#
# Hint: to generate id use uuid3 method of uuid python module and pass uniq string that decribe your object
#
# Create test.py file and create unittests for your models and test all methods
#
# Hint for testing in setUp method create different file path to save your testing objects and in teardown function
# delete testing file


if __name__ == '__main__':

    # user = User("Vachagan", "Grigoryan", "vachagan.grigoryan@outlook.com", "qwerty")
    # user.save()
    # artist = Artist("Vachagan", "Grigoryan", "vachagan.grigoryan@outlook.com", "qwerty", "The best Artist", 56)
    # artist.save()

    def countBits(n: int):
        return n.bit_length()

    print(countBits(50))

    "".capitalize()
