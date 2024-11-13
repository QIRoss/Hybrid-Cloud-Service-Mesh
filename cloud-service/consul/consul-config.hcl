datacenter = "cloud"
data_dir = "/consul/data"
bind_addr = "0.0.0.0"
client_addr = "0.0.0.0"
server = true
ui = true

retry_join = ["127.0.0.1"]

connect {
  enabled = true
}

ports {
  grpc = 8502
}