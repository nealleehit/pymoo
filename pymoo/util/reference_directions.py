import numpy as np
from scipy import special


def get_ref_dirs_from_section(n_obj, n_sections):

    if n_obj == 1:
        return np.array([1.0])

    # all possible values for the vector
    sections = np.linspace(0, 1, num=n_sections + 1)[::-1]

    ref_dirs = []
    ref_recursive([], sections, 0, n_obj, ref_dirs)
    return np.array(ref_dirs)


# returns the closest possible number of references lines to given one
def get_ref_dirs_from_n(n_obj, n_refs, max_sections=100):
    n_sections = np.array([get_number_of_reference_directions(n_obj, i) for i in range(max_sections)])
    idx = np.argmin((n_sections < n_refs).astype(np.int))
    return get_ref_dirs_from_section(n_obj, idx-1)


def ref_recursive(v, sections, level, max_level, result):
    v_sum = np.sum(np.array(v))

    # sum slightly above or below because of numerical issues
    if v_sum > 1.0001:
        return
    elif level == max_level:
        if 1.0 - v_sum < 0.0001:
            result.append(v)
    else:
        for e in sections:
            next = list(v)
            next.append(e)
            ref_recursive(next, sections, level + 1, max_level, result)


def get_number_of_reference_directions(n_obj, n_sections):
    return int(special.binom(n_obj + n_sections - 1, n_sections))


def get_ref_dirs_from_points(n_obj):

    extreme_reference_points = np.eye(n_obj)

    ref_points = np.array([[0.2, 0.4], [0.8, 0.4]])

    ref_points = np.append(ref_points, extreme_reference_points, axis=0)

    return ref_points


if __name__ == '__main__':

    test = get_ref_dirs_from_n(2, 100)

    for i in [3]:
        for j in range(20):
            test = get_ref_dirs_from_section(i, j)
            print(j, len(test), get_number_of_reference_directions(i, j))
    print()