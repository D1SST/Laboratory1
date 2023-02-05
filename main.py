from num2words import num2words

sequence = []
f = open("random.txt", "r")
sequence = [int(i) for i in f.read().split(",")]
for i in range(len(sequence)):
    if (sequence[i] != 0) and (sequence[i] % 2 == 0) and (sequence[i] <= len(sequence)):
        if (i % 2 != 0):
            print(num2words(sequence[i], lang = "ru"), "| иднекс числа -", i)

        else:
            print(sequence[i], "| индекс числа -", i)
        i += 1










