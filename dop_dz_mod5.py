import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f"Пользователь: {self.nickname}, возраст: {self.age}"

    def __repr__(self):
        return f"User({self.nickname}, {self.password}, {self.age})"

    def __hash__(self):
        return hash(self.password)

class Video:
    def __init__(self, title, duration, adult_mode):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return f"Видео: {self.title}, продолжительность: {self.duration} секунд"

    def __repr__(self):
        return f"Video({self.title}, {self.duration}, {self.adult_mode})"

    def __eq__(self, other):
        return self.title == other.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(video == video_ for video_ in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print(f"Просмотр видео: {video.title}")
                while video.time_now < video.duration:
                    time.sleep(1)
                    print(f"Время просмотра: {video.time_now} секунд")
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0
                break
        else:
            print(f"Видео с таким названием не найдено")

# Пример использования
if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 9, adult_mode=False)
    v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)
    ur.add(v1, v2)
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    # ur.watch_video('Для чего девушкам парень программист?')
    # ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    # ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    # print(ur.current_user)
    # ur.watch_video('Лучший язык программирования 2024 года!')
