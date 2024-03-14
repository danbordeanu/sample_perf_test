# Performance tests for AIM-API python backend

## DOCKER

### Build docker container

```bash
$ docker build -t eg_mech_perf .
```

### Run docker container on local machine

```bash
$ docker run -it --name perf - AIM_API_HOST=https://aim-pro-dev.host.com -e AIM_USER=user@host.com -e AIM_PASSWORD=md5password -v "$(pwd):/home" eg_mech_perf /bin/bash -c  "multimech-run aim_api_login_perf""
```

__!!!NB!!!__ By default, if env vars are not specified the test will run against the AKS/Kube deployment

```python
 self.host = os.environ.get('AIM_API_HOST', 'https://aim-pro-dev.host.com/')
        self.url_login = os.environ.get(self.host, '/api/aim/login')
        self.username = os.environ.get('AIM_USER')
        self.password = os.environ.get('AIM_PASSWORD')
```

### Run ab script

```bash
ab  -c 2 -n 60  -p ab_file.data -T  application/json -H 'Content-Type: application/json'  http://127.0.0.1:5000/api/aim/login/user@host.com
```

Results output artifacts are in $(pwd)/aim_api_login_perf/results directory


