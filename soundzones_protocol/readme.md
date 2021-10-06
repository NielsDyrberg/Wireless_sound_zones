
# Documentation for SoundZone Protocol
<!-- 
To compile puml use: (Assuming plantuml you are in the directory)
plantuml.jar -tsvg readme.md -o sequence_diagrams
-->

version = 0.0.2

This file will document SZP.

As it is a 7th layer protocol, it is treated as a Point-Point communication

| Defines | Values |
|---|---|
| IPv | IPv4 |
| Transport protocol | UDP |
| Port | 1695 ( Seemingly not used ) |
| Text encoding | utf-8 |
| Size of msg_len | 2 bytes |

## Main Structure

[msg_len, CID, {payload} ]

* msg_len - Length of message
* CID - Command Id
* payload - Data to send (Structure depends on the CID)

## Commands 

### Command groups

| Range | Name |
|---| ---|
| 0x00 - 0x10 | Normal use |
| 0xA0 - 0xC0 | Configuration |
| 0xF0 - 0xFF | Debugging |

### Command list

|CID | Name | Description |
|---|---|---|
| 0x01 | send | Send a payload to a client |
|||
| 0xA1 | enroll_c | Used by client to enroll |
| 0xA2 | enroll_s | Used by client to enroll |
| 0xB3 | set_sound_compression | Sets the compression for the music |
| 0xB4 | set_sample_rate | Sets the sample rate of the music |
|||
| 0xF1 | checkCon | Used to check connection, used for debug |

---

### 01 - send
This command is used to send sound data to the client.

| Tag | Size [bytes] | Value | Description | 
|---|---|---|---|
| msg_len | 2 | - | Length of message |
| cid | 1 | 0x01 | Command Id |
| time | 5 | - | Time to play the block of sound |
| payload | 1 | - | Payload |

<!--
```
@startuml 01_send
server -> client: [ msg_len, cid, time, payload ]
@enduml
```
-->

![](sequence_diagrams/01_send.svg)

#### Time Encoding
[ mm, ss, ms, µs, ns ]
| Byte| Range | Description | Symbol |
|---|---|---|---|
| 1 | [ 0-60 ] | Minute | mm |
| 2 | [ 0-60 ] | Second | ss |
| 3 | [ 0-1000 ] | Mili second | ms |
| 4 | [ 0-1000 ] | Micro second | µs |
| 5 | [ 0-1000 ] | Nano second | ns |

---

### A1 - enroll_c - client assigned id's
To use this command, client has been preconfigured with an Id.
So the rigth filter is used for the right Id.

In order for the client to be configured with an Id, it has to be planned where each client is located in the room, the master should then have the plan so it knows where wich id is located.
A client is then configured according to where it is located. And then uses this Id to enroll.


| Tag | Size [bytes] | Value | Description | 
|---|---|---|---|
| msg_len | 2 | - | Length of message |
| cid | 1 | 0xA1 | Command Id |
|  client_id | 1 | 0x01-0xFF | Assigned client id (0 is reserved for server) |
| res | 1 | 0 \| 1 | denie \| accept |

<!--
```
@startuml A1_enrole_c
server <- client: [ msg_len, cid, client_id ]
server -> client: [ msg_len, cid, res ]
@enduml
```
-->

![](sequence_diagrams/A1_enrole_c.svg)

---

### A2 - enroll_s - server assigned id's
By using this command there is no need for a preplanned Id, since the Server assignes Id's.
But in order to use it, the Server has to figure out where each client i located in the room, after the Id i assigned.

| Tag | Size [bytes] | Value | Description | 
|---|---|---|---|
| msg_len | 2 | - | Length of message |
| cid | 1 | 0xA2 | Command Id |
| client_id | 1 | 0x01-0xFF | Assigned client id |
| ack | 1 | 0x01 | Accepted |

<!--
```
@startuml A2_enrole_s
server <- client: [ msg_len, cid ]
server -> client: [ msg_len, cid, client_id ]
group succesful
    server <- client: [ msg_len, cid, ack]
end
@enduml
```
-->

![](sequence_diagrams/A2_enrole_s.svg)

---

### B3 - set_sound_format
Sets sound format.

| Tag | Size [bytes] | Value | Description | 
|---|---|---|---|
| msg_len | 2 | - | Length of message |
| cid | 1 | 0xB3 | Command Id |
| format_id | 1 | 0x01-0xFF | Payload format type |
| ack | 1 | 0x01 | Acknolegment |

<!--
```
@startuml B3_set_sound_format
server -> client: [ msg_len, cid, format_id ]
group succesful
    server <- client: [ msg_len, cid, ack ]
end
@enduml
```
-->

![](sequence_diagrams/B3_set_sound_format.svg)

**Supported** **format**
| Id | Name |
|--- |--- |
| 0x01 | Raw |
| 0x02 | WAV |
| 0x03 | FLAC|
| 0x04 | PCM |

---

### B4 - set_sample_rate
Sets the sample rate of the music

| Tag | Size [bytes] | Value | Description | 
|---|---|---|---|
| msg_len | 2 | - | Length of message |
| cid | 1 | 0xB4 | Command Id |
| sample_rate | 2 | - | Sample rate |
| ack | 1 | 0x01 | Acknolegment |

Supported sample rates: **1200**, **42000** [Hz] 

<!--
```
@startuml B4_set_sound_compression
server -> client: [ msg_len, cid, sample_rate ]
group succesful
    server <- client: [ msg_len, cid, ack ]
end
@enduml
```
-->

![](sequence_diagrams/B4_set_sound_compression.svg)

---

### F1 - checkCon
Used the ckeck Connection on SZP level

| Tag | Size [bytes] | Description | 
|---|---|---|
| msg_len | 2 | - | Length of message |
| cid | 1 | Command Id | 

<!--
```
@startuml F1_check_con
server -> client: [ msg_len, cid ]
group succesful
    server <- client: [ msg_len, cid ]
end
@enduml
```
-->

![](sequence_diagrams/F1_check_con.svg)