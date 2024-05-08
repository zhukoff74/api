# FAST API EXAMPLE

```bash
/home/user/code/diplom1-master/env/bin/gunicorn --workers 3 --bind unix:api.sock -m 007 main:app
```