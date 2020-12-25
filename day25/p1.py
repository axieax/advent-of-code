def transform_subject_number(subject_number, loop_size):
    # Version 1:
    # value = 1
    # for _ in range(loop_size):
    #     value *= subject_number
    #     value %= 20201227
    # return value
    
    # Version 2:
    # return (subject_number ** loop_size) % 20201227
    return pow(subject_number, loop_size, 20201227)


# extract input from file
with open('input.txt', 'r') as f:
    card_public_key, door_public_key = [int(x) for x in f.readlines()]
    subject_number = 7

# find card loop size (unnecessary)
# card_loop_size = 0
# while transform_subject_number(subject_number, card_loop_size) != card_public_key:
#     card_loop_size += 1

# find door loop size
door_loop_size = 0
while transform_subject_number(subject_number, door_loop_size) != door_public_key:
    door_loop_size += 1

# find encryption key
encryption_key = transform_subject_number(card_public_key, door_loop_size)
print(encryption_key)
