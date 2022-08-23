class Stats():
    '''отслеживание статистики'''
    def __init__(self):
        '''инициализирует статистику'''
        self.reset_stats()
        self.run_game = True
        with open('record.txt', 'r') as f:
            self.hight_score = int(f.readline())

    def reset_stats(self):
        '''статистика изменяющаяся во время игры'''
        self.gans_left = 2
        self.score = 0