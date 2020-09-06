# air_conditioner_api

This is an API server with minimal functionality to control the air conditioner and is the wrapper for irrp.py which is part of the pigpio project.

# Environment

```
Raspberry Pi 3 model B
Python 3.7.3
```

# Setup

```sh

git clone https://github.com/JIIOryo/air_conditioner_api.git

cd air_conditioner_api

# install pigpio for python3
sudo apt install python3-pigpio -y

# pigpiod start
sudo systemctl enable pigpiod
sudo systemctl start pigpiod

# download irrp.py to project root path
curl http://abyz.me.uk/rpi/pigpio/code/irrp_py.zip | zcat > irrp.py

# pip install
pip3 install -r requirements.txt

# generate config file
cp config.json.template config.json

# run
python3 server.py


```

You need to connect the infrared LED to the GPIO set in config.json.

# Endpoints

## PUT:/on/cool
<details>
<summary>
detail
</summary>

### Request

#### Schema

```json
{
    "cool": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "number",
                "minimum": 16,
                "maximum": 31,
                "description": "Degree celsius of airflow from air conditioner."
            },
            "airflowLevel": {
                "type": "string",
                "enum": ["a", "1", "2", "3"],
                "description": "Level of airflow from air conditioner. a: auto, 1: low, 2: middle, 3: high"
            }
        },
        "required": [
            "temperature",
            "airflowLevel"
        ]
    }
}
```

#### Content-Type

`application/json`

#### Examples

```json
{
    "temperature": 26,
    "airflowLevel": "1"
}
```

```json
{
    "temperature": 23,
    "airflowLevel": "a"
}
```


### Response


#### Content-Type

`application/json`

#### Success example

```
{
  "code": 200,
  "message": "ok"
}
```

#### Error example

```
{
  "code": 400,
  "error": "ValidationError",
  "message": "Validation error ..."
}
````



</details>

<!-- ------------------------------------------------------------------------------------ -->

## PUT:/on/hot
<details>
<summary>
detail
</summary>

### Request

#### Schema

```json
{
    "hot": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "number",
                "minimum": 16,
                "maximum": 31,
                "description": "Degree celsius of airflow from air conditioner."
            },
            "airflowLevel": {
                "type": "string",
                "enum": [
                    "a",
                    "1",
                    "2",
                    "3"
                ],
                "description": "Level of airflow from air conditioner. a: auto, 1: low, 2: middle, 3: high"
            }
        },
        "required": [
            "temperature",
            "airflowLevel"
        ]
    }
}
```

#### Content-Type

`application/json`

#### Examples

```json
{
    "temperature": 26,
    "airflowLevel": "1"
}
```

```json
{
    "temperature": 23,
    "airflowLevel": "a"
}
```

### Response


#### Content-Type

`application/json`

#### Success example

```
{
  "code": 200,
  "message": "ok"
}
```

#### Error example

```
{
  "code": 400,
  "error": "ValidationError",
  "message": "Validation error ..."
}
````

</details>


<!-- ------------------------------------------------------------------------------------ -->


## PUT:/on/dehumidify
<details>
<summary>
detail
</summary>

### Request

#### Schema

```json
{
    "dehumidify": {
        "type": "object",
        "properties": {
            "dehumidificationLevel": {
                "type": "number",
                "minimum": 1,
                "maximum": 3,
                "description": "Level of dehumidification by air conditioner. 1: low, 2: middle, 3: high"
            },
            "airflowLevel": {
                "type": "string",
                "enum": [
                    "a",
                    "1",
                    "2",
                    "3"
                ],
                "description": "Level of airflow from air conditioner. a: auto, 1: low, 2: middle, 3: high"
            }
        },
        "required": [
            "dehumidificationLevel",
            "airflowLevel"
        ]
    }
}
```

#### Content-Type

`application/json`

#### Examples

```json
{
    "dehumidificationLevel": 1,
    "airflowLevel": "2"
}
```

```json
{
    "dehumidificationLevel": 3,
    "airflowLevel": "a"
}
```

### Response


#### Content-Type

`application/json`

#### Success example

```
{
  "code": 200,
  "message": "ok"
}
```

#### Error example

```
{
  "code": 400,
  "error": "ValidationError",
  "message": "Validation error ..."
}
````

</details>


<!-- ------------------------------------------------------------------------------------ -->


## DELETE:/off
<details>
<summary>
detail
</summary>

### Request

#### Schema

```json
None
```

#### Content-Type

`application/json`

#### Examples

```json
None
```

### Response


#### Content-Type

`application/json`

#### Success example

```
{
  "code": 200,
  "message": "ok"
}
```


</details>


<!-- ------------------------------------------------------------------------------------ -->


## GET:/ping

<details>
<summary>
detail
</summary>

### Request

#### Schema

```json
None
```

#### Content-Type

`application/json`

#### Examples

```json
None
```

### Response


#### Content-Type

`application/json`

#### Success example

```
{
  "code": 200,
  "message": "ok"
}
```


</details>


## GET:/

<details>
<summary>
detail
</summary>


This endpoint returns index.html with the minimally configured controller implemented.
    
#### Schema

```json
None
```

#### Content-Type

`text/html; charset=utf-8`

#### Page

<img src="https://github.com/JIIOryo/air_conditioner_api/blob/assets/assets/img/html.png?raw=true" width="500px">


</details>
