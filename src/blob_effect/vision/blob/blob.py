import cv2
import numpy as np

from blob_effect.vision.blob.spline import catmull_rom_spline


class Blob:
    def __init__(
        self, img, x, y, col, r, dense, thickness, is_fill=False, is_square=False
    ):
        """Blob

        Args:
            img (np.ndarray): 画像
            x (int): x座標
            y (int): y座標
            col (tuple[int]): RGB
            r (int): 半径
            dense (int): blob毎の点の数
            thickness (int): 線の太さ
            is_fill (bool): 塗りつぶすかどうか(default: False)
            is_square (bool): 正方形にするかどうか(default: False)
        """
        self.img = img
        self.x = x
        self.y = y
        self.r = r
        self.dense = dense
        self.thickness = thickness
        self.col = col
        self.is_fill = is_fill
        self.is_square = is_square

        self.starting_angle = np.random.uniform(0, 2 * np.pi)
        self.dX = np.random.uniform(0.3, 1.8)
        self.dY = self.dX if self.is_square else np.random.uniform(0.3, 1.8)
        self.offsetX = np.random.uniform(-self.r * 2, self.r * 2)
        self.offsetY = np.random.uniform(-self.r * 2, self.r * 2)

        self.dense = int(np.ceil(self.r * 3) % 360)

        self.pts = []

    def __call__(self):
        """blobを描画する"""
        self.setup()
        self.show()

    def setup(self):
        """blobを更新する"""
        angles = np.linspace(0, 2 * np.pi, self.dense, endpoint=False)
        xs = np.sin(np.sin(np.cos(angles))) * self.r * self.dX + self.x + self.offsetX
        ys = np.sin(np.sin(np.sin(angles))) * self.r * self.dY + self.y + self.offsetY
        self.pts = np.c_[xs, ys]

    def show(self):
        """blobを描画する"""
        # Create a sequence of control points for the spline
        # Add points at the beginning and end to guide the curve's shape
        control_pts = np.vstack([self.pts[-2:], self.pts, self.pts[:2]])

        # Create the spline curve for the blob using Catmull-Rom
        spline_points = []
        for i in range(len(control_pts) - 3):
            sp = catmull_rom_spline(
                control_pts[i],
                control_pts[i + 1],
                control_pts[i + 2],
                control_pts[i + 3],
                self.dense,
            )
            spline_points.extend(sp)
        spline_points = np.array(spline_points, dtype=np.int32).reshape(-1, 1, 2)

        # Draw the spline curve
        if self.is_fill:
            cv2.fillConvexPoly(
                self.img,
                spline_points,
                color=self.col,
            )
        else:
            cv2.polylines(
                self.img,
                [spline_points],
                isClosed=True,
                color=self.col,
                thickness=self.thickness,
            )
