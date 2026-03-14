def prune_context(docs, max_tokens=800):

    pruned = []
    total = 0

    for doc in docs:
        length = len(doc.page_content)

        if total + length < max_tokens:
            pruned.append(doc.page_content)
            total += length
        else:
            break

    return "\n".join(pruned)