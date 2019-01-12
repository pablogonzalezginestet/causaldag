from unittest import TestCase
import unittest
import numpy as np
import causaldag as cd
from scipy.stats import multivariate_normal

from causaldag import ConstantIntervention, BinaryIntervention, ScalingIntervention


class TestDAG(TestCase):
    def setUp(self):
        w = np.zeros((3, 3))
        w[0, 1] = 1
        w[0, 2] = -1
        w[1, 2] = 4
        self.gdag = cd.GaussDAG.from_amat(w)

    def test_arcs(self):
        self.assertEqual(self.gdag.arcs, {(0, 1), (0, 2), (1, 2)})

    def test_add_node(self):
        pass

    def test_add_arc(self):
        pass

    def test_remove_node(self):
        pass

    def test_remove_arc(self):
        pass

    # def test_from_precision(self):
    #     prec = np.array([
    #         [14, 13, -3],
    #         [13, 26, -5],
    #         [-3, -5, 1]
    #     ])
    #     order1 = [0, 1, 2]
    #     gdag1 = cd.GaussDAG.from_precision(prec, order1)
    #     self.assertDictEqual(gdag1.arc_weights, {(1, 2): 2, (1, 3): 3, (2, 3): 5})

    # def test_logpdf_observational(self):
    #     amat = np.array([
    #         [0, 2, 3],
    #         [0, 0, 5],
    #         [0, 0, 0]
    #     ])
    #     gdag = cd.GaussDAG.from_amat(amat)
    #     samples = gdag.sample(100)
    #     logpdf_gdag = gdag.logpdf(samples)
    #     logpdf_scipy = multivariate_normal.logpdf(samples, cov=gdag.covariance)
    #     self.assertTrue(all(np.isclose(logpdf_gdag, logpdf_scipy)))
    #
    # def test_logpdf_interventional_constant(self):
    #     amat = np.array([
    #         [0, 2, 3],
    #         [0, 0, 5],
    #         [0, 0, 0]
    #     ])
    #     gdag = cd.GaussDAG.from_amat(amat)
    #     iv = {0: ConstantIntervention(val=0)}
    #     samples1 = gdag.sample_interventional_perfect(iv, 100)
    #     logpdf_gdag = gdag.logpdf(samples1, interventions=iv)
    #
    #     amat_iv = np.array([
    #         [0, 5],
    #         [0, 0]
    #     ])
    #     gdag_iv = cd.GaussDAG.from_amat(amat_iv)
    #     logpdf_gdag_iv = gdag_iv.logpdf(samples1[:, [1, 2]])
    #
    #     self.assertTrue(all(np.isclose(logpdf_gdag, logpdf_gdag_iv)))
    #
    # def test_logpdf_interventional_binary_constant(self):
    #     amat = np.array([
    #         [0, 2, 3],
    #         [0, 0, 5],
    #         [0, 0, 0]
    #     ])
    #     gdag = cd.GaussDAG.from_amat(amat)
    #     iv = {0: BinaryIntervention(intervention1=ConstantIntervention(val=-2), intervention2=ConstantIntervention(val=2))}
    #     samples1 = gdag.sample_interventional_perfect(iv, 10)
    #     logpdf_gdag = gdag.logpdf(samples1, interventions=iv)
    #
    #     amat_iv = np.array([
    #         [0, 5],
    #         [0, 0]
    #     ])
    #     gdag_iv = cd.GaussDAG.from_amat(amat_iv)
    #     logpdf_iv1 = multivariate_normal.logpdf(samples1[:, [1, 2]] - np.array([4, 26]), cov=gdag_iv.covariance)
    #     logpdf_iv2 = multivariate_normal.logpdf(samples1[:, [1, 2]] - np.array([-4, -26]), cov=gdag_iv.covariance)
    #     logpdf_scipy = np.log(.5 * np.exp(logpdf_iv1) + .5 * np.exp(logpdf_iv2))
    #
    #     self.assertTrue(all(np.isclose(logpdf_gdag, logpdf_scipy)))

    def test_scaling_intervention(self):
        gdag = cd.GaussDAG([0, 1, 2], arcs={(0, 1): 2, (0, 2): 3, (1, 2): 5})
        factor = .1
        gdag_iv = cd.GaussDAG([0, 1, 2], arcs={(0, 1): 2, (0, 2): 3*factor, (1, 2): 5*factor})
        iv = {2: ScalingIntervention(factor=factor)}
        samples = gdag.sample_interventional_soft(iv, 100000)
        print(np.cov(samples, rowvar=False))
        print(gdag_iv.covariance)


if __name__ == '__main__':
    unittest.main()
