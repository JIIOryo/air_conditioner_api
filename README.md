# air_conditioner_api

air_conditioner_apiは、エアコンを操作するためのAPIサーバです。

# Endpoints

## PUT:/on/cool
<details>
<summary>
detail
</summary>

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

</details>

<!-- ------------------------------------------------------------------------------------ -->

## PUT:/on/hot
<details>
<summary>
detail
</summary>

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

</details>


<!-- ------------------------------------------------------------------------------------ -->


## PUT:/on/dehumidify
<details>
<summary>
detail
</summary>

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

</details>


<!-- ------------------------------------------------------------------------------------ -->


## DELETE:/off
<details>
<summary>
detail
</summary>

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

</details>


<!-- ------------------------------------------------------------------------------------ -->


## GET:/ping

<details>
<summary>
detail
</summary>

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

</details>



