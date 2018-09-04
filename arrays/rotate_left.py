# RotLeft Problem

def rot_left(a, d):
    """Rotate the array a d times."""

    idx = len(a) - d
    a = a[-idx:] + a[:d]

    return a

arr = [1,2,3,4,5,6,7,8,9]

if __name__ == '__main__':
    print(rot_left(arr, 4))