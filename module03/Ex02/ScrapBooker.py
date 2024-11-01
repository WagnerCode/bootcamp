import numpy as np


class ScrapBooker:
    def crop(self, array, dim, position=(1,0)):

        print(array)
        b = array[position[0]:dim[0] + position[0], position[1]].copy()
        d = np.reshape(b, (-1, dim[1]))

        return print(d)



    def thin(self, array, n, axis):
        pass
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """


    def juxtapose(self, array, n, axis):
        pass
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """


    def mosaic(self, array, dim):
        pass
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """

f = ScrapBooker()
arr1 = np.arange(0, 25).reshape(5, 5)
#f.crop(arr1, (3,1))

