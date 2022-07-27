"""
 Author:  Michael Luciuk
 Date:    Summer 2022
"""

from typing import Tuple

from pyTEM.lib.interface.Acquisition import Acquisition
from pyTEM.lib.interface.AcquisitionSeries import AcquisitionSeries
from pyTEM_scripts.lib.align_images.GetInOutFile import GetInOutFile


def align_images():
    """
    Read in some images (possibly from a stack, possibly from a bunch of single image files), align the images, and
     save the results back to file.

    Image shifts are estimated using Hyperspy's estimate_shift2D() function. This function uses a phase correlation
     algorithm based on the following paper:
        Schaffer, Bernhard, Werner Grogger, and Gerald Kothleitner. “Automated Spatial Drift Correction for EFTEM
            Image Series.” Ultramicroscopy 102, no. 1 (December 2004): 27–36.

    :return: None. The resulting image stack is saved to file at the location requested by the user.
    """
    # Get the in and out file info from the user.
    in_file, out_file = GetInOutFile().run()

    if isinstance(in_file, str):
        # Then we have a single file, assume it is an image stack.
        acq_series = AcquisitionSeries(source=in_file)

    elif isinstance(in_file, Tuple):
        # We have a bunch of single images in separate files.
        acq_series = AcquisitionSeries()
        for file in in_file:
            acq_series.append(Acquisition(file))

    else:
        raise Exception("Error: in_file type not recognized: " + str(type(in_file)))

    # Go ahead and perform the alignment using AcquisitionSeries' align() method.
    acq_series = acq_series.align()

    # Save to file.
    if out_file[-4:] == ".mrc":
        acq_series.save_as_mrc(out_file=out_file)

    elif out_file[-4:] == ".tif" or out_file[-5:] == ".tiff":
        acq_series.save_as_tif(out_file=out_file)

    else:
        raise Exception("Error: Out file type not recognized: " + str(out_file))


if __name__ == "__main__":
    align_images()
