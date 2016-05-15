def get_multline(ctx=None):
    if ctx:
        print ctx
    lines = []
    while True:
        line = raw_input()
        if line:
            lines.append(line)
        else:
            return '\n'.join(lines)
