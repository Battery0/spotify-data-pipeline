def _grouped_ids(ids, max_limit):
    grouped_album_ids = []

    for num in range(0, len(ids), max_limit):
        twenty_album_ids = ids[num:(num + max_limit)]
        grouped_album_ids.append(twenty_album_ids)
    return grouped_album_ids
