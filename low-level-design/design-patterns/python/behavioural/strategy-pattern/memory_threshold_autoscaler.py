from autoscaling_strategy import  AutoScalingStrategy

class MemoryThresholdAutoScaler(AutoScalingStrategy):
    def __init__(self):
        pass

    def ScaleUP(self, serviceName):
        print(f"Scaling up {serviceName} as memory threshold reached")

    def ScaleDown(self, serviceName):
        print(f"Scaling down {serviceName} as memory is getting underutilized")