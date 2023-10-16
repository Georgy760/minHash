from random import shuffle
import mmh3


text1 = "Once upon a time, in a small village nestled between rolling hills, there lived a curious young girl named Amelia. Amelia had always been fascinated by the mysteries of the forest that bordered their village. The elders often told stories of magical creatures and hidden treasures deep within the woods, but they also warned against venturing too far.One bright and sunny morning, Amelia decided to embark on an adventure. With a small satchel slung over her shoulder, she set off into the heart of the forest, her heart brimming with excitement. As she ventured deeper, the trees grew taller and the air filled with the sweet scent of wildflowers.Amelia lost track of time as she explored, and as the sun began to dip below the horizon, she realized she was deep within the forest, far from home. Panic set in, but just as she was about to give in to fear, a soft glow illuminated the path before her. Following the ethereal light, she stumbled upon a tranquil clearing, where a magnificent waterfall cascaded into a crystal-clear pool. Bathed in the moonlight, the scene felt like something out of a fairy tale. As she approached the pool, she noticed a silvery fish swimming within, its scales shimmering like stars.Amelia reached out to touch the water, and as her fingers made contact, a tingling sensation spread through her. She felt an overwhelming sense of connection with the forest and the creatures that called it home. It was a moment of pure magic and wonder.With newfound courage and wisdom, Amelia found her way back home, and her adventures in the forest became a source of inspiration and fascination for the entire village. She learned that sometimes, the greatest treasures can be found when you step outside your comfort zone and explore the world around you."
text2 = "Under the starry night sky, a lone traveler named David found himself on a deserted stretch of road. He had been driving for hours, the headlights of his car cutting through the darkness. The only sound was the hum of the engine and the occasional hoot of an owl. As he turned a bend in the road, his headlights revealed an old, abandoned mansion. Its windows were shattered, and the ivy-covered walls seemed to whisper tales of long-forgotten secrets. Curiosity got the better of him, and he parked his car by the roadside. David ventured into the mansion, his footsteps echoing through the decaying halls. It was as if time had frozen here. He explored room after room, each revealing more about the mansion's mysterious past. In a dusty library, he found journals dating back centuries, filled with stories of love, loss, and enigmatic occurrences. The further he delved, the more he felt a strange connection to this place. It was as if the mansion had been waiting for him, its secrets ready to be unraveled. He couldn't resist the pull of the unknown. In the heart of the mansion, David discovered a hidden chamber. Within, he found a chest, ornate and covered in intricate carvings. As he opened it, his breath caught in his throat. Inside was a collection of letters, each sealed with a wax emblem. The letters told a tale of forbidden love, of a time when the mansion was alive with laughter and music. They revealed a tragedy that had befallen the inhabitants, a story of star-crossed lovers torn apart by circumstance. As David read, he couldn't help but feel a profound sense of connection to the past. It was as though he had been chosen to uncover this long-buried history, to bring the story of the mansion's lost souls back to life. With the letters in hand, he left the mansion, his journey forever changed. He had not only discovered the secrets of the past but had become a part of their eternal story."
text3 = "In the bustling heart of the city, where skyscrapers touched the sky and the streets thrummed with life, there was a small, unassuming bookstore known as 'Whispering Pages.' Its weathered sign above the entrance hinted at the hidden treasures within. Ella, a young woman with an insatiable love for books, stumbled upon this quaint bookstore one rainy afternoon. As she entered, the scent of old books and the soft creak of wooden floors greeted her. The shelves were crammed with volumes of all sizes and shapes, each seemingly waiting for the right reader to discover its secrets. Ella spent hours among the shelves, her fingers trailing over the spines of countless books. She felt a connection with the place, as if it held a piece of her soul. It was more than just a store; it was a sanctuary for book lovers. The elderly proprietor, Mr. Pendleton, watched Ella from behind the counter. He had a knowing smile, recognizing in her the same passion for books that had led him to open Whispering Pages many years ago. Ella finally chose a book, a weathered copy of a classic novel. As she paid and prepared to leave, Mr. Pendleton leaned in and whispered, Remember, dear, books have a way of finding their readers. They know who needs them most.' With that cryptic message, Ella stepped back out into the bustling city, clutching her new treasure. Little did she know that this simple visit to Whispering Pages would change the course of her life. The book she had chosen would lead her on a journey of self-discovery, love, and adventure, unlocking doors she never knew existed. As Ella walked away, she couldnt help but smile. The citys noise had faded into the background, and she felt like she had discovered a hidden oasis, a place where the whispered secrets of books held the keys to her destiny."

def shingle(text: str, k: int):
    shingle_set = []
    for i in range(len(text) - k+1):
        shingle_set.append(text[i:i+k])
    return set(shingle_set)

text = "The quick brown fox jumps over the lazy dog"
k = 2
shingles1 = shingle(text1, k)
shingles2 = shingle(text2, k)
shingles3 = shingle(text3, k)
print(f"1: {shingles1}\n"
      f"2: {shingles2}\n"
      f"3: {shingles3}")

vocab = shingles1.union(shingles2).union(shingles3)
print(f"vocab: {vocab}")

shingle1_1hot = [1 if x in shingles1 else 0 for x in vocab]
shingle2_1hot = [1 if x in shingles2 else 0 for x in vocab]
shingle3_1hot = [1 if x in shingles3 else 0 for x in vocab]

print(f"1hot-1: {shingle1_1hot}\n"
      f"1hot-2: {shingle2_1hot}\n"
      f"1hot-3: {shingle3_1hot}")

hash_ex = list(range(1, len(vocab)+1))

shuffle(hash_ex)
print(f"hash_ex: {hash_ex}")

print("shingle1_1hot")
for i in range(1, 10):
    idx = hash_ex.index(i)
    signature_val = shingle1_1hot[idx]
    print(f"{i} -> {idx} -> {signature_val}")
    if signature_val == 1:
        print("match!")
        break

print("shingle2_1hot")
for i in range(1, 10):
    idx = hash_ex.index(i)
    signature_val = shingle2_1hot[idx]
    print(f"{i} -> {idx} -> {signature_val}")
    if signature_val == 1:
        print("match!")
        break

print("shingle3_1hot")
for i in range(1, 10):
    idx = hash_ex.index(i)
    signature_val = shingle3_1hot[idx]
    print(f"{i} -> {idx} -> {signature_val}")
    if signature_val == 1:
        print("match!")
        break

def create_hash_func(size: int):
    hash_ex = list(range(1, len(vocab)+1))
    shuffle(hash_ex)
    return hash_ex

def buid_minhash_func(vocab_size: int, nbits: int):
    hashes = []
    for _ in range(nbits):
        hashes.append(create_hash_func(vocab_size))
    return hashes

minhash_func = buid_minhash_func(len(vocab), 20)

def create_hash(vector: list):
    signature = []
    for func in minhash_func:
        for i in range(1, len(vocab)+1):
            idx = func.index(i)
            signature_val = vector[idx]
            if signature_val == 1:
                signature.append(idx)
                break
    return signature

shingle1_sig = create_hash(shingle1_1hot)
shingle2_sig = create_hash(shingle2_1hot)
shingle3_sig = create_hash(shingle3_1hot)

print(f"sig-1: {shingle1_sig}\n"
      f"sig-2: {shingle2_sig}\n"
      f"sig-3: {shingle3_sig}")

def jaccard(x, y):
    return len(x.intersection(y)) / len(x.union(y))

print(jaccard(set(shingle1_sig), set(shingle2_sig)))
print(jaccard(set(text1), set(text2)))

def split_vector(signature, b):
    assert len(signature) % b == 0
    r = int(len(signature) / b)

    subvecs = []
    for i in range(0, len(signature), r):
        subvecs.append(signature[i : i+r])
    return subvecs

band_1 = split_vector(shingle1_sig, 10)
band_2 = split_vector(shingle2_sig, 10)
band_3 = split_vector(shingle3_sig, 10)

print(f"band_1: {band_1}\n"
      f"band_2: {band_2}\n"
      f"band_3: {band_3}")

for rows_1, rows_2 in zip(band_1, band_2):
    if rows_1 == rows_2:
        print(f"Candidate pair for band_1 & band_2: {rows_1} == {rows_2}")
        break

for rows_2, rows_3 in zip(band_2, band_3):
    if rows_2 == rows_3:
        print(f"Candidate pair for band_2 & band_3: {rows_2} == {rows_3}")
        break

for rows_1, rows_3 in zip(band_1, band_3):
    if rows_1 == rows_2:
        print(f"Candidate pair for band_1 & band_3: {rows_1} == {rows_3}")
        break

