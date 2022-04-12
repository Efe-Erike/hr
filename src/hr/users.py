import pwd
# we are naming our function fetch_users
def fetch_users():
# we will start with an empoty user list
    users = []
# now we are going to start a loop. show all of the users...
    for user in pwd.getpwall():
#and we will figure out if this is a system user or not with a couple of tests.
        if user.pw_uid >= 1000 and 'home' in user.pw_dir:
#if those are true, then we are going to run user.append and create a dictionary entry with four attributes: name, id, home, shell
            users.append({
                'name' : user.pw_name,
                'id' : user.pw_uid,
                'home' : user.pw_dir,
                'shell' : user.pw_shell,
            })
    return users
