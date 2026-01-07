from crypto.hash_utils import calculate_sha256

def verify_integrity(file_path, original_hash):
    """
    Verify integrity of evidence by comparing hashes.
    """
    current_hash = calculate_sha256(file_path)
    return current_hash == original_hash
