from dataclasses import dataclass, field


@dataclass
class SignalDataset:
    raw_data: list = field(default_factory=list)
    labels: list = field(default_factory=list)
    patient_ids: list = field(default_factory=list)


# test

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]

# temp = SignalDataset(a, b, c)

# print("hello")
