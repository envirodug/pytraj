import unittest
from pytraj.base import *
from pytraj.decorators import no_test
from pytraj.datasets.DataSet_Coords_TRJ import DataSet_Coords_TRJ
from pytraj.datasets.DataSet_Coords_TRJ import DataSet_Coords_TRJ
from pytraj.utils import assert_almost_equal

class Test(unittest.TestCase):
    def test_0(self):
        TRAJ = TrajectoryIterator(filename="./data/md1_prod.Tc5b.x", top="./data/Tc5b.top")
        print(TRAJ.size)
        Nframe = TRAJ.size

        # creat DataSet_Coords_TRJ object
        # man, should we use Trajectory?
        # might not be a big matter since adding frames are not that expensive vs clustering
        coords_traj = DataSet_Coords_TRJ()
        coords_traj.top = TRAJ.top.copy()
        coords_traj.add_trajin(TRAJ)

        # DataSet_Coords_TRJ does not have GetFrame method
        # what should I do?
        assert coords_traj.size == TRAJ.n_frames
        for frame in coords_traj:
            print (frame)

        print (coords_traj[0])

    def test_1(self):
        coords_traj = DataSet_Coords_TRJ()
        coords_traj.top = Topology("./data/Tc5b.top")
        coords_traj.load("./data/md1_prod.Tc5b.x")
        assert coords_traj.size == 10
        coords_traj.load("./data/md1_prod.Tc5b.x", arg="1 5 2")
        assert coords_traj.size == 13

        for f0 in coords_traj:
            print (f0)

        print ("getitem")
        print (coords_traj[12])

        print (coords_traj)
        ds0 = coords_traj.alloc()
        print (ds0)
        print (dir(ds0))

        # try perform action
        from pytraj.common_actions import calc_distance
        d0 = calc_distance(coords_traj, ":2@CA :10@CA", dtype='dataset')
        print (d0)
        print (d0.size)
        print (d0[:])

        # make sure we load correct frames
        assert_almost_equal(coords_traj[0].coords, coords_traj[10].coords)
        assert d0[0][0] == d0[0][10]

        print (coords_traj.dtype)
        
if __name__ == "__main__":
    unittest.main()
