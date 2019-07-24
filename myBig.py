# @Time   : 2019/7/24 12:30
# @Author : jackman

class Big(object):
    def __init__(self, x, y):
        x = list(str(x))
        y = list(str(y))
        for i in range(len(x) // 2):
            x[i], x[len(x) - 1 - i] = x[len(x) - 1 - i], x[i]
        for j in range(len(y) // 2):
            y[j], y[len(y) - 1 - j] = y[len(y) - 1 - j], y[j]
        self.x = x
        self.y = y

    def add(self):
        x_point = y_point = point = 0
        sum = [0 for i in range((max(len(self.x), len(self.y))) + 1)]

        big = (self.x if len(self.x) > len(self.y) else self.y)
        while x_point < len(self.x) and y_point < len(self.y):
            if int(self.x[x_point]) + int(self.y[y_point]) >= 10:
                sum[point] += (int(self.x[x_point]) + int(self.y[y_point]) - 10)
                sum[point + 1] += 1
            else:
                sum[point] += (int(self.x[x_point]) + int(self.y[y_point]))
            if sum[point] >= 10:
                sum[point] -= 10
                sum[point + 1] += 1
            point += 1
            x_point += 1
            y_point += 1
        while point < len(big):
            sum[point] += int(big[point])
            if sum[point] >= 10:
                sum[point] -= 10
                sum[point + 1] += 1
            point += 1
        if sum[-1] == 0:
            sum.pop()

        return ''.join([str(i) for i in sum[::-1]])

    def mul(self):
        x_point = y_point = point = 0
        sum = [0 for i in range((max(len(self.x), len(self.y))) * 2)]
        for i in range(len(self.y)):
            for j in range(len(self.x)):
                sum[i + j] += int(self.y[i]) * int(self.x[j])
        for i in range(len(sum)):
            if sum[i] >= 10:
                sum[i + 1] += sum[i] // 10
                sum[i] %= 10
        while sum[-1] == 0:
            sum.pop()
        return ''.join([str(i) for i in sum[::-1]])


if __name__ == '__main__':
    big = Big(999999999999999999, 2)
    result1 = big.add()
    result2 = big.mul()
    print(result1, result2)
