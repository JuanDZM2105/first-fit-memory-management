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

            if new_limit > 0:
                memory[pos] = (new_base, new_limit)
            else:
                memory.pop(pos)

            pos = pos if pos < len(memory) else 0

            return  (memory, new_base, new_limit, pos)

    return  None