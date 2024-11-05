import argparse
import cv2

from src.exercises.Lunges import Lunges
from src.exercises.Pushup import Pushup
from src.exercises.Plank import Plank
from src.exercises.ShoulderTap import ShoulderTap
from src.exercises.Squat import Squat
from src.ThreadedCamera import ThreadedCamera



class main:
    def __init__(self):
        self.pushup = Pushup()
        self.plank = Plank()
        self.squat = Squat()
        self.shoulderTap = ShoulderTap()
        self.lunges = Lunges()
        self.threaded = ThreadedCamera()

    def rep(self, type, source):
        
        try:
            if type.lower() == str("pushup"):
                self.pushup.exercise(source)
            elif type.lower() == str("squat"):
                self.squat.exercise(source)
                print("Squat - finished")
            elif type.lower() == str("plank"):
                self.plank.exercise(source)
            elif type.lower() == str("shouldertap"):
                self.shoulderTap.exercise(source)
            elif type.lower() == str("lunges"):
                self.lunges.exercise(source)
            else:
                raise ValueError(f"Input {type} and/or {source} is not correct. \n Kindly refer to the documentation")
        except Exception as e:
            print(f"An error in main : {e}" )
        try:
            if self.threaded.total_frames <= 0:
                return
        except Exception as e:
            print(f"An error in main -try1{e}")
            return
        finally:
            print("Execution completed")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-type', "--type", required=True, help="Type of exercise",
                        type=str)
    parser.add_argument('-source', "--source", required=True, help="Path to video source", type=str)
    args = parser.parse_args()
    type = args.type
    source = args.source
    gym = main()
    gym.rep(type, source)