import ctypes
import pathlib
if __name__ == "__main__":
    # load the shared library in ctypes
    libname = pathlib.Path().absolute() / "libcmult.so"
    c_lib = ctypes.CDLL(libname)
    x, y = 6, 2.3
    c_lib.cmult.restype = ctypes.c_float
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"in python x = {x}, y = {y:.1f}, result = {answer:.1f}")