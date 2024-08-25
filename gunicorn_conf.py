bind = "0.0.0.0:8080"  # Bind to all IP addresses on port 8000
backlog = 2048

workers = 2
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 30
keepalive = 2

limit_request_line = 4094
limit_request_fields = 50
limit_request_field_size = 8190

# Debugging
reload = False 

# Logging
loglevel = "debug"
accesslog = "-"  # Log to stdout
errorlog = "-"  # Log to stderr

# Proc Name
proc_name = "u2bdownload_asgi"
