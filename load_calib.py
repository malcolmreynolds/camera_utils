import numpy as np
from scipy.io import loadmat


class CameraIntrinsics(object):
    def __init__(self, focal_lengths, principal_points, skew, distortion,
                 focal_lengths_error, principal_points_error, skew_error,
                 distortion_error, image_w, image_h):

        self.focal_lengths = focal_lengths
        self.principal_points = principal_points
        self.skew = skew
        self.distortion = distortion

        self.focal_lengths_error = focal_lengths_error
        self.principal_points_error = principal_points_error
        self.skew_error = skew_error
        self.distortion_error = distortion_error

        self.image_w = image_w
        self.image_h = image_h

        self.build_intrinsic_mtx()

    def build_intrinsic_mtx(self):
        self.mtx = np.zeros((3, 3))
        self.mtx[[0, 1], [0, 1]] = self.focal_lengths.flatten()
        self.mtx[0, 1] = self.skew
        self.mtx[:2, 2] = self.principal_points.flatten()
        self.mtx[2, 2] = 1


def load_calibration_data(fname):
    with open(fname) as f:
        calib_data = loadmat(f)

    intrinsics = CameraIntrinsics(
        focal_lengths=calib_data['fc'],
        principal_points=calib_data['cc'],
        skew=calib_data['alpha_c'],
        distortion=calib_data['kc'],
        focal_lengths_error=calib_data['fc_error'],
        principal_points_error=calib_data['cc_error'],
        skew_error=calib_data['alpha_c_error'],
        distortion_error=calib_data['kc_error'],
        image_w=calib_data['nx'],
        image_h=calib_data['ny'])

    return intrinsics
