"""
 Author:  Michael Luciuk
 Date:    Summer 2022
"""


class AcquisitionProperties:
    """
    Basically just a datastructure to hold tilt series acquisition properties.

    Public Attributes:
        camera_name:      str:              The name of the camera being used.
        alpha_arr:        array of floats:  An array of the tilt acquisition's alpha start-stop values.
        alphas:           array of floats:  The middle alpha values of the tilt acquisition.
        integration_time: int:              Total exposure time for a single image in seconds.
        sampling:         str:              Photo resolution.
        out_file:         str:              Out file path.
        tilt_speed:       float:            Alpha tilt speed in "Thermo Fisher speed units".

    Protected Attributes:
        None.

    Private Attributes:
        None.
    """

    def __init__(self, camera_name, alpha_arr, integration_time=3, sampling='1k', out_file=None):
        """
        :param camera_name: str:
            The name of the camera being used.
        :param alpha_arr: numpy.array of floats:
            An array of alpha start-stop values in the tilt acquisition.
        :param sampling: str:
            Photo resolution, one of:
                - '4k' for 4k images (4096 x 4096; sampling=1)
                - '2k' for 2k images (2048 x 2048; sampling=2)
                - '1k' for 1k images (1024 x 1024; sampling=3)
                - '0.5k' for 05.k images (512 x 512; sampling=8)
        :param integration_time: float:
            Total exposure time for a single image in seconds.
        :param out_file: str:
            Out file path (where the results of the acquisition will be saved).
        """
        self.alpha_step = alpha_arr[1] - alpha_arr[0]
        self.camera_name = camera_name
        self.alpha_arr = alpha_arr
        self.integration_time = integration_time
        self.sampling = sampling
        self.out_file = out_file
        self.alphas = alpha_arr[0:-1] + self.alpha_step / 2
        self.tilt_speed = 1.4768 * (self.alpha_step / integration_time) + 0.0001  # TODO: Confirm

    def __str__(self):
        return "Name of the camera being used: " + str(self.camera_name) + \
                "\nAn array of the tilt acquisition's alpha start-stop values: " + str(self.alpha_arr) + \
                "\nThe middle alpha values of the tilt acquisition: " + str(self.alphas) + \
                "\nTotal exposure time for a single image: " + str(self.integration_time) + " [seconds]" + \
                "\nPhoto resolution: " + str(self.sampling) + \
                "\nOut file path: " + str(self.out_file) + \
                "\nAlpha tilt speed: " + str(self.tilt_speed) + " [Thermo Fisher speed units]"


if __name__ == "__main__":

    import numpy as np

    start_alpha = -35
    stop_alpha = 30
    step_alpha = 1
    num_alpha = int((stop_alpha - start_alpha) / step_alpha + 1)
    alpha_arr_ = np.linspace(start=start_alpha, stop=stop_alpha, num=num_alpha, endpoint=True)

    acq_prop = AcquisitionProperties(camera_name="BM-Ceta", alpha_arr=alpha_arr_, integration_time=3, sampling='1k',
                                     out_file=None)

    print(acq_prop)
