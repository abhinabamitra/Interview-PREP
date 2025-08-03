import numpy as np

def minhash_signature(docs: dict):
    """Minhash Algorithm."""
    all_words = sorted(set(word for doc in docs.values() for word in doc))

    word_to_index = {word: i for i, word in enumerate(all_words)}

    matrix = np.zeros((len(all_words), len(docs)), dtype=int)

    for col, doc in enumerate(docs.values()):
        for word in doc:
            matrix[word_to_index[word]][col] = 1

    print("Characteristic Matrix:\n", matrix)

    def h1(x): return (x +1 ) %4
    def h2(x): return (3*x + 2) % 4
    hash_fns = [h1, h2]

    num_hashes = len(hash_fns)
    num_docs = len(docs)

    signature = np.full((num_hashes, num_docs), np.inf)

    for row in range(len(all_words)):
        for i, h in enumerate(hash_fns):
            hashed_rows = h(row)
            for col in range(num_docs):
                if matrix[row, col] == 1:
                    signature[i, col] = min(signature[i, col], hashed_rows)

    print("\nMinhash Signature Matrix:\n", signature.astype(int))

    return signature

def estimate_jaccard(signature: list, cols: list[int]):
    """Estimate Jaccard Similarity using Minhash Signature."""
    return np.mean(signature[:, cols[0]] == signature[:, cols[1]])

if __name__ == "__main__":
    docs = {
        "D1": ["apple", "banana", "mango"],
        "D2": ["banana", "mango", "grape"],
        "D3": ["apple", "banana", "grape"],
    }
    signature = minhash_signature(docs)

    print("\nEstimated Similarity (D1 vs D2):", estimate_jaccard(signature, [0, 1]))
    print("Estimated Similarity (D1 vs D3):", estimate_jaccard(signature, [0, 2]))
    print("Estimated Similarity (D2 vs D3):", estimate_jaccard(signature, [1, 2]))

