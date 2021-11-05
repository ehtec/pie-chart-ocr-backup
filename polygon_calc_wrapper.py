from ctypes import cdll, c_double, c_uint, c_long, c_ulong
import ctypes
# from numpy.ctypeslib import as_ctypes, as_array, as_ctypes_type
import numpy as np
import copy
from numpy.ctypeslib import ndpointer


lib = cdll.LoadLibrary('./libpolygoncalc.so')

# set output types for PolygonCalc methods
lib.PolygonCalc_helloworld.restype = c_double
lib.PolygonCalc_test_calc.restype = c_double

lib.PolygonCalc_test_nparray.restype = ctypes.c_int
# lib.PolygonCalc_test_nparray.argtypes = (ctypes.c_int, )

lib.PolygonCalc_min_poly_distance.restype = c_double

lib.PolygonCalc_poly_intersection_area.restype = c_double

lib.PolygonCalc_poly_intersection_area_ratio.restype = c_double


class PolygonCalc(object):
    def __init__(self):
        self.obj = lib.PolygonCalc_new()
    #     fun = lib.PolygonCalc_new
    #     fun.argtypes = []
    #     fun.restype = ctypes.c_void_p
    #     self.obj = fun()
    #
    # def __del__(self):
    #     fun = lib.PolygonCalc_delete
    #     fun.argtypes = [ctypes.c_void_p]
    #     fun.restype = None
    #     fun(self.obj)

    def helloworld(self):
        return lib.PolygonCalc_helloworld(self.obj)

    def test_calc(self):
        return lib.PolygonCalc_test_calc(self.obj)

    def test_nparray(self, array):
        # c_double_p = POINTER(c_double)
        array = np.ascontiguousarray(array, dtype=np.float32)
        # array = array.astype(np.double)
        # c_array = array.ctypes.data_as(c_double_p)
        # return lib.PolygonCalc_test_nparray(c_array)
        n = len(list(array))
        print("nnnn: {0}".format(n))
        print(array)
        print(ctypes.c_int(n))
        # return lib.PolygonCalc_test_nparray(ctypes.c_int(n))
        return lib.PolygonCalc_test_nparray(self.obj, ctypes.c_void_p(array.ctypes.data), ctypes.c_int(n))

    def min_poly_distance(self, p1, p2):

        poly1x = []
        poly1y = []

        poly2x = []
        poly2y = []

        for elem in p1:
            poly1x.append(elem[0])
            poly1y.append(elem[1])

        for elem in p2:
            poly2x.append(elem[0])
            poly2y.append(elem[1])

        m = len(poly1x)
        n = len(poly2x)

        poly1x = np.ascontiguousarray(poly1x, dtype=np.double)
        poly1y = np.ascontiguousarray(poly1y, dtype=np.double)

        poly2x = np.ascontiguousarray(poly2x, dtype=np.double)
        poly2y = np.ascontiguousarray(poly2y, dtype=np.double)

        return lib.PolygonCalc_min_poly_distance(
            self.obj,
            ctypes.c_void_p(poly1x.ctypes.data),
            ctypes.c_void_p(poly1y.ctypes.data),
            ctypes.c_void_p(poly2x.ctypes.data),
            ctypes.c_void_p(poly2y.ctypes.data),
            m,
            n
        )

    def poly_intersection_area(self, p1, p2):

        poly1x = []
        poly1y = []

        poly2x = []
        poly2y = []

        for elem in p1:
            poly1x.append(elem[0])
            poly1y.append(elem[1])

        for elem in p2:
            poly2x.append(elem[0])
            poly2y.append(elem[1])

        m = len(poly1x)
        n = len(poly2x)

        poly1x = np.ascontiguousarray(poly1x, dtype=np.double)
        poly1y = np.ascontiguousarray(poly1y, dtype=np.double)

        poly2x = np.ascontiguousarray(poly2x, dtype=np.double)
        poly2y = np.ascontiguousarray(poly2y, dtype=np.double)

        return lib.PolygonCalc_poly_intersection_area(
            self.obj,
            ctypes.c_void_p(poly1x.ctypes.data),
            ctypes.c_void_p(poly1y.ctypes.data),
            ctypes.c_void_p(poly2x.ctypes.data),
            ctypes.c_void_p(poly2y.ctypes.data),
            m,
            n
        )

    def poly_intersection_area_ratio(self, p1, p2):

        poly1x = []
        poly1y = []

        poly2x = []
        poly2y = []

        for elem in p1:
            poly1x.append(elem[0])
            poly1y.append(elem[1])

        for elem in p2:
            poly2x.append(elem[0])
            poly2y.append(elem[1])

        m = len(poly1x)
        n = len(poly2x)

        poly1x = np.ascontiguousarray(poly1x, dtype=np.double)
        poly1y = np.ascontiguousarray(poly1y, dtype=np.double)

        poly2x = np.ascontiguousarray(poly2x, dtype=np.double)
        poly2y = np.ascontiguousarray(poly2y, dtype=np.double)

        return lib.PolygonCalc_poly_intersection_area_ratio(
            self.obj,
            ctypes.c_void_p(poly1x.ctypes.data),
            ctypes.c_void_p(poly1y.ctypes.data),
            ctypes.c_void_p(poly2x.ctypes.data),
            ctypes.c_void_p(poly2y.ctypes.data),
            m,
            n
        )

    def group_elements(self, elements, threshold_dist):

        a = []
        b = []
        c = []
        d = []

        for elem in elements:

            a.append(elem[0])
            b.append(elem[1])
            c.append(elem[2])
            d.append(elem[3])

        n = len(elements)

        a = np.ascontiguousarray(a, dtype=np.uint)
        b = np.ascontiguousarray(b, dtype=np.uint)
        c = np.ascontiguousarray(c, dtype=np.uint)
        d = np.ascontiguousarray(d, dtype=np.uint)

        lib.PolygonCalc_group_elements.restype = ndpointer(dtype=c_ulong, shape=(n,))

        res_array = lib.PolygonCalc_group_elements(
            self.obj,
            ctypes.c_void_p(a.ctypes.data),
            ctypes.c_void_p(b.ctypes.data),
            ctypes.c_void_p(c.ctypes.data),
            ctypes.c_void_p(d.ctypes.data),
            n,
            ctypes.c_double(threshold_dist)
        )

        res_array_copy = copy.deepcopy(res_array)

        res_array_p = res_array.ctypes.data_as(ctypes.POINTER(c_ulong))

        lib.free_long_array(res_array_p)

        return res_array_copy

