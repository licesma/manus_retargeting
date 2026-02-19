import time
from vr import VuerTeleop

CONFIG_FILE = "../Humanoid-Teleop/assets/inspire_hand/inspire_hand.yml"

teleop = VuerTeleop(config_file_path=CONFIG_FILE, img_shm_name=None)

print("Streaming hand positions. Press Ctrl+C to stop.\n")
try:
    while True:
        head, left_wrist, right_wrist, left_hand, right_hand = teleop.step()

        # left_hand and right_hand are retargeted joint angles (qpos)
        # shape: (7,) for Unitree Dex3 [thumb x3, middle x2, index x2]
        # None if no hand data received yet
        print(f"Left  hand qpos: {left_hand}")
        print(f"Right hand qpos: {right_hand}")
        print()

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Shutting down...")
    teleop.shutdown()
