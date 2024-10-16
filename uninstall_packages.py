# uninstall_packages.py
with open('installed_packages.txt', 'r') as file:
    packages = file.readlines()

# Uninstall each package
for package in packages:
    package_name = package.strip()
    if package_name:  # Ensure package name is not empty
        print(f"Uninstalling {package_name}")
        import os
        os.system(f"pip uninstall -y {package_name}")
