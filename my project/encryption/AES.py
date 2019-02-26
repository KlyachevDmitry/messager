
import numpy as np
import random
#from encryption.RSA import Crypt_massages, DeCrypt_massages, Genarate_keys
from encryption.RSA import rsa
from copy import copy
#Massage_data='qweиtyuiasfgfgf'.encode('utf-8')
Massage_data='Codewars is an educational community for computer programming. On the platform, software developers train on programming challenges known as kata.[1][2] These discrete programming exercises train a variety of skills in a variety of programming languages, and are completed within an online IDE.'.encode('utf-8')

def aes(Massage_data):
    return AES(Massage_data)


class AES:
    def __init__(self, Massage_data, block=4):
        self.block = block
        self.RaundKeys = self.KeyExpansionAES()
        self.open_key, self.closed_key = rsa().generate_keys()
        self.RaundKeys_copy = copy(self.RaundKeys)
        Crypt_key_AES = rsa().crypt_massages(self.RaundKeys_copy, self.open_key)
        self.Massage_data = Massage_data
        DeCrypt_key_AES = rsa().decrypt_massages(Crypt_key_AES, self.closed_key)
        #print('decry',DeCrypt_key_AES)
        self.Code_data = self.CrashingMassage()
        #print('first', self.Code_data)
        for i in self.Code_data:
            print(111,self.Code_data)
            self.Coding(i, 10)
            #print(i)
            #print(222,self.Code_data)
            #print(i)
            self.DeCoding(i,  10)
            print(333, self.Code_data)
        #print(self.Code_data)
        Full_Encrypt_Massage=Crypt_key_AES + self.ConnectMassage(self.Code_data)
        Massage_data = bytes(self.Code_data).decode('utf-8')
        print(Massage_data)

    def CrashingMassage(self):   #crashing can be done better
        Massage_data = list(self.Massage_data)
        Code_data = []
        packeg = int(len(Massage_data)/16)
        if len(Massage_data) % 16 != 0:
            packeg+=1
            Massage_data+=([0]*(16-(len(Massage_data)-(len(Massage_data)//16)*16)))  # method '%' don't work
        for iter in range(packeg):
            Code_data += [Massage_data[iter*16:iter*16+16]]
        #print(Code_data)
        return Code_data

    def SubBytes(self, frame):
        frame_ = list(frame)
        subBytes = [
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

        for iter in range(16):
            #print(frame_)
            frame[iter] = subBytes[frame_[iter]]
        return frame


    def rotate(self, word, n):
        return word[n:]+word[0:n]

#    @staticmethod
    def shift_rows(self, Code_data):
        for iter in range(1,4):
            Code_data[iter * 4:iter * 4 + 4] = self.rotate(Code_data[iter * 4:iter * 4 + 4], iter)
        #print([bin(x) for x in Code_data])
        return Code_data

    def galois_mult(self, a, b):
        p = 0
        hiBitSet = 0
        for i in range(8):
            if b & 1 == 1:
                p ^= a
            hiBitSet = a & 0x80
            a <<= 1
            if hiBitSet == 0x80:
                a ^= 0x1b
            b >>= 1
        return p % 256

    def mixColumn(self, column):
        temp = copy(column)
        column[0] = self.galois_mult(temp[0],2) ^ self.galois_mult(temp[3],1) ^ \
                    self.galois_mult(temp[2],1) ^ self.galois_mult(temp[1],3)
        column[1] = self.galois_mult(temp[1],2) ^ self.galois_mult(temp[0],1) ^ \
                    self.galois_mult(temp[3],1) ^ self.galois_mult(temp[2],3)
        column[2] = self.galois_mult(temp[2],2) ^ self.galois_mult(temp[1],1) ^ \
                    self.galois_mult(temp[0],1) ^ self.galois_mult(temp[3],3)
        column[3] = self.galois_mult(temp[3],2) ^ self.galois_mult(temp[2],1) ^ \
                    self.galois_mult(temp[1],1) ^ self.galois_mult(temp[0],3)
        return column


    def MixColomns(self, Code_data):

        for itr in range(0,4):
            vector = []
            for iter in range(0,4):
                vector.append(Code_data[4*iter+itr])
            vector = self.mixColumn(vector)
            #Mod256(vector)
            for iter in range(0,4):
                Code_data[4 * iter + itr] = vector[iter]
        return Code_data


    def KeyExpansionAES(self):
        RaundKey = []
        RaundConstant=random.getrandbits(8)
        for iter in range((10+1)*16):
            BaseKey = random.getrandbits(8)
            if iter<16:
                RaundKey.append(BaseKey)
            else:
                if iter % 16 == 0:
                    RaundKey.append(RaundKey[iter - 1] ^ RaundConstant^ RaundKey[iter - 16])
                    continue
                RaundKey.append(RaundKey[iter-1]^RaundKey[iter-16])
        #print('roundkey', RaundKey)
        return RaundKey



    def AddRoundKey(self, Code_data, RAUND):
        #print('-------', Code_data, '-------', RaundKeys, '-------', RAUND)
        for i in range(16):
            Code_data[i] = Code_data[i] ^ self.RaundKeys[RAUND*16+i]
        return Code_data

    def Raund(self, Code_data, RAUND):
        Code_data = self.SubBytes(Code_data)

        self.shift_rows(Code_data)
        self.MixColomns(Code_data)
        self.AddRoundKey(Code_data, RAUND)
        #if RAUND ==9: print(RAUND, Code_data)
        return Code_data

    def FinalRaund(self, Code_data, RAUND):  # FIXME проверить ключи
        self.SubBytes(Code_data)
        #print(RAUND, Code_data)
        self.shift_rows(Code_data)

        self.AddRoundKey(Code_data, RAUND)

        return Code_data

    def Coding(self, Code_data, АmountRAUND):
        RAUND=0
        while RAUND < 10:

            if RAUND == 0:
                #print(RAUND, Code_data)
                Code_data = self.AddRoundKey(Code_data,  0)
                RAUND += 1

            else:
                for iter in range(АmountRAUND-1):
                    #if iter ==8: print(RAUND, Code_data, АmountRAUND)
                    Code_data = self.Raund(Code_data, RAUND)
                    RAUND += 1

                else:
                    #print(RAUND, Code_data,АmountRAUND)
                    Code_data = self.FinalRaund(Code_data, RAUND)

        return Code_data

    ###DECODE###
    def InvSubBytes(self, DECode_data):
        DECode_data_=list(DECode_data)
        sboxInv = [
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
            DECode_data[i]=sboxInv[DECode_data_[i]]
        return DECode_data


    def Invrotate(self, word, n):
        return word[-n:] + word[:-n]

    def InvShiftRows(self, Code_data):
        for iter in range(1,4):
            Code_data[iter * 4:iter * 4 + 4] = self.Invrotate(Code_data[iter * 4:iter * 4 + 4], iter)
        return Code_data

    def mixColumnInv(self, column):
        temp = copy(column)
        column[0] = self.galois_mult(temp[0],14) ^ self.galois_mult(temp[3],9) ^ \
                    self.galois_mult(temp[2],13) ^ self.galois_mult(temp[1],11)
        column[1] = self.galois_mult(temp[1],14) ^ self.galois_mult(temp[0],9) ^ \
                    self.galois_mult(temp[3],13) ^ self.galois_mult(temp[2],11)
        column[2] = self.galois_mult(temp[2],14) ^ self.galois_mult(temp[1],9) ^ \
                    self.galois_mult(temp[0],13) ^ self.galois_mult(temp[3],11)
        column[3] = self.galois_mult(temp[3],14) ^ self.galois_mult(temp[2],9) ^ \
                    self.galois_mult(temp[1],13) ^ self.galois_mult(temp[0],11)
        return column


    def InvMixColomns(self, Code_data):

        for itr in range(0,4):
            vector = []
            for iter in range(0,4):
                vector.append(Code_data[4*iter+itr])
            vector = self.mixColumnInv(vector)
            for iter in range(0,4):
                Code_data[4 * iter + itr] = vector[iter]
        return Code_data

    def InvAddRoundKey(self, Code_data, RAUND):
        for i in range(16):
            Code_data[i] = Code_data[i] ^ self.RaundKeys[(10-RAUND)*16+i]
        return Code_data

    def InvRaund(self, Code_data, RAUND):
        #if RAUND == 1: print(RAUND, Code_data)
        Code_data = self.InvAddRoundKey(Code_data, RAUND)
        self.InvMixColomns(Code_data)
        self.InvShiftRows(Code_data)

        self.InvSubBytes(Code_data)
        return Code_data

    def InvFinalRaund(self, Code_data, RAUND):  # FIXME проверить ключи
        self.InvAddRoundKey(Code_data, RAUND)

        self.InvShiftRows(Code_data)
        #print(RAUND, Code_data)
        self.InvSubBytes(Code_data)
        return Code_data

    def DeCoding(self, Code_data, АmountRaund):
        #print(Code_data)
        RAUND=0
        while RAUND<10:
            if RAUND==0:
                Code_data = self.InvFinalRaund(Code_data, 0)
                RAUND+=1
                #print(RAUND, Code_data)
            else:
                for iter in range(АmountRaund-1):
                    Code_data = self.InvRaund(Code_data, RAUND)
                    RAUND += 1
                    #if iter == 0: print(RAUND, Code_data)
                else:
                    Code_data = self.InvAddRoundKey(Code_data, RAUND)
                    #print(RAUND, Code_data)

        return Code_data

    def ConnectMassage(self, Code_data):
        temp = list(Code_data)
        Code_data.clear()
        for iter in range(len(temp)):
            Code_data += temp[iter]
        return Code_data


aes(Massage_data)
# def mainAES():
#     RaundKeys = KeyExpansionAES()
#     open_key, closed_key = Genarate_keys()
#     RaundKeys_copy=copy(RaundKeys)
#     Crypt_key_AES = Crypt_massages(RaundKeys_copy, open_key)
#     # DeCrypt_key_AES = DeCrypt_massages(Crypt_key_AES, closed_key)
#     #print('decry',DeCrypt_key_AES)
#     for iter in Code_data:
#         Coding(iter, RaundKeys, 10)
#         #DeCoding(iter, DeCrypt_key_AES, 10)
#     #Full_Encrypt_Massage=Crypt_key_AES+ConnectMassage(Code_data)
#     # Massage_data = bytes(Code_data).decode('utf-8')
#     # print(Massage_data)
# if __name__ == "__main__":
#     mainAES()