# darvester-api
<i>API Backend for a Darvester database</i>

- Curently a WIP
- Developed in Python primarily (yes, there is also a Rust project, I'll get to that later)

### [Darvester](https://github.com/V3ntus/darvester)
The main package. Discord OSINT and data harvesting toolkit
### [Darvester API Frontend](https://github.com/V3ntus/darvester-api-frontend)
To interface with this package


## Install:
### 1. Clone
```
git clone https://github.com/V3ntus/darvester-api; cd darvester-api
```
### 2. Setup
```
python3.9 -m venv env
source env/bin/activate
pip install -r requirements
```
*Note: Your harvested.db file should be in the same directory as this package. Command line arg and config should be added soon*
### 3. Run
```
python main.py --host 0.0.0.0 --port 3000
```
