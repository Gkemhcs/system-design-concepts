from autoscaler_instance import AutoScaler
from memory_threshold_autoscaler import MemoryThresholdAutoScaler
from cpu_threshold_autoscaler import CPUThresholdAutoscaler
from scheduled_autoscaler import ScheduledAutoScaler

def main():

    cpu_auto_scaler=CPUThresholdAutoscaler()
    memory_auto_scaler=MemoryThresholdAutoScaler()
    scheduled_auto_scaler=ScheduledAutoScaler()

    auto_scaler=AutoScaler(cpu_auto_scaler)
    auto_scaler.scale_up("billing-service")
    auto_scaler.scale_down("billing-service")
    auto_scaler.set_strategy(memory_auto_scaler)
    auto_scaler.scale_up("billing-service")
    auto_scaler.scale_down("billing-service")
    auto_scaler.set_strategy(scheduled_auto_scaler)
    auto_scaler.scale_up("billing-service")
    auto_scaler.scale_down("billing-service")
   
if (__name__=="__main__"):
    main()




