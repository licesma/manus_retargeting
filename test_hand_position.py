import time
from vr import VuerTeleop

CONFIG_FILE = "./assets/inspire_hand/inspire_hand.yml"

teleop = VuerTeleop(config_file_path=CONFIG_FILE, img_shm_name=None)

print("Streaming hand positions. Press Ctrl+C to stop.\n")
try:
    while True:
        head, left_wrist, right_wrist, left_hand, right_hand = teleop.step()

        # right_hand qpos shape: (7,) -> [thumb x3, middle x2, index x2]
        if right_hand is not None:
            idx0, idx1 = right_hand[5], right_hand[6]
            #print(f"Right hand index joints: [{idx0:.4f}, {idx1:.4f}]")
        else:
            print("Right hand index joints: no data yet")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Shutting down...")
    teleop.shutdown()
