import math

def main():
    theta = 45
    angle_in_radian = theta * (3.141592/180)
    arm_length = 90 / (math.sin(angle_in_radian))
    temp_angle_rad = 390 / arm_length
    beta = temp_angle_rad * (180/3.141592)


    print("*********************************************")
    print("oliyad-tesfaye dimension analysis with python")
    print("*********************************************")
    
    print(f"arm_length: {arm_length}")
    print(f"theta: {theta}")
    print(f"angle_in_radian: {angle_in_radian}")
    print(f"temp_angle_rad: {temp_angle_rad}")
    print(f"beta: {beta}")

if __name__ == "__main__":
    main()