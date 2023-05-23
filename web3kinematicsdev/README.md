Web3 Kinematics tools and integration using Optimism MUD starter kit

How to install dependencies for development
===========================================

For development, install the Box2D library.

* Install `swig`,
   - On Ubuntu/Debian, run
    ```sudo apt install swig```
   - On Fedora/RHEL systems, run
    ```sudo dnf install swig```
* Install setuptools and pip,
   - On Ubuntu/Debian, run
   ```sudo apt install python3 python3-setuptools python3-pip python3-all-dev ```
   - On Fedora/RHEL, run
   ```sudo dnf install python3-pip python3-setuptools```
* Clone pybox2d and build, run
```
git clone https://github.com/pybox2d/pybox2d
cd pybox2d
# Make sure you have installed swig
python3 setup.py build
pip3 install . --system

```
