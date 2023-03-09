class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = self._check_coord(x)
        self._y = self._check_coord(x)
        self._length = length
        self._is_move = True
        self._cells = [1 for _ in range(self._length)]
        self._tp = tp

    def _check_coord(self, coord):
        if not isinstance(coord, int) or coord <0:
            raise ValueError('Неверная координата')
        return coord

    def set_start_coords(self,x,y):
        pass

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        pass

    def is_vollide(self, ship):
        pass

    def is_out_pole(self, size):
        pass

    def __setitem__(self, key, value):
        if not 0 <= key <= len(self._length):
            raise IndexError('Неверный индекс')
        if value not in (1, 2):
            raise ValueError('Неверное значение')
        self._cells[key] = value

    def __getitem__(self, item):
        if not 0 <= item <= len(self._length):
            raise IndexError('Неверный индекс')
        return self._cells[item]



class GamePole:
    ...