# input
card_public_key = 15335876
door_public_key = 15086442

# sample
# card_public_key = 5764801
# door_public_key = 17807724

def transform_subject_number(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value

def decrypt_transform(subject_number, value):
    # doesn't seem possible to reverse transform_subject_number function
    loop_size = 0
    while True:
        loop_size += 1
    return loop_size


card_transforms = {} # transform -> loop_size
door_transforms = {} # transform -> loop_size
# find card subject number
for subject_number in range(1, 1000):  
    card_loop_size = 0
    while card_loop_size < 1000 and card_public_key not in card_transforms:
        card_transforms[transform_subject_number(subject_number, card_loop_size)] = card_loop_size
        card_loop_size += 1
    door_loop_size = 0
    while door_loop_size < 1000 and door_public_key not in door_transforms:
        door_transforms[transform_subject_number(subject_number, door_loop_size)] = door_loop_size
        door_loop_size += 1
    if card_public_key in card_transforms and door_public_key in door_transforms:
        print(subject_number, card_transforms[card_public_key], door_transforms[door_public_key])
        break


# find encryption key
door_loop_size = door_transforms[door_public_key]
encryption_key = transform_subject_number(card_public_key, door_loop_size)
print(encryption_key)
