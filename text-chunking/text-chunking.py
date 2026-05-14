def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    i = 0
    results = []
    while i < len(tokens):
        chunk = tokens[i: i + chunk_size]
        results.append(chunk)

        if i + chunk_size >= len(tokens):
            break
            
        i = i + step

    return results