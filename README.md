# Youtube2mp3

### Requisitos

```bash
user@machine:~$ sudo apt install ffmpeg
```

### Modo de Uso:

```python

user@machine:~$ virtualenv -p python3 env
user@machine:~$ source env/bin/activate
(env) user@machine:~$ pip install youtube-dl
(env) user@machine:~$ exit
user@machine:~$
```

```bash
user@machine:~$ git clone https://github.com/perseoq/Youtube2mp3.git
user@machine:~$ cd Youtube2mp3
user@machine:~$ /home/user/env/bin/python mp3.py
```

#### Recomiendo:
```bash

user@machine:~$ nano .bashrc
```
- Agrega
```
alias mp3 = '/home/user/env/bin/python mp3.py'
```
```
user@machine:~$ source .bashrc

user@machine:~$ mp3 
Agrega una dirección de YouTube: https://www.youtube.com/watch?v=He8prinKmR4
```
