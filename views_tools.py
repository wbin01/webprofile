import unicodedata


def color() -> dict:
    h = '#FFF'
    return {
        'card': {
            'h1': h, 'h2': h, 'h3': h,
            'h4': h, 'h5': h, 'h6': h,
            'p': '#AAA'},
        'content': {
            'h1': h, 'h2': h, 'h3': h,
            'h4': h, 'h5': h, 'h6': h,
            'p': '#55555'},
    }


def font() -> dict:
    h = 'Alkalami'
    return {
        'card': {
            'h1': h, 'h2': h, 'h3': h,
            'h4': h, 'h5': h, 'h6': h}
    }


def separate_posts_into_quantity_groups(
        posts_list: list, items_quantity: int) -> list:
    """Separate on groups

    if quantity groups is 3...
    move this:
    [obj, obj, obj, obj, obj, obj]

    for this:
    [[obj, obj, obj], [obj, obj, obj]]

    :param posts_list:
    :param items_quantity:
    :return:
    """

    all_post_groups_list = []
    one_post_group_list = []
    for item in enumerate(posts_list):
        index_post, object_post = (item[0], item[1])

        if index_post != 0 and index_post % items_quantity == 0:
            all_post_groups_list.append(one_post_group_list)
            one_post_group_list = []

        one_post_group_list.append(object_post)
    all_post_groups_list.append(one_post_group_list)

    return all_post_groups_list


def normalize_title(title: str):
    return ''.join(
        c for c in unicodedata.normalize('NFD', title)
        if unicodedata.category(c) != 'Mn').replace(' ', '_').lower()
