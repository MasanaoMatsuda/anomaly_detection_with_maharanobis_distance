import numpy as np

class MahalanobisDistance2:

    def __init__(self, data):
        self.mean = np.mean(data, axis=0)
        self.cov_inv = np.linalg.pinv(np.cov(data, rowvar=False))

    def measure(self, new_data):
        return np.dot(
            np.dot((new_data - self.mean), self.cov_inv),
            (new_data - self.mean).T
        )
        # return np.sqrt(
        #     np.dot(
        #         np.dot((new_data - self.mean), self.cov_inv),
        #         (new_data - self.mean).T
        #     )
        # )

def mahalanobis_distances2(x: np.ndarray) -> np.ndarray:
    mean = np.mean(x, axis=0)
    cov_inv = np.linalg.inv(np.cov(x.T))
    return [np.dot(np.dot((s-mean), cov_inv), (s-mean).T) for s in x]

# mahalanobis_distances2(sifs.values)