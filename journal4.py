class Cat:
    def __init__(self, arm_length: float, leg_length: float,
                 num_eyes: int, has_tail: bool, is_furry: bool):
        # Physical characteristics
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("This animal is a cat with the following characteristics:")
        print(f"- Arm length: {self.arm_length} units")
        print(f"- Leg length: {self.leg_length} units")
        print(f"- Number of eyes: {self.num_eyes}")
        print(f"- Has a tail: {self.has_tail}")
        print(f"- Is furry: {self.is_furry}")


# Example usage
my_cat = Cat(
    arm_length=0.25,
    leg_length=0.35,
    num_eyes=2,
    has_tail=True,
    is_furry=True
)

my_cat.describe()