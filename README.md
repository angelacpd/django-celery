# Django Celery

Based on [Learn Django - Celery](https://www.youtube.com/watch?v=fBfzE0yk97k&list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20)

## Dependencies

The tutorial uses pip en virtualenv to manage packages. You can install the python packages from requirements.txt,
however I decided to use poetry.

```shell
pip install --require-hashes -r requirements.txt
```

### Poetry
- Install `poetry`

```shell
pip install poetry
```

- Create a virtual environment

```shell
poetry env use ^3.8
```

- Activate the virtual environment
```shell
poetry shell
```

- Install dependencies
```shell
poetry install
```

- Export hashes to requirements.txt
```shell
poetry export -f requirements.txt --output requirements.txt
```

### RabbitMQ

- Install RabbitMQ
```shell
sudo apt-get install rabbitmq-server
```

- Enable Server
```shell
sudo systemctl enable rabbitmq-server
```

- Start Server
```shell
sudo systemctl start rabbitmq-server
```

- Check server status
```shell
systemctl status rabbitmq-server
```

- Stop server
```shell
sudo rabbitmqctl stop
```

## Run celery worker

Ubuntu OS
```shell
celery -A core worker --loglevel=info
```

Windows OS
```shell
celery -A core worker -l info --pool=solo
```

## Run tasks

- Open Django shell
```shell
python3 manage.py shell
```

- Import task
> from app1.tasks import add

- Run task with delay
> add.delay(4, 4)

- Output: 
<AsyncResult: 33443489-a3e7-46e1-a83a-5bfca33a6ce2>

- Result:
> [2022-01-03 14:33:09,787: INFO/MainProcess] Task app1.tasks.add[33443489-a3e7-46e1-a83a-5bfca33a6ce2] received

> [2022-01-03 14:33:09,788: INFO/ForkPoolWorker-8] Task app1.tasks.add[33443489-a3e7-46e1-a83a-5bfca33a6ce2] succeeded in 0.0002217720011685742s: 8

- Run task 'add' asynchronously
> add.apply_async((3, 3), countdown=5)

Output:
<AsyncResult: 8e3760ef-4257-4fbe-9813-4ea5a6711dec>

- Result:
> [2022-01-03 14:35:04,733: INFO/MainProcess] Task app1.tasks.add[8e3760ef-4257-4fbe-9813-4ea5a6711dec] received

> [2022-01-03 14:35:11,593: INFO/ForkPoolWorker-8] Task app1.tasks.add[8e3760ef-4257-4fbe-9813-4ea5a6711dec] succeeded in 0.00033385799906682223s: 6

Send Email review

- Go to http://localhost:8000/reviews/
- Fill the form

- Result:
> [2022-01-03 22:50:40,841: INFO/MainProcess] Task send_review_email_task[103684d2-0539-46b6-b1ec-341284688409] received

> [2022-01-03 22:50:40,843: INFO/ForkPoolWorker-8] send_review_email_task[103684d2-0539-46b6-b1ec-341284688409]: Send review email

> [2022-01-03 22:50:44,198: INFO/ForkPoolWorker-8] Task send_review_email_task[103684d2-0539-46b6-b1ec-341284688409] succeeded in 3.3558420879999176s: 1
