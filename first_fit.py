def first_fit(memory, required, index):

    n = len(memory)
    if n == 0:
        return None

    for i in range(n):
        pos = (index + i) % n
        base, limit = memory[pos]

        if limit >= required:

            new_base = base + required
            new_limit = limit - required
            new_index = (pos+1) % len(memory)

            if new_limit > 0:
                memory[pos] = (new_base, new_limit)
            else:
                new_index = pos
                memory.pop(pos)

            return  (memory, new_base, new_limit, new_index if memory else 0)

    return  None