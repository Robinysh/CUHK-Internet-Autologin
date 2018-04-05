#CUHK-Internet-Autologin

##How To Use
Install the dependencies from pip.
```
pip install -r requirements.txt
```
Run the following command to start auto monitoring.
```
python monitor.py
```

You may also run the following command to test if the log-in function works.
```
python login.py
```

##Settings
Edit your username and password inside `login.py`

Period for checking internet connection can be adjusted inside `monitor.py` at `SLEEP_TIME`, in terms of seconds. 

