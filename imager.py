
class Imager:
    '''
    usage:
        with Imager('image.bin', width=6) as imager:
            some_processing ...
    '''
    def __init__(self, filename:str, width:int):
        '''
        :param x: in bytes - not bits
        '''
        self.filename = filename
        self.width = width
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'rb')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __readline(self) -> bytes:
        line = self.file.read(self.width)
        if line == b'' or line == None:
            raise StopIteration
        if len(line) != self.width:
            line = self.__fill_zero(line)
        return bytes(line)

    def __fill_zero(self, line):
        n_zeros = self.width - len(line)
        assert n_zeros > 0
        line_with_zeros = line + n_zeros * b'\x00'
        return line_with_zeros

    def __str__(self):
        s = super(Imager, self).__str__()
        return "{}:{}".format(self.__class__, self.filename)

    def __iter__(self):
        return self

    def __next__(self) -> bytes:
        return self.__readline()

    @staticmethod
    def line_bytes_to_bits(bytes, width) -> str:
        converted = bin(int(bytes.hex(), base=16))[2:]
        zeros_prefix = '0' * (width * 8 - len(converted))
        return zeros_prefix + converted

    @property
    def str_bin_list(self) -> list:
        '''
        :return: example: ['10101101', '10101101']
        '''
        str_bin_lines = []
        self.file.seek(0)
        for line in self:
            bits = self.line_bytes_to_bits(line, self.width)
            str_bin_lines.append(bits)
        return str_bin_lines

    @staticmethod
    def str_bin_list_to_file(str_bin_list: list, filename: str):
        '''
        :param str_bin_list: example: ['10101101', '10101101']
        every str_bin should has len n*8
        '''
        with open(filename, 'wb') as f:
            for str_bin in str_bin_list:
                for striped in Imager.gen_chars(str_bin, step=8):
                    i = int(striped, base=2)
                    b = i.to_bytes(1, byteorder='big')
                    f.write(b)

    @staticmethod
    def gen_chars(str, step=8):
        pointer_from = 0
        while True:
            try:
                ret = str[pointer_from:pointer_from+step]
                assert len(ret) == 8
                yield ret
                pointer_from += step
            except Exception as e:
                raise StopIteration

    @staticmethod
    def print_line(line:bytes, width):
        print(Imager.line_bytes_to_bits(line, width), line)

    def _print_line(self, line):
        print(self.line_bytes_to_bits(line, self.width), line)

    def print(self):
        self.reset_seek()
        for line in self:
            self._print_line(line)
        self.reset_seek()

    def reset_seek(self):
        self.file.seek(0)



if __name__ == '__main__':
    from python_image import PYTHON_IMAGE

    Imager.str_bin_list_to_file(str_bin_list=PYTHON_IMAGE, filename='python_image.bin')

    with Imager('python_image.bin', width=6) as imager:
        # First image print
        imager.print()

        print('\n\n') # enters

        # Second prints
        for line in imager: # line is 'bytes' object
            imager._print_line(line)

        imager.reset_seek()
        print('\n\n')  # enters

        # Third prints
        # using static method
        for line in imager:
            Imager.print_line(line, width=6)

        imager.reset_seek()
        print('\n\n')  # enters

        # Access to variables
        str_bin_list = imager.str_bin_list
        print(str_bin_list)



