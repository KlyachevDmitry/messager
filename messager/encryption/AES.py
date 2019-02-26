import random
#from encryption.RSA import rsa
from copy import copy
#message_data='qweиtyuiasfgfgf'.encode('utf-8')
message_data='Codewars is an educational community for computer programming. On the platform, software developers train on programming challenges known as kata.[1][2] These discrete programming exercises train a variety of skills in a variety of programming languages, and are completed within an online IDE.'.encode('utf-8')


def aes(server_flag):
    return AES(server_flag)


class AES:
    def __init__(self, server_flag, block=4):
        self.block = block
        self.ROUND_KEYS = []
        self.ROUND_KEYS_COPY = []

    def generate_round_keys(self):
        self.ROUND_KEYS = self.key_expansion_aes()
        self.ROUND_KEYS_COPY = copy(self.ROUND_KEYS)

        #self.open_key, self.closed_key = rsa().generate_keys()

        #crypt_key_aes = rsa().crypt_massages(self.ROUND_KEYS_COPY, self.open_key)
        #self.message_data = message_data
        #Decrypt_key_aes = rsa().decrypt_massages(crypt_key_aes, self.closed_key)
        # self.code_data = self.crashing_message()
        # for i in self.code_data:
        #     self.coding(i, 10)
        #     self.decoding(i,  10)
        #Full_Encrypt_Massage=crypt_key_aes + self.connect_massage(self.code_data)
        # message_data = bytes(self.code_data).decode('utf-8')
        # print(message_data)

    @staticmethod
    def crashing_message(message_data):   #crashing can be done better
        message_data = list(message_data)
        print(message_data)
        code_data = []
        package = int(len(message_data)/16)
        if len(message_data) % 16 != 0:
            package += 1
            message_data += ([0]*(16-(len(message_data)-(len(message_data)//16)*16)))  # method '%' don't work
        for i in range(package):
            code_data += [message_data[i*16:i*16+16]]
        return code_data

    @staticmethod
    def sub_bytes(frame):
        frame_ = list(frame)
        sub_bytes = [
                0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
                0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
                0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
                0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
                0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
                0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
                0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
                0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
                0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
                0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
                0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
                0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
                0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
                0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
                0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
                0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
                ]

        for i in range(16):
            frame[i] = sub_bytes[frame_[i]]
        return frame

    @staticmethod
    def rotate(word, n):
        return word[n:]+word[0:n]

    def shift_rows(self, code_data):
        for i in range(1, 4):
            code_data[i * 4:i * 4 + 4] = self.rotate(code_data[i * 4:i * 4 + 4], i)
        return code_data

    @staticmethod
    def galois_mult(a, b):
        p = 0
        hi_bit_set = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            if hi_bit_set == 0x80:
                a ^= 0x1b
            b >>= 1
        return p % 256

    def mix_column(self, column):
        temp = copy(column)
        column[0] = self.galois_mult(temp[0], 2) ^ self.galois_mult(temp[3], 1) ^ \
            self.galois_mult(temp[2], 1) ^ self.galois_mult(temp[1], 3)
        column[1] = self.galois_mult(temp[1], 2) ^ self.galois_mult(temp[0], 1) ^ \
            self.galois_mult(temp[3], 1) ^ self.galois_mult(temp[2], 3)
        column[2] = self.galois_mult(temp[2], 2) ^ self.galois_mult(temp[1], 1) ^ \
            self.galois_mult(temp[0], 1) ^ self.galois_mult(temp[3], 3)
        column[3] = self.galois_mult(temp[3], 2) ^ self.galois_mult(temp[2], 1) ^ \
            self.galois_mult(temp[1], 1) ^ self.galois_mult(temp[0], 3)
        return column

    def mix_columns(self, code_data):
        for itr in range(0, 4):
            vector = []
            for i in range(0, 4):
                vector.append(code_data[4*i+itr])
            vector = self.mix_column(vector)
            for i in range(0, 4):
                code_data[4 * i + itr] = vector[i]
        return code_data

    @staticmethod
    def key_expansion_aes():
        round_key = []
        round_constant = random.getrandbits(8)
        for i in range((10+1)*16):
            base_key = random.getrandbits(8)
            if i < 16:
                round_key.append(base_key)
            else:
                if i % 16 == 0:
                    round_key.append(round_key[i - 1] ^ round_constant ^ round_key[i - 16])
                    continue
                round_key.append(round_key[i-1] ^ round_key[i-16])
        return round_key

    def add_round_key(self, code_data, round_num):
        for i in range(16):
            code_data[i] = code_data[i] ^ self.ROUND_KEYS[round_num*16+i]
        return code_data

    def round_num(self, code_data, round_num):
        code_data = self.sub_bytes(code_data)
        self.shift_rows(code_data)
        self.mix_columns(code_data)
        self.add_round_key(code_data, round_num)
        return code_data

    def final_round(self, code_data, round_num):
        self.sub_bytes(code_data)
        self.shift_rows(code_data)
        self.add_round_key(code_data, round_num)
        return code_data

    def coding(self, code_data, amount_round):
        round_num = 0
        while round_num < 10:
            if round_num == 0:
                code_data = self.add_round_key(code_data,  0)
                round_num += 1
            else:
                for i in range(amount_round-1):
                    code_data = self.round_num(code_data, round_num)
                    round_num += 1
                else:
                    code_data = self.final_round(code_data, round_num)
        return code_data

    """DECODE"""
    @staticmethod
    def inv_sub_bytes(decode_data):
        print(decode_data)
        decode_data_ = list(decode_data)
        sbox_inv = [
            0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
            0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
            0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
            0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
            0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
            0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
            0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
            0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
            0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
            0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
            0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
            0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
            0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
            0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
        ]
        for i in range(16):
            decode_data[i] = sbox_inv[decode_data_[i]]
        return decode_data

    @staticmethod
    def inv_rotate(word, n):
        return word[-n:] + word[:-n]

    def inv_shift_rows(self, code_data):
        for i in range(1, 4):
            code_data[i * 4:i * 4 + 4] = self.inv_rotate(code_data[i * 4:i * 4 + 4], i)
        return code_data

    def inv_mix_column(self, column):
        temp = copy(column)
        column[0] = self.galois_mult(temp[0], 14) ^ self.galois_mult(temp[3], 9) ^ \
            self.galois_mult(temp[2], 13) ^ self.galois_mult(temp[1], 11)
        column[1] = self.galois_mult(temp[1], 14) ^ self.galois_mult(temp[0], 9) ^ \
            self.galois_mult(temp[3], 13) ^ self.galois_mult(temp[2], 11)
        column[2] = self.galois_mult(temp[2], 14) ^ self.galois_mult(temp[1], 9) ^ \
            self.galois_mult(temp[0], 13) ^ self.galois_mult(temp[3], 11)
        column[3] = self.galois_mult(temp[3], 14) ^ self.galois_mult(temp[2], 9) ^ \
            self.galois_mult(temp[1], 13) ^ self.galois_mult(temp[0], 11)
        return column

    def inv_mix_columns(self, code_data):
        for itr in range(0, 4):
            vector = []
            for i in range(0, 4):
                vector.append(code_data[4*i+itr])
            vector = self.inv_mix_column(vector)
            for i in range(0, 4):
                code_data[4 * i + itr] = vector[i]
        return code_data

    def inv_add_round_key(self, code_data, round_num):
        for i in range(16):
            code_data[i] = code_data[i] ^ self.ROUND_KEYS[(10-round_num)*16+i]
        return code_data

    def inv_round(self, code_data, round_num):
        code_data = self.inv_add_round_key(code_data, round_num)
        self.inv_mix_columns(code_data)
        self.inv_shift_rows(code_data)
        self.inv_sub_bytes(code_data)
        return code_data

    def inv_final_round(self, code_data, round_num):
        self.inv_add_round_key(code_data, round_num)
        self.inv_shift_rows(code_data)
        self.inv_sub_bytes(code_data)
        return code_data

    def decoding(self, code_data, amount_round):
        round_num = 0
        while round_num < 10:
            if round_num == 0:
                code_data = self.inv_final_round(code_data, 0)
                round_num += 1
            else:
                for i in range(amount_round-1):
                    code_data = self.inv_round(code_data, round_num)
                    round_num += 1
                else:
                    code_data = self.inv_add_round_key(code_data, round_num)
        return code_data

    @staticmethod
    def connect_massage(code_data):
        temp = list(code_data)
        code_data.clear()
        for i in range(len(temp)):
            code_data += temp[i]
        return code_data



# aes(message_data)


# def mainAES():
#     ROUND_KEYS = key_expansion_aes()
#     open_key, closed_key = Genarate_keys()
#     ROUND_KEYS_COPY=copy(ROUND_KEYS)
#     crypt_key_aes = Crypt_massages(ROUND_KEYS_COPY, open_key)
#     # Decrypt_key_aes = DeCrypt_massages(crypt_key_aes, closed_key)
#     #print('decry',Decrypt_key_aes)
#     for i in code_data:
#         coding(i, ROUND_KEYS, 10)
#         #decoding(i, Decrypt_key_aes, 10)
#     #Full_Encrypt_Massage=crypt_key_aes+connect_massage(code_data)
#     # message_data = bytes(code_data).decode('utf-8')
#     # print(message_data)
# if __name__ == "__main__":
#     mainAES()