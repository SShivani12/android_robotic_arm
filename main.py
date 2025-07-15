import time

class RoboticArm:
    def __init__(self):
        self.state = "Idle"

    def move(self, direction):
        directions = ["up", "down", "left", "right", "grab", "release"]
        if direction in directions:
            print(f"Moving {direction}")
            self.state = direction
            time.sleep(1)
        else:
            print("Invalid command")

    def status(self):
        return f"Current arm state: {self.state}"

def receive_android_command():
    # Simulated input from Android
    print("Waiting for Android command...")
    time.sleep(2)
    return "grab"  # Simulate receiving "grab" command

if __name__ == "__main__":
    arm = RoboticArm()

    while True:
        command = receive_android_command()
        if command == "exit":
            print("Shutting down.")
            break
        arm.move(command)
        print(arm.status())
