# Embedded JSON serialized Storage for Python

This is a key/value storage hosted in local file system for embedded systems like raspberry pi.

## Example of usage

    import models
    from models.group import Group
    from models.user import User
    
    if __name__ == '__main__':
        for obj in models.storage.all():
            print(obj)
    
        user1 = User(id='c92046b6-52b3-474d-9942-65dd8e8fb879')
        user1.name = "admin"
        user1.email = "admin@domain.com"
        user1.name = "Xpto user"
    
        group1 = Group(id='57787bed-9e6d-4ff8-af27-7b19a3129ede')
        group1.name = "Administrator"
        group2 = Group(id='c6bade24-1ee0-46d6-957c-86f1e0031cb9')
        group2.name = "Guest"
    
        models.storage.new(user1)
        models.storage.new(group1)
        models.storage.new(group2)
        models.storage.save()

