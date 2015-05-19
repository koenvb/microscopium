from __future__ import absolute_import
import itertools as it
import numpy as np
from scipy.stats.mstats import mquantiles
from scipy import ndimage as nd
from skimage import morphology as skmorph
from skimage import filters as imfilter, measure, util
from sklearn.neighbors import NearestNeighbors
from six.moves import range



def test_normalize_vectors():
    input =
    assert expected == result


def test_triplet_angles():
    expected =