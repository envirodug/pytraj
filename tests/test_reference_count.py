from __future__ import print_function
import unittest
import pytraj as pt
import sys
from pytraj.base import *
from pytraj import adict
from pytraj import io as mdio
from pytraj.utils.check_and_assert import assert_almost_equal
import pytraj.common_actions as pyca


class TestReferentCounting(unittest.TestCase):
    def test_pyca(self):
        # pyca
        traj = mdio.iterload('./data/md1_prod.Tc5b.x', './data/Tc5b.top')

        # pyca
        d = pyca.search_hbonds(traj)

        assert sys.getrefcount(d) == 2
        sys.getrefcount(d) == 2
        junk = d.filter('SER')
        del junk

        assert sys.getrefcount(d) == 2
        sys.getrefcount(d)

        pyca.search_hbonds(traj).filter('SER')
        pyca.search_hbonds(traj).filter('SER').filter("SER")
        e = pyca.search_hbonds(traj).filter(
            'SER').filter("SER").filter("").filter("")
        # make sure getting not segmentation fault

    def test_traj_search_hbonds(self):
        traj = mdio.iterload('./data/md1_prod.Tc5b.x', './data/Tc5b.top')
        # traj.search_hbonds
        d = pt.search_hbonds(traj, )

        assert sys.getrefcount(d) == 2
        sys.getrefcount(d) == 2
        junk = d.filter('SER')
        del junk

        assert sys.getrefcount(d) == 2
        sys.getrefcount(d)
        junk = d[:3].filter('SER')
        del junk
        assert sys.getrefcount(d) == 2

        pt.search_hbonds(traj, ).filter('SER')
        pt.search_hbonds(traj, ).filter('SER').filter("SER")
        e = pt.search_hbonds(traj, ).filter(
            'SER').filter("SER").filter("").filter("")
        # make sure getting not segmentation fault


if __name__ == '__main__':
    unittest.main()
