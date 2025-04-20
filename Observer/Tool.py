import numpy as np
from abc import ABC, abstractmethod


class PDEBaseSolver(object):

    def __init__(self, T: float = 2.0, dt: float = 0.001, X: int = 1, dx: float = 0.01):
        
        """
        初始化PDE求解器。

        :param T: 总时间（默认值为1.0）。
        :param dt: 时间步长（默认值为0.01）。
        :param X: 空间长度（默认值为1.0）。
        :param dx: 空间步长（默认值为0.1）。
        """

        # 根据模拟的时空来进行离散
        self.nt = int(round(T / dt))
        self.nx = int(round(X / dx))
        self.dt = dt
        self.T = T
        self.dx = dx
        self.x = np.linspace(0, X, self.nx)

        self.u = np.zeros((self.nt, self.nx))

        self.time_index = 0

        print(f" 👀 State variable discretization completed. Shape of u: {self.u.shape}")
    
    
    def simulation(self, control: float = 0.0):
        """
        建立不同系统的演化步骤,默认为开环控制
        """
        pass


if __name__ == "__main__":
    # 测试参数
    T = 2.0
    dt = 0.001
    X = 1.0
    dx = 0.01

    # 创建 PDEBaseSolver 实例
    solver = PDEBaseSolver(T=T, dt=dt, X=X, dx=dx)
