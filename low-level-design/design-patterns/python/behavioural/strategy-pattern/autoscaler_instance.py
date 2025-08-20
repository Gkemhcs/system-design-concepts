from autoscaling_strategy import AutoScalingStrategy


class AutoScaler:
    def __init__(self,strategy:AutoScalingStrategy):
        self.strategy=strategy
    def set_strategy(self,strategy:AutoScalingStrategy):
        self.strategy=strategy
    def scale_up(self,serviceName):
        self.strategy.ScaleUP(serviceName)
    def scale_down(self,serviceName):
        self.strategy.ScaleDown(serviceName)