from autoscaling_strategy import AutoScalingStrategy

class CPUThresholdAutoscaler(AutoScalingStrategy):
    def __init__(self):
        pass 

    def ScaleUP(self,serviceName):
        print(f"Scaling up {serviceName} as cpu threshold reached")
    def ScaleDown(self,serviceName):
        print(f"Scaling down {serviceName} as cpu is getting underutilized")