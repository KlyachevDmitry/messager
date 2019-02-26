import random


def rsa():
    return RSA()


class RSA:
    def __init__(self):
        self.open_key, self.closed_key = self.generate_keys()
        self.open_key_other_user = []

        #massages = [1, 2, 3, 1, 5, 7]
        #crypt_massage = self.crypt_massages(massages, self.open_key)
        #print(crypt_massage)
        #decrypt_massage = self.decrypt_massages(crypt_massage, self.closed_key)
        #print(decrypt_massage)

    @staticmethod
    def all_simples_number_from_n():
        """найдем все простые чисела до числа 512"""
        # len_number_check = input("n=")
        len_number_check = 512
        lst = [2]
        for i in range(3, len_number_check + 1, 2):
            if (i > 10) and (i % 10 == 5):
                continue
            for j in lst:
                if j * j - 1 > i:
                    lst.append(i)
                    break
                if i % j == 0:
                    break
            else:
                lst.append(i)
        return lst

    @staticmethod
    def to_binary(n):
        """разбивает число на бинарный массив"""
        r = []
        while n > 0:
            r.append(n % 2)
            n /= 2
            return r

    def method_miller_rabin(self, n, s=50):
        """Метод Миллера Рабина"""
        for j in range(1, s + 1):
                a = random.randint(1, n - 1)
                b = self.to_binary(n - 1)
                d = 1
                for i in range(len(b) - 1, -1, -1):
                    x = d
                    d = (d * d) % n
                    if d == 1 and x != 1 and x != n - 1:
                        return True  # Составное
                    if b[i] == 1:
                        d = (d * a) % n
                        if d != 1:
                            return True  # Составное
                        return False  # Простое

    @staticmethod
    def is_prime(n):
        """
        Miller-Rabin primality test.

        A return value of False means n is certainly not prime. A return value of
        True means n is very likely a prime.
        """
        if n != int(n):
            return False
        n = int(n)
        if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
            return False
        if n == 2 or n == 3 or n == 5 or n == 7:
            return True
        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        assert (2 ** s * d == n - 1)

        def trial_composite(random_number):
            if pow(random_number, d, n) == 1:
                return False
            for i in range(s):
                if pow(random_number, 2 ** i * d, n) == n - 1:
                    return False
            return True

        for i in range(8):  # number of trials
            random_number = random.randrange(2, n)
            if trial_composite(random_number):
                return False
        return True

    def generate_simple_number(self, lst, digit_number):
        """Генерирует простое случайное число"""
        while True:
            simple_number_probable = random.getrandbits(digit_number)   # generate *bit number
            for i in lst:
                if simple_number_probable % i == 0:     # проверяем делимость на первые 97 простых чисел до 512
                    break
            else:
                if self.is_prime(simple_number_probable):
                    return simple_number_probable

    def generate_keys(self):
        """ Generating key for encode"""
        lst = self.all_simples_number_from_n()
        p = self.generate_simple_number(lst, 150)
        q = self.generate_simple_number(lst, 150)
        n = p * q  # module
        fi = (p - 1) * (q - 1)  # func Eyler
        e = 65537  # open EXPonent(1.simple, 2.e<fi, 3.e vzaimno prostoe s fi)
        open_key = [e, n]
        d = self.modular_inverse(e, fi)
        closed_key = [d, n]
        return open_key, closed_key
    
    @staticmethod
    def encrypt_256(massage, open_key):
        """encode part massage"""
        #print('-------------', massage, open_key)
        crypting = (massage**open_key[0]) % open_key[1]   # massage<n, else don't work
        return crypting
    
    @staticmethod
    def decrypt_256(massage, closed_key):
        """decode part massage"""
        encrypting = pow(massage, closed_key[0], closed_key[1])
        return encrypting

    def egcd(self, a, b):
        """gcd"""
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modular_inverse(self, a, m):
        """modular inverse"""
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def crypt_massages(self, massages, open_key):
        """encode massage"""
        for i in range(len(massages)):
            crypt_massage_ = self.encrypt_256(massages[i], open_key)
            massages[i] = crypt_massage_
        return massages

    def decrypt_massages(self, crypt_massage, closed_key):
        """decode massage"""
        for i in range(len(crypt_massage)):
            crypt_massage_ = self.decrypt_256(crypt_massage[i], closed_key)
            crypt_massage[i] = crypt_massage_
        return crypt_massage


rsa()

# def mainRSA():
#     open_key, closed_key = generate_keys()
#     massages = [1, 2, 3, 1, 5, 7]
#     crypt_massage=crypt_massages(massages, open_key)
#     decrypt_massage=decrypt_massages(crypt_massage, closed_key)
#     print(decrypt_massage)

# if __name__ == "__main__":
#     mainRSA()

#
# def gcdex(a, b):
#     if b == 0:
#         return a, 1, 0
#     else:
#         d, x, y = gcdex(b, a % b)
#         return d, y, x - y * (a // b)

