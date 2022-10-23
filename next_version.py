current_version = input().split(".")
current_version_str = ''.join(current_version)

current_version_int = int(current_version_str)
current_version_int += 1

new_version = list(str(current_version_int))
print(('.').join(new_version))