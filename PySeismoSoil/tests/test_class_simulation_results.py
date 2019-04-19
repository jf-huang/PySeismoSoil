# Author: Jian Shi

import unittest
import numpy as np

from PySeismoSoil.class_ground_motion import Ground_Motion
from PySeismoSoil.class_Vs_profile import Vs_Profile
from PySeismoSoil.class_frequency_spectrum import Frequency_Spectrum
from PySeismoSoil.class_simulation_results import Simulation_Results

import PySeismoSoil.helper_site_response as sr

class Test_Class_Simulation_Results(unittest.TestCase):
    def test_plot(self):
        # Test that the desired data are correctly saved to the object
        accel_in = Ground_Motion('./files/sample_accel.txt', unit='m/s/s')
        accel_tmp = accel_in.accel.copy()
        accel_tmp[:, 1] *= 5.0
        accel_out = Ground_Motion(accel_tmp, unit='m/s/s')
        vs_profile = Vs_Profile('./files/profile_FKSH14.txt')
        thk = vs_profile._thk
        depth_bound = sr.thk2dep(thk, midpoint=False)
        depth_midpoint = sr.thk2dep(thk, midpoint=True)
        max_a_v_d = np.column_stack((depth_bound,
                                     depth_bound * 1,
                                     depth_bound * 2,
                                     depth_bound * 3))
        max_gamma_tau = np.column_stack((depth_midpoint,
                                         depth_midpoint * 1,
                                         depth_midpoint * 2))
        freq, tf_ro = vs_profile.transfer_function()[:2]
        trans_func = Frequency_Spectrum(np.column_stack((freq, tf_ro)))
        sim_results = Simulation_Results(accel_in, accel_out, vs_profile,
                                         max_a_v_d, max_gamma_tau, trans_func)
        sim_results.plot(save_fig=False)

if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(Test_Class_Simulation_Results)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
