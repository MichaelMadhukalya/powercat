# powercat
`powercat` is a netcat like utility meant for `Windows OS`. It is a handy utility when running / experimenting with softwares like Apache Kafka, Flink using a a Windows dev box setup.
It can send lines of text typed by user to a specific server port using TCP protocol. The lines of text can then be consumed by Kafka or Flink listening on that specific port.
The following two pictures show the user sending lines of text to a simple Python server program listening to incoming data over TCP port 80. The server then simply echoes the data.

![powercat](https://github.com/user-attachments/assets/9dc0354f-5889-4bf7-a6fe-59834459cdad)

![pyserver](https://github.com/user-attachments/assets/fda65856-f004-4661-aad2-3b6f95276f9f)

### Usage
The Powercat utility can be used either by specifying an IP address or a DNS. If a DNS is specified it creates the host address to connect to based on the list of machine addresses that are 
returned and then using the first address from that list. The following describes a basic usage syntax for the tool:

```
# netcat like utility for windows using powershell
# usage: .\powercat -Address "127.0.0.1" -Port 80
# or .\powercat -Dns "localhost" -Port 80
```

Hopefully you will like this tool. Enjoy!
