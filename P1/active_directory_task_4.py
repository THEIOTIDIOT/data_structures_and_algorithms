class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    groups = group.get_groups()

    if len(groups) < 1:
        return

    for item in groups:
        users = item.get_users()
        if len(users) > 0:
            for usr in users:
                if usr == user:
                    return print('FOUND')

    return print('NOTFOUND')


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
child.add_user('child_user')

if is_user_in_group('sub_child_user', parent):
    print('True')
else:
    print('False')